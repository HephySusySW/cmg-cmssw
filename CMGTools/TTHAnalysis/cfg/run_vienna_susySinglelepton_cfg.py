##########################################################
##       CONFIGURATION FOR SUSY SingleLep TREES         ##
## skim condition: >= 1 loose leptons, no pt cuts or id ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

import os
#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

####### Leptons  #####
# lep collection
lepAna.packedCandidates = 'packedPFCandidates'

## ELECTRONS
lepAna.loose_electron_pt  = 5
eleID = "MVAID"

if eleID == "CBID":
  lepAna.loose_electron_id  = "POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto_full5x5"
  lepAna.loose_electron_lostHits = 999. # no cut
  lepAna.loose_electron_dxy    = 999.
  lepAna.loose_electron_dz     = 999.

  lepAna.inclusive_electron_id  = ""#"POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto_full5x5"
  lepAna.inclusive_electron_lostHits = 999. # no cut since embedded in ID
  lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
  lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID

elif eleID == "MVAID":
  inclusive_electron_id  = "" # same as in susyCore

  #lepAna.loose_electron_id = "POG_MVA_ID_Phys14_NonTrig_VLoose" # Phys14 era
  lepAna.loose_electron_id = "POG_MVA_ID_Spring15_NonTrig_VLoose" # Spring15 25ns era

elif eleID == "Incl": # as inclusive as possible
  lepAna.loose_electron_id  = ""
  lepAna.loose_electron_lostHits = 999. # no cut
  lepAna.loose_electron_dxy    = 999.
  lepAna.loose_electron_dz     = 999.

  lepAna.inclusive_electron_id  = ""
  lepAna.inclusive_electron_lostHits = 999.  # no cut
  lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
  lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID

## MUONS
lepAna.loose_muon_pt  = 3  ##loosen mu cut from 5GeV

# Isolation
isolation = "hybridIso"
#isolation = "miniIso"

if isolation == "miniIso":
  # do miniIso
  lepAna.doMiniIsolation = True
  lepAna.miniIsolationPUCorr = 'rhoArea'
  lepAna.miniIsolationVetoLeptons = None
  lepAna.loose_muon_isoCut     = lambda muon : muon.miniRelIso < 0.4
  lepAna.loose_electron_isoCut = lambda elec : elec.miniRelIso < 0.4
elif isolation == "relIso03":
  # normal relIso03
  lepAna.ele_isoCorr = "rhoArea"
  lepAna.mu_isoCorr = "rhoArea"

  lepAna.loose_electron_relIso = 0.5
  lepAna.loose_muon_relIso = 0.5

    


elif isolation == "hybridIso":
  lepAna.doMiniIsolation = False

  lepAna.ele_isoCorr = "rhoArea"
  lepAna.mu_isoCorr = "rhoArea"
  
  #lepAna.loose_muon_isoCut     =  lambda mu: ( (mu.pt() < 25  and mu.absIso04 < 5 ) or (mu.pt()>=25 and mu.relIso04 < 0.2 ) )
  lepAna.loose_muon_isoCut     =  lambda mu: ( (mu.pt() < 25  and mu.absIso03 < 15 ) or (mu.pt()>=25 and mu.relIso03 < 0.6 ) )
  #lepAna.loose_muon_isoCut     =  lambda mu: ( True )
  #lepAna.loose_electron_isoCut =  None # 
  lepAna.loose_electron_isoCut = lambda el: (  (el.pt() < 25  and el.absIso03 < 15 ) or (el.pt()>=25 and el.relIso03 < 0.6 )  )


# --- LEPTON SKIMMING ---
#ttHLepSkim.minLeptons = 1
ttHLepSkim.minLeptons = 0 # Loosen min lep requirement
ttHLepSkim.maxLeptons = 999
#LepSkim.idCut  = ""
#LepSkim.ptCuts = []

# --- JET-LEPTON CLEANING ---
jetAna.minLepPt = 10
jetAna.applyL2L3Residual = 'Data' 
jetAna.jetPt = 25
jetAna.jetEta = 5.2
jetAna.addJECShifts = True
jetAna.doQG = True
jetAna.smearJets = False #should be false in susycore, already
jetAna.recalibrateJets =  True #For data

