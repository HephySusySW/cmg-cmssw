##########################################################
##       CONFIGURATION FOR SUSY SingleLep TREES       ##
## skim condition: >= 0 loose leptons, no pt cuts or id ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg


#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import * 

lepAna.loose_muon_pt  = 5
lepAna.loose_muon_relIso = 0.5
lepAna.mu_isoCorr = "deltaBeta" 
lepAna.loose_electron_pt  = 7
lepAna.loose_electron_relIso = 0.5
lepAna.ele_isoCorr = "rhoArea" 
lepAna.ele_tightId = "Cuts_2012"


# Redefine what I need

# --- LEPTON SKIMMING ---
ttHLepSkim.minLeptons = 0
ttHLepSkim.maxLeptons = 999
#LepSkim.idCut  = ""
#LepSkim.ptCuts = []

# --- JET-LEPTON CLEANING ---
jetAna.minLepPt = 10 
#JetMCAna.smearJets     = False # do we need to smear the jets?
jetAna.smearJets = False

#ttHReclusterJets = cfg.Analyzer(
#            'ttHReclusterJetsAnalyzer',
#            )

# Event Analyzer for susy multi-lepton (at the moment, it's the TTH one)


isoTrackAna.setOff=False

#from CMGTools.TTHAnalysis.analyzers.ttHReclusterJetsAnalyzer  import ttHReclusterJetsAnalyzer
#ttHReclusterJets = cfg.Analyzer(
#    ttHReclusterJetsAnalyzer, name="ttHReclusterJetsAnalyzer",
#    )
from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
ttHEventAna = cfg.Analyzer(
    ttHLepEventAnalyzer, name="ttHLepEventAnalyzer",
    minJets25 = 0,
    )

## Insert the SV analyzer in the sequence
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        ttHFatJetAna)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        ttHSVAna)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        ttHHeavyFlavourHadronAna)



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
     PDFWeights = PDFWeights,
     globalVariables = susySingleLepton_globalVariables,
     globalObjects = susySingleLepton_globalObjects,
     collections = susySingleLepton_collections,
)



#-------- SAMPLES AND TRIGGERS -----------

from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *
from CMGTools.TTHAnalysis.samples.samples_13TeV_private_heplx import *
#selectedComponents = [ SingleMu, DoubleElectron, TTHToWW_PUS14, DYJetsToLL_M50_PU20bx25, TTJets_PUS14 ]
#selectedComponents =  WJetsToLNuHT #[WJetsToLNu] # + WJetsToLNuHT 
#selectedComponents = [TTJets]
#TTJets.splitFactor=1000
selectedComponents = QCDHT + [WJetsToLNu]  + DYJetsM50HT + SingleTop + [ TTWJets, TTZJets, TTH] + SusySignalSamples
#-------- SEQUENCE

sequence = cfg.Sequence(susyCoreSequence+[
    ttHEventAna,
#    ttHReclusterJets,
    treeProducer,
    ])


#-------- HOW TO RUN
test = 0
if test==1:
    # test a single component, using a single thread.
    comp = TTJets
    comp.files = comp.files[:1]
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
