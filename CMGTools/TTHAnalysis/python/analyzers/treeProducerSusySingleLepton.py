from CMGTools.TTHAnalysis.analyzers.treeProducerSusyCore import *
from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *

susySingleLepton_globalVariables = susyCore_globalVariables + [


            ##-------- custom jets ------------------------------------------
            NTupleVariable("htJet25", lambda ev : ev.htJet25, help="H_{T} computed from leptons and jets (with |eta|<2.4, pt > 25 GeV)"),
            NTupleVariable("mhtJet25", lambda ev : ev.mhtJet25, help="H_{T}^{miss} computed from leptons and jets (with |eta|<2.4, pt > 25 GeV)"),
            NTupleVariable("htJet40j", lambda ev : ev.htJet40j, help="H_{T} computed from only jets (with |eta|<2.4, pt > 40 GeV)"),
            NTupleVariable("htJet40", lambda ev : ev.htJet40, help="H_{T} computed from leptons and jets (with |eta|<2.4, pt > 40 GeV)"),
            NTupleVariable("mhtJet40", lambda ev : ev.mhtJet40, help="H_{T}^{miss} computed from leptons and jets (with |eta|<2.4, pt > 40 GeV)"),
            NTupleVariable("nSoftBJetLoose25",  lambda ev: sum([(sv.mva>0.3 and (sv.jet == None or sv.jet.pt() < 25)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 25 passing CSV medium and SV from ivf with loose sv mva"),
            NTupleVariable("nSoftBJetMedium25", lambda ev: sum([(sv.mva>0.7 and (sv.jet == None or sv.jet.pt() < 25)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 25 passing CSV medium and SV from ivf with medium sv mva"),
            NTupleVariable("nSoftBJetTight25",  lambda ev: sum([(sv.mva>0.9 and (sv.jet == None or sv.jet.pt() < 25)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 25 passing CSV medium and SV from ivf with tight sv mva"),
#            NTupleVariable("metTxy_pt", lambda ev : ev.metTxy.pt(), help="E_{T}^{miss} Txy corrected"),
#            NTupleVariable("metTxy_phi", lambda ev : ev.metTxy.phi(), help="phi(E_{T}^{miss}) Txy corrected"),
#            NTupleVariable("metRaw_pt", lambda ev : ev.metRaw.pt(), help="E_{T}^{miss} raw"),
#            NTupleVariable("metRaw_phi", lambda ev : ev.metRaw.phi(), help="phi(E_{T}^{miss}) raw"),
            ##------------------------------------------------
]
susySingleLepton_globalObjects = susyCore_globalObjects.copy()
susySingleLepton_globalObjects.update({
            # put more here
})

susySingleLepton_collections = susyCore_collections.copy()
susySingleLepton_collections.update({

            # put more here
            "genParticles"     : NTupleCollection("genPartAll",  genParticleWithMotherId, 200, help="all pruned genparticles"), # need to decide which gen collection ?
            ## ---------------------------------------------
            "selectedLeptons" : NTupleCollection("LepGood", leptonTypeSusy, 8, help="Leptons after the preselection"),
            "otherLeptons"    : NTupleCollection("LepOther", leptonTypeSusy, 8, help="Leptons after the preselection"),
            "selectedTaus"    : NTupleCollection("TauGood", tauTypeSusy, 3, help="Taus after the preselection"),
            "selectedIsoTrack"    : NTupleCollection("isoTrack", isoTrackType, 50, help="isoTrack, sorted by pt"),
            ##------------------------------------------------
            "cleanJetsAll"       : NTupleCollection("Jet",     jetTypeSusy, 25, help="Cental jets after full selection and cleaning, sorted by pt"),
            "fatJets"         : NTupleCollection("FatJet",  fatJetType,  15, help="AK8 jets, sorted by pt"),
            "reclusteredFatJets" : NTupleCollection("RCFatJet",     fourVectorType,20, help="FatJets1.2 reclusterd from ak4 cleanJetsAll pT > 30, eta <5 "),
            #"cleanJetsAllAK4CHS"     : NTupleCollection("JetAK4CHS",  fatJetType,  15, help="for Cental reclustered AK4CHS after full selection and cleaning, sorted by pt "),
            ##------------------------------------------------
            ##   j['chef'] > 0.2 and j['neef']<0.7 and j['nhef']<0.7 and j['ceef'] < 0.5 and abs(j['eta']) < 2.4


            #"chHEF"            : NTupleCollection("Jet",  jetTypeSusyExtra,  25, help="chargedHadronEnergyFraction (relative to uncorrected jet energy)"),
            #"neHEF"            : NTupleCollection("Jet",  jetTypeSusyExtra,  25, help="neutralHadronEnergyFraction (relative to uncorrected jet energy)"),
            #"phEF"             : NTupleCollection("Jet",  jetTypeSusyExtra,  25, help="photonEnergyFraction (relative to corrected jet energy)"),
            #"eEF"              : NTupleCollection("Jet",  jetTypeSusyExtra,  25, help="electronEnergyFraction (relative to corrected jet energy)"),
            #"muEF"             : NTupleCollection("Jet",  jetTypeSusyExtra,  25, help="muonEnergyFraction (relative to corrected jet energy)"),
            #"HFHEF"            : NTupleCollection("Jet",  jetTypeSusyExtra,  25, help="HFHadronEnergyFraction (relative to corrected jet energy)"),
            #"HFEMEF"           : NTupleCollection("Jet",  jetTypeSusyExtra,  25, help="HFEMEnergyFraction (relative to corrected jet energy)"),
            #"chHMult"          : NTupleCollection("Jet",  jetTypeSusyExtra,  25, help="chargedHadronMultiplicity from PFJet.h"),
            #"neHMult"          : NTupleCollection("Jet",  jetTypeSusyExtra,  25, help="neutralHadronMultiplicity from PFJet.h"),
            #"phMult"           : NTupleCollection("Jet",  jetTypeSusyExtra,  25, help="photonMultiplicity from PFJet.h"),
            #"eMult"            : NTupleCollection("Jet",  jetTypeSusyExtra,  25, help="electronMultiplicity from PFJet.h"),
            #"muMult"           : NTupleCollection("Jet",  jetTypeSusyExtra,  25, help="muonMultiplicity from PFJet.h"),
            #"HFHMult"          : NTupleCollection("Jet",  jetTypeSusyExtra,  25, help="HFHadronMultiplicity from PFJet.h"),
            #"HFEMMult"         : NTupleCollection("Jet",  jetTypeSusyExtra,  25, help="HFEMMultiplicity from PFJet.h"),




            
            ## ---------------------------------------------
            "ivf"       : NTupleCollection("SV",     svType, 20, help="SVs from IVF"),
})