metAna.recalibrate = False #should be false in susycore, already

isoTrackAna.setOff=False
genAna.allGenTaus = True
genAna.makePackedGenParticles=False
isoTrackAna.makeAllTracks=False


from PhysicsTools.Heppy.analyzers.objects.TrackAnalyzer import TrackAnalyzer
trackAna = cfg.Analyzer(
    TrackAnalyzer, name='trackAnalyzer',
    setOff=False,
    trackOpt="reco",
    do_mc_match=True,
    
    )
genTrackAna = cfg.Analyzer(
    TrackAnalyzer, name='GenTrackAnalyzer',
    setOff=False,
    trackOpt="gen"
    )







from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
ttHEventAna = cfg.Analyzer(
    ttHLepEventAnalyzer, name="ttHLepEventAnalyzer",
    minJets25 = 0,
    )

## Insert the FatJet, SV, HeavyFlavour analyzers in the sequence
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        ttHFatJetAna)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        ttHSVAna)
## Insert TrackAna in the sequence:
susyCoreSequence.insert(susyCoreSequence.index(metAna)+1,
                        genTrackAna)
susyCoreSequence.insert(susyCoreSequence.index(genTrackAna)+1,
                        trackAna)

from PhysicsTools.Heppy.analyzers.gen.LHEAnalyzer import LHEAnalyzer 
LHEAna = LHEAnalyzer.defaultConfig


### Single lepton + ST skim
#from CMGTools.TTHAnalysis.analyzers.ttHSTSkimmer import ttHSTSkimmer
#ttHSTSkimmer = cfg.Analyzer(
#    ttHSTSkimmer, name='ttHSTSkimmer',
#    minST = 200,
#    )

#from CMGTools.TTHAnalysis.analyzers.ttHReclusterJetsAnalyzer import ttHReclusterJetsAnalyzer
#ttHReclusterJets = cfg.Analyzer(
#    ttHReclusterJetsAnalyzer, name="ttHReclusterJetsAnalyzer",
#    pTSubJet = 30,
#    etaSubJet = 5.0,
#            )

from CMGTools.TTHAnalysis.analyzers.hbheAnalyzer import hbheAnalyzer
hbheFilterAna = cfg.Analyzer(
    hbheAnalyzer, name = 'hbheAnalyzer',
    IgnoreTS4TS5ifJetInLowBVRegion = False
)


