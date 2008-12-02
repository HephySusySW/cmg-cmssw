#include <iostream>
#include <vector>
#include <memory>

// Framework
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Utilities/interface/Exception.h"

#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "Geometry/CaloGeometry/interface/CaloSubdetectorGeometry.h"
#include "Geometry/CaloTopology/interface/CaloTopology.h"
#include "Geometry/CaloEventSetup/interface/CaloTopologyRecord.h"


#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/EgammaReco/interface/ClusterShape.h"
#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/EgammaCandidates/interface/PhotonFwd.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "RecoEgamma/PhotonIdentification/interface/CutBasedPhotonID.h"

#include "DataFormats/EgammaReco/interface/ElectronPixelSeed.h"
#include "RecoCaloTools/Selectors/interface/CaloConeSelector.h"
#include "RecoEgamma/EgammaPhotonProducers/interface/PhotonProducer.h"



PhotonProducer::PhotonProducer(const edm::ParameterSet& config) : 
  conf_(config), 
  theLikelihoodCalc_(0)

{

  // use onfiguration file to setup input/output collection names
  scHybridBarrelProducer_       = conf_.getParameter<edm::InputTag>("scHybridBarrelProducer");
  scIslandEndcapProducer_       = conf_.getParameter<edm::InputTag>("scIslandEndcapProducer");
  barrelEcalHits_   = conf_.getParameter<edm::InputTag>("barrelEcalHits");
  endcapEcalHits_   = conf_.getParameter<edm::InputTag>("endcapEcalHits");

  conversionProducer_ = conf_.getParameter<std::string>("conversionProducer");
  conversionCollection_ = conf_.getParameter<std::string>("conversionCollection");
  vertexProducer_   = conf_.getParameter<std::string>("primaryVertexProducer");
  PhotonCollection_ = conf_.getParameter<std::string>("photonCollection");
  pixelSeedProducer_   = conf_.getParameter<std::string>("pixelSeedProducer");

  hbheLabel_        = conf_.getParameter<std::string>("hbheModule");
  hbheInstanceName_ = conf_.getParameter<std::string>("hbheInstance");
  hOverEConeSize_   = conf_.getParameter<double>("hOverEConeSize");
  maxHOverE_        = conf_.getParameter<double>("maxHOverE");
  minSCEt_        = conf_.getParameter<double>("minSCEt");
  highEt_        = conf_.getParameter<double>("highEt");
  minR9_        = conf_.getParameter<double>("minR9");
  likelihoodWeights_= conf_.getParameter<std::string>("MVA_weights_location");

  usePrimaryVertex_ = conf_.getParameter<bool>("usePrimaryVertex");
  risolveAmbiguity_ = conf_.getParameter<bool>("risolveConversionAmbiguity");

 
 
  // Parameters for the position calculation:
  std::map<std::string,double> providedParameters;
  providedParameters.insert(std::make_pair("LogWeighted",conf_.getParameter<bool>("posCalc_logweight")));
  providedParameters.insert(std::make_pair("T0_barl",conf_.getParameter<double>("posCalc_t0_barl")));
  providedParameters.insert(std::make_pair("T0_endc",conf_.getParameter<double>("posCalc_t0_endc")));
  providedParameters.insert(std::make_pair("T0_endcPresh",conf_.getParameter<double>("posCalc_t0_endcPresh")));
  providedParameters.insert(std::make_pair("W0",conf_.getParameter<double>("posCalc_w0")));
  providedParameters.insert(std::make_pair("X0",conf_.getParameter<double>("posCalc_x0")));
  posCalculator_ = PositionCalc(providedParameters);
  //
  preselCutValuesBarrel_.push_back(conf_.getParameter<double>("ecalRecHitSumBarrel")); 
  preselCutValuesBarrel_.push_back(conf_.getParameter<double>("hcalTowerSumBarrel"));
  preselCutValuesBarrel_.push_back(conf_.getParameter<double>("nTrackSolidConeBarrel"));
  preselCutValuesBarrel_.push_back(conf_.getParameter<double>("nTrackHollowConeBarrel"));     
  preselCutValuesBarrel_.push_back(conf_.getParameter<double>("trackPtSumSolidConeBarrel"));     
  preselCutValuesBarrel_.push_back(conf_.getParameter<double>("trackPtSumHollowConeBarrel"));     
  //  
  preselCutValuesEndcap_.push_back(conf_.getParameter<double>("ecalRecHitSumEndcap")); 
  preselCutValuesEndcap_.push_back(conf_.getParameter<double>("hcalTowerSumEndcap"));
  preselCutValuesEndcap_.push_back(conf_.getParameter<double>("nTrackSolidConeEndcap"));
  preselCutValuesEndcap_.push_back(conf_.getParameter<double>("nTrackHollowConeEndcap"));     
  preselCutValuesEndcap_.push_back(conf_.getParameter<double>("trackPtSumSolidConeEndcap"));     
  preselCutValuesEndcap_.push_back(conf_.getParameter<double>("trackPtSumHollowConeEndcap"));     
  //
  thePhotonIsolationCalculator_ = new PhotonIsolationCalculator();
  edm::ParameterSet isolationSumsCalculatorSet = conf_.getParameter<edm::ParameterSet>("isolationSumsCalculatorSet"); 
  thePhotonIsolationCalculator_->setup(isolationSumsCalculatorSet);


  // Register the product
  produces< reco::PhotonCollection >(PhotonCollection_);

}

