import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### Signals, 25 ns

ZprimeToTT_M2000_W200 = kreator.makeMCComponent("ZprimeToTT_M2000_W200", "/ZprimeToTT_M-2000_W-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
ZprimeToTT_M2000_W20 = kreator.makeMCComponent("ZprimeToTT_M2000_W20", "/ZprimeToTT_M-2000_W-20_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
ZprimeToTT_M2000_W600 = kreator.makeMCComponent("ZprimeToTT_M2000_W600", "/ZprimeToTT_M-2000_W-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)

ZprimeToTT_M3000_W300 = kreator.makeMCComponent("ZprimeToTT_M3000_W300", "/ZprimeToTT_M-3000_W-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
ZprimeToTT_M3000_W30 = kreator.makeMCComponent("ZprimeToTT_M3000_W30", "/ZprimeToTT_M-3000_W-30_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
ZprimeToTT_M3000_W900 = kreator.makeMCComponent("ZprimeToTT_M3000_W900", "/ZprimeToTT_M-3000_W-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)

ZprimeToTauTau_M2000 = kreator.makeMCComponent("ZprimeToTauTau_M2000", "/ZprimeToTauTau_M_2000_TuneCUETP8M1_tauola_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
ZprimeToTauTau_M3000= kreator.makeMCComponent("ZprimeToTauTau_M3000", "/ZprimeToTauTau_M_3000_TuneCUETP8M1_tauola_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)

ZprimeToTprimeT_TprimeToHT_MZp2000Nar_MTp1200Nar_LH = kreator.makeMCComponent("ZprimeToTprimeT_TprimeToHT_MZp2000Nar_MTp1200Nar_LH", "/ZprimeToTprimeT_TprimeToHT_MZp-2000Nar_MTp-1200Nar_LH_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)

ZprimeToWW_narrow_M2000 = kreator.makeMCComponent("ZprimeToWW_narrow_M2000", "/ZprimeToWW_narrow_M-2000_13TeV-madgraph/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
ZprimeToWW_narrow_M3000 = kreator.makeMCComponent("ZprimeToWW_narrow_M3000", "/ZprimeToWW_narrow_M-3000_13TeV-madgraph/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
ZprimeToWW_narrow_M4500 = kreator.makeMCComponent("ZprimeToWW_narrow_M4500", "/ZprimeToWW_narrow_M-4500_13TeV-madgraph/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)

ZprimeToZhToZinvhbb_narrow_M2000 = kreator.makeMCComponent("ZprimeToZhToZinvhbb_narrow_M2000", "/ZprimeToZhToZinvhbb_narrow_M-2000_13TeV-madgraph/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
ZprimeToZhToZinvhbb_narrow_M3000 = kreator.makeMCComponent("ZprimeToZhToZinvhbb_narrow_M3000", "/ZprimeToZhToZinvhbb_narrow_M-3000_13TeV-madgraph/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
ZprimeToZhToZinvhbb_narrow_M4500 = kreator.makeMCComponent("ZprimeToZhToZinvhbb_narrow_M4500", "/ZprimeToZhToZinvhbb_narrow_M-4500_13TeV-madgraph/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)

WprimeToMuNu_M2000 = kreator.makeMCComponent("WprimeToMuNu_M2000", "/WprimeToMuNu_M-2000_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
WprimeToENu_M2000 = kreator.makeMCComponent("WprimeToENu_M2000", "/WprimeToENu_M-2000_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
WprimeToTauNu_M2000 = kreator.makeMCComponent("WprimeToTauNu_M2000", "/WprimeToTauNu_M-2000_TuneCUETP8M1_13TeV-pythia8-tauola/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)

WprimeToWZ_M2000 = kreator.makeMCComponent("WprimeToWZ_M2000", "/WprimeToWZ_M-2000_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
WprimeToWhToWlephbb_narrow_M2000 = kreator.makeMCComponent("WprimeToWhToWlephbb_narrow_M2000", "/WprimeToWhToWlephbb_narrow_M-2000_13TeV-madgraph/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
WprimeToTB_plusSM_TToLep_M2000  = kreator.makeMCComponent("WprimeToTB_plusSM_TToLep_M2000", "/WprimeToTB_plusSM_TToLep_M-2000_LH_TuneCUETP8M1_13TeV-comphep-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
WprimeToTB_TToLep_M2000 = kreator.makeMCComponent("WprimeToTB_TToLep_M2000", "/WprimeToTB_TToLep_M-2000_RH_TuneCUETP8M1_13TeV-comphep-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)

SignalEXO = [ ZprimeToTT_M2000_W200, ZprimeToTT_M2000_W20, ZprimeToTT_M2000_W600, ZprimeToTT_M3000_W300, ZprimeToTT_M3000_W30, ZprimeToTT_M3000_W900, ZprimeToTauTau_M2000, ZprimeToTauTau_M3000, ZprimeToTprimeT_TprimeToHT_MZp2000Nar_MTp1200Nar_LH, ZprimeToWW_narrow_M2000, ZprimeToWW_narrow_M3000, ZprimeToWW_narrow_M4500, ZprimeToZhToZinvhbb_narrow_M2000, ZprimeToZhToZinvhbb_narrow_M3000, ZprimeToZhToZinvhbb_narrow_M4500, WprimeToMuNu_M2000, WprimeToENu_M2000, WprimeToTauNu_M2000, WprimeToWZ_M2000, WprimeToWhToWlephbb_narrow_M2000, WprimeToTB_plusSM_TToLep_M2000, WprimeToTB_TToLep_M2000 ]

#BulkGravToZZToZlepZhad_narrow_M2000 = kreator.makeMCComponent("BulkGravToZZToZlepZhad_narrow_M2000", "/BulkGravToZZToZlepZhad_narrow_M-2000_13TeV-madgraph/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
#RSGravToZZ_kMpl01_M2000 = kreator.makeMCComponent("RSGravToZZ_kMpl01_M2000", "/RSGravToZZ_kMpl01_M-2000_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
#
#SignalEXO_50ns = SignalEX0_50ns + [ BulkGravToZZToZlepZhad_narrow_M2000, RSGravToZZ_kMpl01_M2000 ]

SMS_T1bbbb_mGluino1000_mLSP900 = kreator.makeMCComponent("SMS_T1bbbb_mGluino1000_mLSP900", "/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 0.325388, useAAA=True)
SMS_T1bbbb_mGluino1500_mLSP100 = kreator.makeMCComponent("SMS_T1bbbb_mGluino1500_mLSP100", "/SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 0.0141903, useAAA=True)
SMS_T1qqqq_mGluino1000_mLSP800 = kreator.makeMCComponent("SMS_T1qqqq_mGluino1000_mLSP800", "/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 0.325388, useAAA=True)
SMS_T1qqqq_mGluino1400_mLSP100 = kreator.makeMCComponent("SMS_T1qqqq_mGluino1400_mLSP100", "/SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 0.0252977, useAAA=True)
SMS_T1tttt_mGluino1200_mLSP800 = kreator.makeMCComponent("SMS_T1tttt_mGluino1200_mLSP800", "/SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 0.0856418, useAAA=True) 
SMS_T1tttt_mGluino1500_mLSP100 = kreator.makeMCComponent("SMS_T1tttt_mGluino1500_mLSP100", "/SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 0.0141903, useAAA=True)

SignalSUSY = [ SMS_T1bbbb_mGluino1000_mLSP900, SMS_T1bbbb_mGluino1500_mLSP100, SMS_T1qqqq_mGluino1000_mLSP800, SMS_T1qqqq_mGluino1400_mLSP100, SMS_T1tttt_mGluino1200_mLSP800, SMS_T1tttt_mGluino1500_mLSP100 ]

SMS_T1bbbb_mGluino1000_1025_mLSP1to975_1000 = kreator.makeMCComponent("SMS_T1bbbb_mGluino1000_1025_mLSP1to975_1000", "/SMS-T1bbbb_mGluino-1000-1025_mLSP-1to975-1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
SMS_T1bbbb_mGluino1450_1500_mLSP250to1400_1350to1450 = kreator.makeMCComponent("SMS_T1bbbb_mGluino1450_1500_mLSP250to1400_1350to1450", "/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)
SMS_T1bbbb_mGluino1500_1550_mLSP1to1300_1000to1300 = kreator.makeMCComponent("SMS_T1bbbb_mGluino1500_1550_mLSP1to1300_1000to1300", "/SMS-T1bbbb_mGluino-1500-1550_mLSP-1to1300-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.0, useAAA=True)

SignalSUSYFullScan = [ SMS_T1bbbb_mGluino1000_1025_mLSP1to975_1000, SMS_T1bbbb_mGluino1500_1550_mLSP1to1300_1000to1300 ]



SMS_T2_4bd_mStop_100_mLSP_20to90        = kreator.makeMCComponent("SMS_T2_4bd_mStop_100_mLSP_20to90","/SMS-T2-4bd_mStop-100_mLSP-20to90_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root",  1521.11        )
SMS_T2_4bd_mStop_125_mLSP_45to115       = kreator.makeMCComponent("SMS_T2_4bd_mStop_125_mLSP_45to115","/SMS-T2-4bd_mStop-125_mLSP-45to115_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root",  574.981      )
SMS_T2_4bd_mStop_150_mLSP_45to115       = kreator.makeMCComponent("SMS_T2_4bd_mStop_150_mLSP_45to115","/SMS-T2-4bd_mStop-150_mLSP-70to140_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root",  249.409      )
SMS_T2_4bd_mStop_175_mLSP_95to165       = kreator.makeMCComponent("SMS_T2_4bd_mStop_175_mLSP_95to165","/SMS-T2-4bd_mStop-175_mLSP-95to165_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root",  121.416      )
SMS_T2_4bd_mStop_200_mLSP_120to190      = kreator.makeMCComponent("SMS_T2_4bd_mStop_200_mLSP_120to190","/SMS-T2-4bd_mStop-200_mLSP-120to190_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 64.5085     )
SMS_T2_4bd_mStop_225_mLSP_145to225      = kreator.makeMCComponent("SMS_T2_4bd_mStop_225_mLSP_145to225","/SMS-T2-4bd_mStop-225_mLSP-145to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 36.3818     )
SMS_T2_4bd_mStop_250_mLSP_170to240      = kreator.makeMCComponent("SMS_T2_4bd_mStop_250_mLSP_170to240","/SMS-T2-4bd_mStop-250_mLSP-170to240_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 21.5949     )
SMS_T2_4bd_mStop_275_mLSP_195to265      = kreator.makeMCComponent("SMS_T2_4bd_mStop_275_mLSP_195to265","/SMS-T2-4bd_mStop-275_mLSP-195to265_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 13.3231     )
SMS_T2_4bd_mStop_300_mLSP_220to290      = kreator.makeMCComponent("SMS_T2_4bd_mStop_300_mLSP_220to290","/SMS-T2-4bd_mStop-300_mLSP-220to290_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 8.51615     )
SMS_T2_4bd_mStop_325_mLSP_245to315      = kreator.makeMCComponent("SMS_T2_4bd_mStop_325_mLSP_245to315","/SMS-T2-4bd_mStop-325_mLSP-245to315_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 5.60471     )
SMS_T2_4bd_mStop_350_mLSP_270to340      = kreator.makeMCComponent("SMS_T2_4bd_mStop_350_mLSP_270to340","/SMS-T2-4bd_mStop-350_mLSP-270to340_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 3.78661     )
SMS_T2_4bd_mStop_375_mLSP_295to365      = kreator.makeMCComponent("SMS_T2_4bd_mStop_375_mLSP_295to365","/SMS-T2-4bd_mStop-375_mLSP-295to365_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 2.61162     )
SMS_T2_4bd_mStop_400_mLSP_320to390      = kreator.makeMCComponent("SMS_T2_4bd_mStop_400_mLSP_320to390","/SMS-T2-4bd_mStop-400_mLSP-320to390_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 1.83537     )
SMS_T2_4bd_mStop_425to475_mLSP_345to465 = kreator.makeMCComponent("SMS_T2_4bd_mStop_425to475_mLSP_345to465","/SMS-T2-4bd_mStop-425to475_mLSP-345to465_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root"     )
SMS_T2_4bd_mStop_500to550_mLSP_470to590 = kreator.makeMCComponent("SMS_T2_4bd_mStop_500to550_mLSP_470to590","/SMS-T2-4bd_mStop-500to550_mLSP-420to540_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root"     )  # mixed stops, no xsec
SMS_T2_4bd_mStop_550to600_mLSP_470to590 = kreator.makeMCComponent("SMS_T2_4bd_mStop_550to600_mLSP_470to590","/SMS-T2-4bd_mStop-550to600_mLSP-470to590_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root"     )  # mixed stops, no xsec
# 550: 0.296128    575: 0.226118       600: 0.174599













SMS_T2mixed_mStop_100_mLSP_20to90         =  kreator.makeMCComponent("SMS_T2mixed_mStop_100_mLSP_20to90","/SMS-T2mixed_mStop-100_mLSP-20to90_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root"     )
SMS_T2mixed_mStop_125_mLSP_45to115        =  kreator.makeMCComponent("SMS_T2mixed_mStop_125_mLSP_45to115","/SMS-T2mixed_mStop-125_mLSP-45to115_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root"     )
SMS_T2mixed_mStop_150_mLSP_70to140        =  kreator.makeMCComponent("SMS_T2mixed_mStop_150_mLSP_70to140","/SMS-T2mixed_mStop-150_mLSP-70to140_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root"     )
SMS_T2mixed_mStop_175_mLSP_95to165        =  kreator.makeMCComponent("SMS_T2mixed_mStop_175_mLSP_95to165","/SMS-T2mixed_mStop-175_mLSP-95to165_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root"     )
SMS_T2mixed_mStop_200_mLSP_120to190       =  kreator.makeMCComponent("SMS_T2mixed_mStop_200_mLSP_120to190","/SMS-T2mixed_mStop-200_mLSP-120to190_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root"     )
SMS_T2mixed_mStop_250_mLSP_170to240       =  kreator.makeMCComponent("SMS_T2mixed_mStop_250_mLSP_170to240","/SMS-T2mixed_mStop-250_mLSP-170to240_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root"     )
SMS_T2mixed_mStop_275_mLSP_195to265       =  kreator.makeMCComponent("SMS_T2mixed_mStop_275_mLSP_195to265","/SMS-T2mixed_mStop-275_mLSP-195to265_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root"     )
SMS_T2mixed_mStop_300_mLSP_220to290       =  kreator.makeMCComponent("SMS_T2mixed_mStop_300_mLSP_220to290","/SMS-T2mixed_mStop-300_mLSP-220to290_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root"     )
SMS_T2mixed_mStop_350_mLSP_270to340       =  kreator.makeMCComponent("SMS_T2mixed_mStop_350_mLSP_270to340","/SMS-T2mixed_mStop-350_mLSP-270to340_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root"     )
SMS_T2mixed_mStop_375_mLSP_295to365       =  kreator.makeMCComponent("SMS_T2mixed_mStop_375_mLSP_295to365","/SMS-T2mixed_mStop-375_mLSP-295to365_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root"     )
SMS_T2mixed_mStop_425to475_mLSP_345to465  =  kreator.makeMCComponent("SMS_T2mixed_mStop_425to475_mLSP_345to465","/SMS-T2mixed_mStop-425to475_mLSP-345to465_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root"     )
SMS_T2mixed_mStop_500to550_mLSP_420to540  =  kreator.makeMCComponent("SMS_T2mixed_mStop_500to550_mLSP_420to540","/SMS-T2mixed_mStop-500to550_mLSP-420to540_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root"     )






#SMS-T2mixed_mStop-100_mLSP-20to90         = kreator.makeMCComponent("/SMS-T2mixed_mStop-100_mLSP-20to90_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root",  1521.11     , useAAA=True)
#SMS-T2mixed_mStop-125_mLSP-45to115        = kreator.makeMCComponent("/SMS-T2mixed_mStop-125_mLSP-45to115_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root",  574.981    , useAAA=True)
#SMS-T2mixed_mStop-150_mLSP-70to140        = kreator.makeMCComponent("/SMS-T2mixed_mStop-150_mLSP-70to140_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root",  249.409    , useAAA=True)
#SMS-T2mixed_mStop-175_mLSP-95to165        = kreator.makeMCComponent("/SMS-T2mixed_mStop-175_mLSP-95to165_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root",  121.416    , useAAA=True)
#SMS-T2mixed_mStop-250_mLSP-170to240       = kreator.makeMCComponent("/SMS-T2mixed_mStop-250_mLSP-170to240_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root",  21.5949    , useAAA=True)
#SMS-T2mixed_mStop-275_mLSP-195to265       = kreator.makeMCComponent("/SMS-T2mixed_mStop-275_mLSP-195to265_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v2/MINIAODSIM", "CMS", ".*root",  13.3231    , useAAA=True)
#SMS-T2mixed_mStop-350_mLSP-270to340       = kreator.makeMCComponent("/SMS-T2mixed_mStop-350_mLSP-270to340_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v2/MINIAODSIM", "CMS", ".*root",  3.78661    , useAAA=True)
#SMS-T2mixed_mStop-375_mLSP-295to365       = kreator.makeMCComponent("/SMS-T2mixed_mStop-375_mLSP-295to365_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v2/MINIAODSIM", "CMS", ".*root",   2.61162   , useAAA=True)
#SMS-T2mixed_mStop-425to475_mLSP-345to465  = kreator.makeMCComponent("/SMS-T2mixed_mStop-425to475_mLSP-345to465_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v2/MINIAODSIM", "CMS", ".*root", 0     , useAAA=True)
#SMS-T2mixed_mStop-500to550_mLSP-420to540  = kreator.makeMCComponent("/SMS-T2mixed_mStop-500to550_mLSP-420to540_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v2/MINIAODSIM", "CMS", ".*root", 0     , useAAA=True)
#SMS-T2mixed_mStop-500to550_mLSP-420to540  = kreator.makeMCComponent("/SMS-T2mixed_mStop-500to550_mLSP-420to540_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root",  0    , useAAA=True)

#SMS_T2_4bd_mStop-200_mLSP_120to190      = kreator.makeMCComponent("/SMS-T2-4bd_mStop-200_mLSP-120to190_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v1/MINIAODSIM ", "CMS", ".*root",                            64.5085       , useAAA=True)
#SMS_T2_4bd_mStop-275_mLSP_195to265      = kreator.makeMCComponent("/SMS-T2-4bd_mStop-275_mLSP-195to265_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v1/MINIAODSIM ", "CMS", ".*root",  13.3231    , useAAA=True)
#SMS_T2_4bd_mStop-325_mLSP_245to315      = kreator.makeMCComponent("/SMS-T2-4bd_mStop-325_mLSP-245to315_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v1/MINIAODSIM ", "CMS", ".*root",  5.60471    , useAAA=True)
#SMS_T2_4bd_mStop-375_mLSP_295to365      = kreator.makeMCComponent("/SMS-T2-4bd_mStop-375_mLSP-295to365_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v1/MINIAODSIM ", "CMS", ".*root", 2.61162     , useAAA=True)
#SMS_T2_4bd_mStop-400_mLSP_320to390      = kreator.makeMCComponent("/SMS-T2-4bd_mStop-400_mLSP-320to390_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15FSPremix-MCRUN2_74_V9-v1/MINIAODSIM ", "CMS", ".*root",  1.83537    , useAAA=True)

    
SignalT2Deg4BodyScan= [ 
    SMS_T2_4bd_mStop_100_mLSP_20to90   ,SMS_T2_4bd_mStop_125_mLSP_45to115  ,SMS_T2_4bd_mStop_200_mLSP_120to190 ,
    SMS_T2_4bd_mStop_225_mLSP_145to225 ,SMS_T2_4bd_mStop_275_mLSP_195to265 ,SMS_T2_4bd_mStop_300_mLSP_220to290    , 
    SMS_T2_4bd_mStop_325_mLSP_245to315 ,SMS_T2_4bd_mStop_350_mLSP_270to340 ,SMS_T2_4bd_mStop_375_mLSP_295to365    , 
    SMS_T2_4bd_mStop_400_mLSP_320to390 ,SMS_T2_4bd_mStop_550to600_mLSP_470to590,
          ]


SignalT2DegMixedScan = [SMS_T2mixed_mStop_100_mLSP_20to90 ,SMS_T2mixed_mStop_125_mLSP_45to115 , SMS_T2mixed_mStop_175_mLSP_95to165 ,SMS_T2mixed_mStop_275_mLSP_195to265]

SignalT2DegFullScan = SignalT2Deg4BodyScan + SignalT2DegMixedScan
 
#SMS_T2bb_2J_mStop600_mLSP580 = kreator.makeMyPrivateMCComponent("SMS_T2bb_2J_mStop600_mLSP580", "/SMS-T2bb_2J_mStop-600_mLSP-580_Tune4C_13TeV-madgraph-tauola/namin-step3-fb89f44b0d6970d718ed21d513cd1c9d/USER", "PRIVATE", ".*root", "phys03", 0.174599, useAAA=True)
#SMS_T2bb_2J_mStop900_mLSP100 = kreator.makeMyPrivateMCComponent("SMS_T2bb_2J_mStop900_mLSP100", "/SMS-T2bb_2J_mStop-900_mLSP-100_Tune4C_13TeV-madgraph-tauola/namin-step3-fb89f44b0d6970d718ed21d513cd1c9d/USER", "PRIVATE", ".*root", "phys03", 0.0128895, useAAA=True)
#SMS_T2qq_2J_mStop1200_mLSP100 = kreator.makeMyPrivateMCComponent("SMS_T2qq_2J_mStop1200_mLSP100", "/SMS-T2qq_2J_mStop-1200_mLSP-100_Tune4C_13TeV-madgraph-tauola/namin-step3-fb89f44b0d6970d718ed21d513cd1c9d/USER", "PRIVATE", ".*root", "phys03", 0.0162846, useAAA=True)
#SMS_T2qq_2J_mStop600_mLSP550 = kreator.makeMyPrivateMCComponent("SMS_T2qq_2J_mStop600_mLSP550", "/SMS-T2qq_2J_mStop-600_mLSP-550_Tune4C_13TeV-madgraph-tauola/namin-step3-fb89f44b0d6970d718ed21d513cd1c9d/USER", "PRIVATE", ".*root", "phys03", 1.76645, useAAA=True)
#SMS_T2tt_2J_mStop425_mLSP325 = kreator.makeMyPrivateMCComponent("SMS_T2tt_2J_mStop425_mLSP325", "/SMS-T2tt_2J_mStop-425_mLSP-325_Tune4C_13TeV-madgraph-tauola/namin-step3-fb89f44b0d6970d718ed21d513cd1c9d/USER", "PRIVATE", ".*root", "phys03", 1.31169, useAAA=True)
#SMS_T2tt_2J_mStop500_mLSP325 = kreator.makeMyPrivateMCComponent("SMS_T2tt_2J_mStop500_mLSP325", "/SMS-T2tt_2J_mStop-500_mLSP-325_Tune4C_13TeV-madgraph-tauola/namin-step3-fb89f44b0d6970d718ed21d513cd1c9d/USER", "PRIVATE", ".*root", "phys03", 0.51848, useAAA=True)
#SMS_T2tt_2J_mStop650_mLSP325 = kreator.makeMyPrivateMCComponent("SMS_T2tt_2J_mStop650_mLSP325", "/SMS-T2tt_2J_mStop-650_mLSP-325_Tune4C_13TeV-madgraph-tauola/namin-step3-fb89f44b0d6970d718ed21d513cd1c9d/USER", "PRIVATE", ".*root", "phys03", 0.107045, useAAA=True)
#SMS_T2tt_2J_mStop850_mLSP100 = kreator.makeMyPrivateMCComponent("SMS_T2tt_2J_mStop850_mLSP100", "/SMS-T2tt_2J_mStop-850_mLSP-100_Tune4C_13TeV-madgraph-tauola/namin-step3-fb89f44b0d6970d718ed21d513cd1c9d/USER", "PRIVATE", ".*root", "phys03", 0.0189612, useAAA=True)
#
#SignalSUSYPrivate = [ SMS_T2bb_2J_mStop600_mLSP580, SMS_T2bb_2J_mStop900_mLSP100, SMS_T2qq_2J_mStop1200_mLSP100, SMS_T2qq_2J_mStop600_mLSP550, SMS_T2tt_2J_mStop425_mLSP325, SMS_T2tt_2J_mStop500_mLSP325, SMS_T2tt_2J_mStop650_mLSP325, SMS_T2tt_2J_mStop850_mLSP100 ] 


### ----------------------------- summary ----------------------------------------


signalSamples = SignalEXO + SignalSUSY + SignalSUSYFullScan #+ SignalSUSYPrivate

samples = signalSamples

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

#Define splitting
for comp in signalSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 250 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012

if __name__ == "__main__":
   import sys
   if "test" in sys.argv:
       from CMGTools.RootTools.samples.ComponentCreator import testSamples
       testSamples(samples)
