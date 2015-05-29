##########################################################
##       CONFIGURATION FOR SUSY SingleLep TREES       ##
## skim condition: >= 0 loose leptons, no pt cuts or id ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import * 

# Lepton Preselection
# ele
lepAna.loose_electron_id = "POG_MVA_ID_Run2_NonTrig_Loose"
lepAna.loose_electron_pt  = 5
# mu
lepAna.loose_muon_pt  = 5

# Redefine what I need
lepAna.packedCandidates = 'packedPFCandidates'

# selec Iso
isolation = "miniIso"

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

#### FOR BUGGY T2Deg
#  lepAna.selected_muon_dxy = 100
#  lepAna.selected_muon_dz = 100
#  lepAna.selected_electron_dxy = 100
#  lepAna.selected_electron_dz = 100

dxy0fix = False
if dxy0fix:
  lepAna.loose_muon_dxy = 100
  lepAna.loose_muon_dz = 100
  lepAna.loose_electron_dxy = 100
  lepAna.loose_electron_dz = 100

  lepAna.inclusive_muon_dxy = 100
  lepAna.inclusive_muon_dz = 100
  lepAna.inclusive_electron_dxy = 100
  lepAna.inclusive_electron_dz = 100




# --- LEPTON SKIMMING ---
ttHLepSkim.minLeptons = 0
ttHLepSkim.maxLeptons = 999
#LepSkim.idCut  = ""
#LepSkim.ptCuts = []

# --- JET-LEPTON CLEANING ---
jetAna.minLepPt = 10

jetAna.mcGT = "PHYS14_V4_MC"
jetAna.doQG = True
jetAna.smearJets = False #should be false in susycore, already
jetAna.recalibrateJets = True #should be true in susycore, already
metAna.recalibrate = False #should be false in susycore, already
metAna.otherMETs = [\
  ("metTxy",('slimmedTxyMETs', 'std::vector<pat::MET>')),
  ("metRaw",('slimmedRAWMETs', 'std::vector<pat::MET>')),
  ]

isoTrackAna.setOff=False

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

## Single lepton + ST skim
from CMGTools.TTHAnalysis.analyzers.ttHSTSkimmer import ttHSTSkimmer
ttHSTSkimmer = cfg.Analyzer(
    ttHSTSkimmer, name='ttHSTSkimmer',
    minST = 200,
    )

from CMGTools.TTHAnalysis.analyzers.ttHReclusterJetsAnalyzer import ttHReclusterJetsAnalyzer
ttHReclusterJets = cfg.Analyzer(
    ttHReclusterJetsAnalyzer, name="ttHReclusterJetsAnalyzer",
    pTSubJet = 30,
    etaSubJet = 5.0,
            )

from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14  import *

triggerFlagsAna.triggerBits = {
#put trigger here for data
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


from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14  import *

triggerFlagsAna.triggerBits = {
#put trigger here for data
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

#-------- SAMPLES AND TRIGGERS -----------

from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *
#selectedComponents =  [TTJets]
#from CMGTools.TTHAnalysis.samples.samples_13TeV_private import *
selectedComponents = T2ttDeg



for comp in selectedComponents: splitFactor = len(comp.files)

#-------- SEQUENCE

sequence = cfg.Sequence(susyCoreSequence+[
    ttHEventAna,
#    ttHSTSkimmer,
#    ttHReclusterJets,
    treeProducer,
    ])


#-------- HOW TO RUN
test = 0
if test==1:
    # test a single component, using a single thread.
    #comp = TTJets
    #comp = T2DegStop_300_270
    comp = selectedComponents[0]
#    comp = SMS_T1tttt_2J_mGl1500_mLSP100
    comp.files = comp.files[:10]
    print "Files:",comp.files
    selectedComponents = [comp]
    comp.splitFactor = 1
elif test==2:
    # test all components (1 thread per component).
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]

from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],
                     events_class = Events)