PhotonProducer::~PhotonProducer() {

  delete theLikelihoodCalc_;
  delete thePhotonIsolationCalculator_;
}


void  PhotonProducer::beginJob (edm::EventSetup const & theEventSetup) {
  theLikelihoodCalc_ = new ConversionLikelihoodCalculator();
  edm::FileInPath path_mvaWeightFile(likelihoodWeights_.c_str() );
  theLikelihoodCalc_->setWeightsFile(path_mvaWeightFile.fullPath().c_str());


  // nEvt_=0;
}




void PhotonProducer::produce(edm::Event& theEvent, const edm::EventSetup& theEventSetup) {

  using namespace edm;
  //  nEvt_++;

  reco::PhotonCollection outputPhotonCollection;
  std::auto_ptr< reco::PhotonCollection > outputPhotonCollection_p(new reco::PhotonCollection);

  // Get the  Barrel Super Cluster collection
  bool validBarrelSCHandle=true;
  Handle<reco::SuperClusterCollection> scBarrelHandle;
  theEvent.getByLabel(scHybridBarrelProducer_,scBarrelHandle);
  if (!scBarrelHandle.isValid()) {
    edm::LogError("PhotonProducer") << "Error! Can't get the product "<<scHybridBarrelProducer_.label();
    bool validBarrelSCHandle=false;
  }


 // Get the  Endcap Super Cluster collection
  bool validEndcapSCHandle=true;
  Handle<reco::SuperClusterCollection> scEndcapHandle;
  theEvent.getByLabel(scIslandEndcapProducer_,scEndcapHandle);
  if (!scEndcapHandle.isValid()) {
    edm::LogError("PhotonProducer") << "Error! Can't get the product "<<scIslandEndcapProducer_.label();
    validEndcapSCHandle=false;
  }

  
 // Get EcalRecHits
  bool validEcalRecHits=true;
  Handle<EcalRecHitCollection> barrelHitHandle;
  EcalRecHitCollection barrelRecHits;
  theEvent.getByLabel(barrelEcalHits_, barrelHitHandle);
  if (!barrelHitHandle.isValid()) {
    edm::LogError("PhotonProducer") << "Error! Can't get the product "<<barrelEcalHits_.label();
    validEcalRecHits=false; 
  }
  if (  validEcalRecHits)  barrelRecHits = *(barrelHitHandle.product());

  
  Handle<EcalRecHitCollection> endcapHitHandle;
  theEvent.getByLabel(endcapEcalHits_, endcapHitHandle);
  EcalRecHitCollection endcapRecHits;
  if (!endcapHitHandle.isValid()) {
    edm::LogError("PhotonProducer") << "Error! Can't get the product "<<endcapEcalHits_.label();
    validEcalRecHits=false; 
  }
  if( validEcalRecHits) endcapRecHits = *(endcapHitHandle.product());


  // get the geometry from the event setup:
  theEventSetup.get<CaloGeometryRecord>().get(theCaloGeom_);
  const CaloGeometry* geometry = theCaloGeom_.product();
  const CaloSubdetectorGeometry *barrelGeometry = theCaloGeom_->getSubdetectorGeometry(DetId::Ecal, EcalBarrel);
  const CaloSubdetectorGeometry *endcapGeometry = theCaloGeom_->getSubdetectorGeometry(DetId::Ecal, EcalEndcap);
  const CaloSubdetectorGeometry *preshowerGeometry = theCaloGeom_->getSubdetectorGeometry(DetId::Ecal, EcalPreshower);

  edm::ESHandle<CaloTopology> pTopology;
  theEventSetup.get<CaloTopologyRecord>().get(theCaloTopo_);
  const CaloTopology *topology = theCaloTopo_.product();


  ///// Get the conversion collection
  validConversions_=true;
  edm::Handle<reco::ConversionCollection> conversionHandle; 
  theEvent.getByLabel(conversionProducer_, conversionCollection_ , conversionHandle);
  if (!conversionHandle.isValid()) {
    //if ( nEvt_%10==0 ) edm::LogError("PhotonProducer") << "Error! Can't get the product  "<<conversionCollection_.c_str() << " but keep running. Photons will be produced with null reference to conversions " << "\n";
    validConversions_=false;
  }
 


  // Get HoverE
  bool validHcalRecHits=true;
  Handle<HBHERecHitCollection> hbhe;
  std::auto_ptr<HBHERecHitMetaCollection> mhbhe;
  theEvent.getByLabel(hbheLabel_,hbheInstanceName_,hbhe);  
  if (!hbhe.isValid()) {
    edm::LogError("PhotonProducer") << "Error! Can't get the product "<<hbheInstanceName_.c_str();
    validHcalRecHits=false;
  }

  if ( hOverEConeSize_ > 0.) {
    if ( validHcalRecHits ) mhbhe=  std::auto_ptr<HBHERecHitMetaCollection>(new HBHERecHitMetaCollection(*hbhe));
  }

  
  theHoverEcalc_=HoECalculator(theCaloGeom_);

  // Get ElectronPixelSeeds
  validPixelSeeds_=true;
  Handle<reco::ElectronPixelSeedCollection> pixelSeedHandle;
  reco::ElectronPixelSeedCollection pixelSeeds;
  theEvent.getByLabel(pixelSeedProducer_, pixelSeedHandle);
  if (!pixelSeedHandle.isValid()) {
    //if ( nEvt_%100==0 ) std::cout << " PhotonProducer Can't get the product ElectronPixelSeedHandle but Photons will be produced anyway with pixel seed flag set to false "<< "\n";
    validPixelSeeds_=false;
  }
  if ( validPixelSeeds_) pixelSeeds = *(pixelSeedHandle.product());



  // Get the primary event vertex
  Handle<reco::VertexCollection> vertexHandle;
  reco::VertexCollection vertexCollection;
  bool validVertex=true;
  if ( usePrimaryVertex_ ) {
    theEvent.getByLabel(vertexProducer_, vertexHandle);
    if (!vertexHandle.isValid()) {
      edm::LogError("PhotonProducer") << "Error! Can't get the product primary Vertex Collection "<< "\n";
      validVertex=false;
    }
    if (validVertex) vertexCollection = *(vertexHandle.product());
  }
  math::XYZPoint vtx(0.,0.,0.);
  if (vertexCollection.size()>0) vtx = vertexCollection.begin()->position();

  edm::LogInfo("PhotonProducer") << "Constructing Photon 4-vectors assuming primary vertex position: " << vtx << std::endl;

  int iSC=0; // index in photon collection
  // Loop over barrel and endcap SC collections and fill the  photon collection
  if ( validBarrelSCHandle) fillPhotonCollection(theEvent,
						 theEventSetup,
						 scBarrelHandle,
						 geometry, 
						 barrelGeometry,
						 preshowerGeometry,
						 topology,
						 &barrelRecHits,
						 mhbhe.get(),
						 preselCutValuesBarrel_,
						 conversionHandle,
						 pixelSeeds,
						 vtx,
						 outputPhotonCollection,
						 iSC);
  if ( validEndcapSCHandle) fillPhotonCollection(theEvent,
						 theEventSetup,
						 scEndcapHandle,
						 geometry, 
						 endcapGeometry,
						 preshowerGeometry,
						 topology,
						 &endcapRecHits,
						 mhbhe.get(),
						 preselCutValuesEndcap_,
						 conversionHandle,
						 pixelSeeds,
						 vtx,
						 outputPhotonCollection,
						 iSC);

  // put the product in the event
  edm::LogInfo("PhotonProducer") << " Put in the event " << iSC << " Photon Candidates \n";
  outputPhotonCollection_p->assign(outputPhotonCollection.begin(),outputPhotonCollection.end());
  theEvent.put( outputPhotonCollection_p, PhotonCollection_);

}