#from CMGTools.RootTools.samples.triggers_13TeV_Spring15 import * # central trigger list
from CMGTools.RootTools.samples.triggers_13TeV_Spring15 import *
from CMGTools.RootTools.samples.triggers_13TeV_Spring15_1l import *
triggerFlagsAna.triggerBits = {
        ## hadronic
        'HT350' : triggers_HT350,
        'HT600' : triggers_HT600,
        'HT800' : triggers_HT800,
        'MET170' : triggers_MET170,
        'HT350MET120' : triggers_HT350MET120,
        'HT350MET100' : triggers_HT350MET100,
        'HTMET' : triggers_HT350MET100 + triggers_HT350MET120,
        ## muon
        'SingleMu' : triggers_1mu,
        'IsoMu27' : triggers_1mu,
        'IsoMu20' : triggers_1mu20,
        'Mu45eta2p1' : trigger_1mu_noiso_r,
        'Mu50' : trigger_1mu_noiso_w,
        'MuHT600' : triggers_mu_ht600,
        'MuHT400MET70' : triggers_mu_ht400_met70,
        'MuHT350MET70' : triggers_mu_ht350_met70,
        'MuHT350MET50' : triggers_mu_ht350_met50,
        'MuHT350' : triggers_mu_ht350,
        'MuHTMET' : triggers_mu_ht350_met70 + triggers_mu_ht400_met70,
        'MuMET120' : triggers_mu_met120,
        'MuHT400B': triggers_mu_ht400_btag,
        ## electrons
        'IsoEle32' : triggers_1el,
        'IsoEle23' : triggers_1el23,
        'IsoEle22' : triggers_1el22,
        'Ele105' : trigger_1el_noiso,
        'EleHT600' : triggers_el_ht600,
        'EleHT400MET70' : triggers_el_ht400_met70,
        'EleHT350MET70' : triggers_el_ht350_met70,
        'EleHT350MET50' : triggers_el_ht350_met50,
        'EleHT350' : triggers_el_ht350,
        'EleHTMET' : triggers_el_ht350_met70 + triggers_el_ht400_met70,
        'EleHT200' :triggers_el_ht200,
        'EleHT400B': triggers_el_ht400_btag,

#mumu
        'mumuIso' : triggers_mumu_iso,
        'mumuNoniso_50ns' : triggers_mumu_noniso_50ns,
        'mumuNoiso' : triggers_mumu_noniso,
        'mumuSS' : triggers_mumu_ss,
        'mumuHT' : triggers_mumu_ht,
# ee
        'ee_DZ': triggers_ee, 
#mue
        'mue':triggers_mue,
#dilepton+HT
        'ee_ht':triggers_ee_ht,
        'mue_ht':triggers_mue_ht,
#multi-lepton
        '3e':triggers_3e,
        '3mu':triggers_3mu,
        '3mu_alt':triggers_3mu_alt,
        '2mu1e':triggers_2mu1e,
        '2e1mu':triggers_2e1mu,
#fake rate
        'FR_1mu_iso':triggers_FR_1mu_iso,
        'FR_1mu_noiso':triggers_FR_1mu_noiso,
        'FR_1e_noiso':triggers_FR_1e_noiso,
        'FR_1e_iso':triggers_FR_1e_iso,
        'FR_1e_b2g':triggers_FR_1e_b2g,
#MET
        'Jet80MET90'       :triggers_Jet80MET90      ,
        'Jet80MET120'      :triggers_Jet80MET120     ,
        'MET120Mu5'        :triggers_MET120Mu5       ,

        #'MET170_pres'      :triggers_MET170_pres     , 
        #'MET250'           :triggers_MET250          ,
        #'MET90nc'          :triggers_MET90nc         ,
        #'MET120nc'         :triggers_MET120nc        ,
        #'MET90'            :triggers_MET90MHT90      ,
        #'MET120'           :triggers_MET120MHT120    ,
        #'PhysRates'        :triggers_PhysRate        ,
        #'Mu3erHT140MET125' :triggers_Mu3erHT140MET125,
        'DiPFJetAve100_HFJEC': ["HLT_DiPFJetAve100_HFJEC_v*"],
        'DiPFJetAve140': ["HLT_DiPFJetAve140_v*"],
        'DiPFJetAve160_HFJEC': ["HLT_DiPFJetAve160_HFJEC_v*"],
        'DiPFJetAve200': ["HLT_DiPFJetAve200_v*"],
        'DiPFJetAve220_HFJEC': ["HLT_DiPFJetAve220_HFJEC_v*"],
        'DiPFJetAve260': ["HLT_DiPFJetAve260_v*"],
        'DiPFJetAve300_HFJEC': ["HLT_DiPFJetAve300_HFJEC_v*"],
        'DiPFJetAve320': ["HLT_DiPFJetAve320_v*"],
        'DiPFJetAve40': ["HLT_DiPFJetAve40_v*"],
        'DiPFJetAve400': ["HLT_DiPFJetAve400_v*"],
        'DiPFJetAve500': ["HLT_DiPFJetAve500_v*"],
        'DiPFJetAve60_HFJEC': ["HLT_DiPFJetAve60_HFJEC_v*"],
        'DiPFJetAve60': ["HLT_DiPFJetAve60_v*"],
        'DiPFJetAve80_HFJEC': ["HLT_DiPFJetAve80_HFJEC_v*"],
        'DiPFJetAve80': ["HLT_DiPFJetAve80_v*"],




        ### MET PD::
        "CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72"                       :triggers_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72                        ,
        "CaloMHTNoPU90_PFMET90_PFMHT90_IDTight"                                   :triggers_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight                                    ,
        "MET200"                                                                  :triggers_HLT_MET200                                                      ,
        "MET250"                                                                  :triggers_HLT_MET250                                                                   ,
        "MET300"                                                                  :triggers_HLT_MET300                                                                   ,
        "MET60_IsoTrk35_Loose"                                                    :triggers_HLT_MET60_IsoTrk35_Loose                                                     ,
        "MET75_IsoTrk50"                                                          :triggers_HLT_MET75_IsoTrk50                                                           ,
        "MET90_IsoTrk50"                                                          :triggers_HLT_MET90_IsoTrk50                                                           ,
        "MonoCentralPFJet80_PFMETNoMu120_PFMH_PFMHTNoMu120_IDTight"               :triggers_HLT_MonoCentralPFJet80_PFMETNoMu120_PFMH_PFMHTNoMu120_IDTight   ,
        "MonoCentralPFJet80_PFMETNoMu90_PFMHT_PFMHTNoMu90_IDTight"                :triggers_HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHT_PFMHTNoMu90_IDTight    ,
        "Mu14er_PFMET100"                                                         :triggers_HLT_Mu14er_PFMET100                                             ,
        "Mu3er_PFHT140_PFMET125"                                                  :triggers_HLT_Mu3er_PFHT140_PFMET125                                      ,
        "Mu6_PFHT200_PFMET100"                                                    :triggers_HLT_Mu6_PFHT200_PFMET100                                        ,
        "Mu6_PFHT200_PFMET80_BTagCSV0p72"                                         :triggers_HLT_Mu6_PFHT200_PFMET80_BTagCSV0p72                             ,
        "PFMET100_PFMHT100_IDTight"                                               :triggers_HLT_PFMET100_PFMHT100_IDTight                                                ,
        "PFMET110_PFMHT110_IDTight"                                               :triggers_HLT_PFMET110_PFMHT110_IDTight                                                ,
        "PFMET120_BTagCSV0p72"                                                    :triggers_HLT_PFMET120_BTagCSV0p72                                        ,
        "PFMET120_Mu5"                                                            :triggers_HLT_PFMET120_Mu5                                                ,
        "PFMET120_PFMHT120_IDTight"                                               :triggers_HLT_PFMET120_PFMHT120_IDTight                                                ,
        "PFMET170_HBHECleaned"                                                    :triggers_HLT_PFMET170_HBHECleaned                                                     ,
        "PFMET170_JetIdCleaned"                                                   :triggers_HLT_PFMET170_JetIdCleaned                                                    ,
        "PFMET170_NoiseCleaned"                                                   :triggers_HLT_PFMET170_NoiseCleaned                                                    ,
        "PFMET170"                                                                :triggers_HLT_PFMET170                                                                 ,
        "PFMET300"                                                                :triggers_HLT_PFMET300                                                    ,
        "PFMET400"                                                                :triggers_HLT_PFMET400                                                    ,
        "PFMET90_PFMHT90_IDTight"                                                 :triggers_HLT_PFMET90_PFMHT90_IDTight                                                  ,
        "PFMETNoMu120_PFMHTNoMu120_IDTight"                                       :triggers_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight                           ,
        "PFMETNoMu90_PFMHTNoMu90_IDTight"                                         :triggers_HLT_PFMETNoMu90_PFMHTNoMu90_IDTight                             ,

        #### SingleMuon PD:
        "IsoMu17_eta2p1"         :  triggers_HLT_IsoMu17_eta2p1    ,
        "IsoMu18"                :  triggers_HLT_IsoMu18           ,
        "IsoMu20"                :  triggers_HLT_IsoMu20           ,
        "IsoMu22"                :  triggers_HLT_IsoMu22           ,
        "IsoMu27"                :  triggers_HLT_IsoMu27           ,
        "IsoTkMu18"              :  triggers_HLT_IsoTkMu18         ,
        "IsoTkMu20"              :  triggers_HLT_IsoTkMu20         ,
        "IsoTkMu22"              :  triggers_HLT_IsoTkMu22         ,
        "IsoTkMu27"              :  triggers_HLT_IsoTkMu27         ,
        "L1SingleMu16"           :  triggers_HLT_L1SingleMu16      ,
        "L1SingleMuOpen"         :  triggers_HLT_L1SingleMuOpen    ,
        "L2Mu10"                 :  triggers_HLT_L2Mu10            ,
        "Mu20"                   :  triggers_HLT_Mu20              ,
        "Mu24_eta2p1"            :  triggers_HLT_Mu24_eta2p1       ,
        "Mu27"                   :  triggers_HLT_Mu27              ,
        "Mu45_eta2p1"            :  triggers_HLT_Mu45_eta2p1       ,
        "Mu50"                   :  triggers_HLT_Mu50              ,
        "Mu55"                   :  triggers_HLT_Mu55              ,
        "TkMu20"                 :  triggers_HLT_TkMu20            ,
        "TkMu24_eta2p1"          :  triggers_HLT_TkMu24_eta2p1     ,



        }