void PhotonProducer::fillPhotonCollection(edm::Event& evt,
					  edm::EventSetup const & es,
					  const edm::Handle<reco::SuperClusterCollection> & scHandle,
					  const CaloGeometry *geometry,
					  const CaloSubdetectorGeometry *subDetGeometry,
					  const CaloSubdetectorGeometry *geometryES,
					  const CaloTopology *topology,
					  const EcalRecHitCollection* hits,
					  HBHERecHitMetaCollection *mhbhe,
					  std::vector<double> preselCutValues,
					  const edm::Handle<reco::ConversionCollection> & conversionHandle,
					  const reco::ElectronPixelSeedCollection& pixelSeeds,
					  math::XYZPoint & vtx,
					  reco::PhotonCollection & outputPhotonCollection, int& iSC) {
  

  reco::ElectronPixelSeedCollection::const_iterator pixelSeedItr;
  for(unsigned int lSC=0; lSC < scHandle->size(); lSC++) {
    
    // get SuperClusterRef
    reco::SuperClusterRef scRef(reco::SuperClusterRef(scHandle, lSC));
    iSC++;
    const reco::SuperCluster* pClus=&(*scRef);
    
    // SC energy preselection
    if (scRef->energy()/cosh(scRef->eta()) <= minSCEt_) continue;
    // calculate HoE
    double HoE=theHoverEcalc_(pClus,mhbhe);

    
    // recalculate position of seed BasicCluster taking shower depth for unconverted photon
    math::XYZPoint unconvPos = posCalculator_.Calculate_Location(scRef->seed()->getHitsByDetId(),hits,subDetGeometry,geometryES);

    static std::pair<DetId, float> maxXtal = EcalClusterTools::getMaximum (*(scRef->seed()), &(*hits) );
    float e1x5    =   EcalClusterTools::e1x5(  *(scRef->seed()), &(*hits), &(*topology)); 
    float e2x5    =   EcalClusterTools::e2x5Max(  *(scRef->seed()), &(*hits), &(*topology)); 
    float e3x3    =   EcalClusterTools::e3x3(  *(scRef->seed()), &(*hits), &(*topology)); 
    float e5x5    = EcalClusterTools::e5x5( *(scRef->seed()), &(*hits), &(*topology)); 
    std::vector<float> cov =  EcalClusterTools::covariances( *(scRef->seed()), &(*hits), &(*topology), geometry); 
    float covEtaEta = cov[0];
    std::vector<float> locCov =  EcalClusterTools::localCovariances( *(scRef->seed()), &(*hits), &(*topology)); 
    float covIetaIeta = locCov[0];


    float r9 =e3x3/(scRef->rawEnergy());
    // compute position of ECAL shower
    math::XYZPoint caloPosition;
    double photonEnergy=0;
    if (r9>minR9_) {
      caloPosition = unconvPos;
      photonEnergy=e5x5;
    } else {
      caloPosition = scRef->position();
      photonEnergy=scRef->energy();
    }
    
    // does the SuperCluster have a matched pixel seed?
    bool hasSeed = false;
    if ( validPixelSeeds_) {
      for(pixelSeedItr = pixelSeeds.begin(); pixelSeedItr != pixelSeeds.end(); pixelSeedItr++) {
	if (fabs(pixelSeedItr->superCluster()->eta() - scRef->eta()) < 0.0001 &&
	    fabs(pixelSeedItr->superCluster()->phi() - scRef->phi()) < 0.0001) {
	  hasSeed=true;
	  break;
	}
      }
    }
    
    // compute momentum vector of photon from primary vertex and cluster position
    math::XYZVector direction = caloPosition - vtx;
    math::XYZVector momentum = direction.unit() * photonEnergy ;

    const reco::Particle::LorentzVector  p4(momentum.x(), momentum.y(), momentum.z(), photonEnergy );
    
    reco::Photon newCandidate(p4, caloPosition, scRef, HoE, hasSeed, vtx);
    newCandidate.setShowerShapeVariables ( maxXtal.second, e1x5, e2x5,  e3x3, e5x5, covEtaEta,  covIetaIeta );
    //std::cout << " PhotonProducer e1x5 " << newCandidate.e1x5() << " e5x5 " <<   newCandidate.e5x5() << " max Xtal " << newCandidate.maxEnergyXtal() <<  std::endl;

    PhotonFiducialFlags fidFlags;
    PhotonIsolationVariables isolVarR03, isolVarR04;

    thePhotonIsolationCalculator_-> calculate ( &newCandidate,evt,es,fidFlags,isolVarR04, isolVarR03);

    newCandidate.setFiducialVolumeFlags (fidFlags.isEBPho, 
					 fidFlags.isEEPho, 
					 fidFlags.isEBGap, 
					 fidFlags.isEEGap, 
					 fidFlags.isEBEEGap  );    
    newCandidate.setIsolationVariablesConeDR04 (isolVarR04.isolationEcalRecHit, 
					      isolVarR04.isolationHcalTower, 
					      isolVarR04.isolationSolidTrkCone,
					      isolVarR04.isolationHollowTrkCone,
					      isolVarR04.nTrkSolidCone,
					      isolVarR04.nTrkHollowCone);    
    newCandidate.setIsolationVariablesConeDR03 (isolVarR03.isolationEcalRecHit, 
					      isolVarR03.isolationHcalTower, 
					      isolVarR03.isolationSolidTrkCone,
					      isolVarR03.isolationHollowTrkCone,
					      isolVarR03.nTrkSolidCone,
					      isolVarR03.nTrkHollowCone);    

    /// Pre-selection loose  isolation cuts
    bool isLooseEM=true;
    //    std::cout << " Photon Et " <<  newCandidate.pt() << std::endl;
    if ( newCandidate.pt() < highEt_) { 
      std::cout << " This photon Et is below " << highEt_ << " so I apply pre-selection ID cuts " << std::endl;
      if ( newCandidate.hadronicOverEm()                >= maxHOverE_ )              isLooseEM=false;
      if ( newCandidate.ecalRecHitSumConeDR04()          > preselCutValues[0] )      isLooseEM=false;
      if ( newCandidate.hcalTowerSumConeDR04()           > preselCutValues[1] )      isLooseEM=false;
      if ( newCandidate.nTrkSolidConeDR04()              > int(preselCutValues[2]) ) isLooseEM=false;
      if ( newCandidate.nTrkHollowConeDR04()             > int(preselCutValues[3]) ) isLooseEM=false;
      if ( newCandidate.isolationTrkSolidConeDR04()      > preselCutValues[4] )      isLooseEM=false;
      if ( newCandidate.isolationTrkHollowConeDR04()     > preselCutValues[5] )      isLooseEM=false;
    } 


    if ( isLooseEM) {
    
    
      if ( validConversions_) {
	
      if ( risolveAmbiguity_ ) { 
	
        reco::ConversionRef bestRef=solveAmbiguity( conversionHandle , scRef);	
	
	if (bestRef.isNonnull() ) newCandidate.addConversion(bestRef);	
	
	
      } else {
	

	for( unsigned int icp = 0;  icp < conversionHandle->size(); icp++) {
	  
	  reco::ConversionRef cpRef(reco::ConversionRef(conversionHandle,icp));
          
          if (!( scRef.id() == cpRef->caloCluster()[0].id() && scRef.key() == cpRef->caloCluster()[0].key() )) continue; 
	  if ( !cpRef->isConverted() ) continue;  
	  newCandidate.addConversion(cpRef);     

	}	  
	
      } // solve or not the ambiguity	     
      
    }

   
    outputPhotonCollection.push_back(newCandidate);
    
    }    
  }

}