# Tree Producer
from CMGTools.TTHAnalysis.analyzers.treeProducerSusySingleLepton import *
## Tree Producer
treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerSusySingleLepton',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     defaultFloatType = 'F', # use Float_t for floating point
     PDFWeights = PDFWeights,
     globalVariables = susySingleLepton_globalVariables,
     globalObjects = susySingleLepton_globalObjects,
     collections = susySingleLepton_collections,
)


#if os.environ.has_key("FASTSIM"):
#  isFastSim = os.environ["FASTSIM"].lower() == "true"
#else:
#  isFastSim = False
#
#extraSeq= [hbheFilterAna] if not isFastSim else[]


#!# #-------- SAMPLES AND SEQUENCE -----------

selectedComponents = [
        ]

sequence = cfg.Sequence(
  susyCoreSequence+ 
    #extraSeq +
      [
        LHEAna,
        ttHEventAna,
        treeProducer,
        ])


if os.environ.has_key("ISDATA"):
  isData = os.environ["ISDATA"].lower() == "true"
else:
  isData = False

print "------------------------------------------ isData: %s"%isData
#bx = '50ns'
bx = '25ns'

#if True or getHeppyOption("loadSamples"):
if getHeppyOption("loadSamples"):
  if not isData:
    from CMGTools.RootTools.samples.samples_13TeV_RunIISpring15MiniAODv2 import *

    from CMGTools.RootTools.samples.samples_13TeV_74X_susyT2DegStopPriv import *
    from CMGTools.RootTools.samples.samples_13TeV_signals import *

  if not isData and bx=='50ns':
    selectedComponents = [DYJetsToLL_M50_50ns]
    for comp in selectedComponents:
      comp.files=comp.files[:1]
      comp.splitFactor = 1 
  if not isData and bx=='25ns':
    #selectedComponents = [QCD_HT200to300]
    #selectedComponents = [ SMS_T2_4bd_mStop_400_mLSP_320to390,  SMS_T2_4bd_mStop_550to600_mLSP_470to590 ] 
    #selectedComponents = SignalT2DegFullScan 
    selectedComponents = [TTJets]
    #selectedComponents = [T2tt_300_270_FastSim]
    #selectedComponents = [T2DegStop_300_270_FastSim, T2DegStop_300_240_FastSim,T2DegStop_300_290_FastSim]
    for comp in selectedComponents:
#      comp.files=['root://xrootd.unl.edu//store/mc/RunIISpring15DR74/tZq_ll_4f_13TeV-amcatnlo-pythia8_TuneCUETP8M1/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/102EC100-5D2A-E511-A807-0CC47A4D99A4.root']
      comp.files = comp.files[:1]
      comp.splitFactor = len(comp.files) 
  if isData and bx=='50ns':
    from CMGTools.RootTools.samples.samples_13TeV_DATA2015 import *
    selectedComponents = [ MuonEG_Run2015B ]
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files 
        comp.isMC = False
        comp.isData = True
  if isData and bx=='25ns':
    from CMGTools.RootTools.samples.samples_13TeV_DATA2015 import *
    selectedComponents = [ DoubleMuon_Run2015D_Promptv4 ]
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[10:11]
        comp.json = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_246908-258750_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt" 
#        comp.files = [ 'root://eoscms.cern.ch//eos/cms/store/data/Run2015D/SingleMuon/MINIAOD/PromptReco-v3/000/256/676/00000/C2D5A4CC-F55F-E511-A02A-02163E0123FC.root'] 
        comp.isMC = False
        comp.isData = True
#        comp.json = None

from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
event_class = Events
if getHeppyOption("fetch"):
  event_class = EOSEventsWithDownload

print "Components"
print selectedComponents
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],
#                     preprocessor=preprocessor, # comment if pre-processor non needed
                     events_class = event_class)