reco::ConversionRef  PhotonProducer::solveAmbiguity(const edm::Handle<reco::ConversionCollection> & conversionHandle, reco::SuperClusterRef& scRef) {

  std::multimap<reco::ConversionRef, double >   convMap;


  for ( unsigned int icp=0; icp< conversionHandle->size(); icp++) {
    reco::ConversionRef cpRef(reco::ConversionRef(conversionHandle,icp));
    //icp++;      

    if (!( scRef.id() == cpRef->caloCluster()[0].id() && scRef.key() == cpRef->caloCluster()[0].key() )) continue;    
    if ( !cpRef->isConverted() ) continue;  
    
    double like = theLikelihoodCalc_->calculateLikelihood(cpRef);
    //    std::cout << " Like " << like << std::endl;
    convMap.insert ( std::make_pair(cpRef,like) ) ;
  }		     
  
  
  
  std::multimap<reco::ConversionRef, double >::iterator  iMap; 
  double max_lh = -1.;
  reco::ConversionRef bestRef;
  //std::cout << " Pick up the best conv " << std::endl;
  for (iMap=convMap.begin();  iMap!=convMap.end(); iMap++) {
    double like = iMap->second;
    if (like > max_lh) { 
      max_lh = like;
      bestRef=iMap->first;
    }
  }            
  
  //std::cout << " Best conv like " << max_lh << std::endl;    
  
  float ep=0;
  if ( max_lh <0 ) {
    //  std::cout << " Candidates with only one track " << std::endl;
    /// only one track reconstructed. Pick the one with best E/P
    float epMin=999; 
    
    for (iMap=convMap.begin();  iMap!=convMap.end(); iMap++) {
      reco::ConversionRef convRef=iMap->first;
      std::vector<reco::TrackRef> tracks = convRef->tracks();	
	    float px=tracks[0]->innerMomentum().x();
	    float py=tracks[0]->innerMomentum().y();
	    float pz=tracks[0]->innerMomentum().z();
	    float p=sqrt(px*px+py*py+pz*pz);
	    ep=fabs(1.-convRef->caloCluster()[0]->energy()/p);
	    //    std::cout << " 1-E/P = " << ep << std::endl;
	    if ( ep<epMin) {
	      epMin=ep;
	      bestRef=iMap->first;
	    }
    }
    //std::cout << " Best conv 1-E/P " << ep << std::endl;    
            
  }
  

  return bestRef;
  
  
} 

///// Obsolete 
double PhotonProducer::hOverE(const reco::SuperClusterRef & scRef,
			      HBHERecHitMetaCollection *mhbhe){

  ////// this is obsolete. Taking the calculator in EgammaTools instead
  double HoE=0;
  if (mhbhe) {
    CaloConeSelector sel(hOverEConeSize_, theCaloGeom_.product(), DetId::Hcal);
    GlobalPoint pclu((*scRef).x(),(*scRef).y(),(*scRef).z());
    double hcalEnergy = 0.;
    std::auto_ptr<CaloRecHitMetaCollectionV> chosen=sel.select(pclu,*mhbhe);
    for (CaloRecHitMetaCollectionV::const_iterator i=chosen->begin(); i!=chosen->end(); i++) {
      hcalEnergy += i->energy();
    }
    HoE= hcalEnergy/(*scRef).energy();
    LogDebug("") << "H/E : " << HoE;
  }
  return HoE;
}
