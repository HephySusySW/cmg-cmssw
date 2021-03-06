from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
import PhysicsTools.HeppyCore.framework.config as cfg
from DataFormats.FWLite import Handle,Lumis
from ROOT.gen import WeightsInfo

class LHEWeightAnalyzer( Analyzer ):
    """Read the WeightsInfo objects of the LHE branch and store them
       in event.LHE_weights list.

       If the WeightsInfo.id is a string, replace it with an integer.

       So far the only allowed string format is "mg_reweight_X",
       which gets stored as str(10000+int(X))

       If w.id is an unknown string or anything but a string or int,
       a RuntimeError is raised.
    """
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(LHEWeightAnalyzer,self).__init__(cfg_ana,cfg_comp,looperName)

        self.LHEWeightsNames=[]

    def declareHandles(self):
        super(LHEWeightAnalyzer, self).declareHandles()
        self.mchandles['LHEweights'] = AutoHandle('externalLHEProducer',
                                                  'LHEEventProduct',
                                                  mayFail=True,
                                                  fallbackLabel='source',
                                                  lazy=False )
        if self.cfg_ana.useLumiInfo or self.cfg_ana.usePSweights:
            self.mchandles['GenInfos'] = AutoHandle('generator',
                                                    'GenEventInfoProduct',
                                                    mayFail=True,
                                                    fallbackLabel='source',
                                                    lazy=False )
            self.genLumiHandle = Handle("GenLumiInfoHeader")
        
    def beginLoop(self, setup):
        super(LHEWeightAnalyzer,self).beginLoop(setup)
        
        if self.cfg_ana.useLumiInfo or self.cfg_ana.usePSweights:
            lumis = Lumis(self.cfg_comp.files)
            for lumi in lumis:
                if lumi.getByLabel('generator',self.genLumiHandle):
                    weightNames = self.genLumiHandle.product().weightNames()
                    for wn in weightNames:  #direct cast is not working properly, copy of elements is needed
                        self.LHEWeightsNames.append(wn)
                    break

    def process(self, event):
        self.readCollections( event.input )
        
        # if not MC, nothing to do
        if not self.cfg_comp.isMC:
            return True

        # Add LHE weight info
        event.LHE_weights = []
        event.LHE_originalWeight = 1.0
        
        if self.mchandles['LHEweights'].isValid() and not self.cfg_ana.useLumiInfo:
            event.LHE_originalWeight = self.mchandles['LHEweights'].product().originalXWGTUP()

            for w in self.mchandles['LHEweights'].product().weights():
                # Check if id is string or int and convert to int if it's a string
                try:
                    int(w.id)
                    event.LHE_weights.append(w)
                except ValueError:
                    if not type(w.id) == str:
                        raise RuntimeError('Non int or string type for LHE weight id')

                    newweight = WeightsInfo()
                    newweight.wgt = w.wgt
                    if w.id.startswith('mg_reweight'):
                        newid = str(10000 + int(w.id.rsplit('_',1)[1]))
                        newweight.id = newid

                    elif w.id.startswith('rwgt'):
                        newid = str(20000 + int(w.id.rsplit('_',1)[1])) 
                        newweight.id = newid
                    else:
                        #print w.id, newweight.wgt
                        raise RuntimeError('Unknown string id in LHE weights: %r' % w.id)
                    event.LHE_weights.append(newweight)


        if self.cfg_ana.useLumiInfo and self.mchandles['GenInfos'].isValid() :          
            for cnt,w in enumerate(self.mchandles['GenInfos'].product().weights()[1:10]):
                weight= WeightsInfo()
                weight.wgt=w
                idstr=self.LHEWeightsNames[cnt+1].split(',')[1]
                weight.id=str(10000 + int(idstr[6:]) )
                event.LHE_weights.append(weight)
        
        if self.cfg_ana.usePSweights and self.mchandles['GenInfos'].isValid():
            for cnt,w in enumerate(self.mchandles['GenInfos'].product().weights()[:14]):
                weight= WeightsInfo()
                weight.wgt=w
                # appending the PS weights to the LHE weights vector.
                # 0,1 correspond to central ME weight value and replica
                # The remaining 12 values (weightIDs = 2 to 13) correspond to the PS weights in the following order (ISR up, FSR up, ISR down, FSR down) x 3 sets
                # 2 = isrRedHi isr:muRfac=0.707, 3 = fsrRedHi fsr:muRfac=0.707, 4 = isrRedLo isr:muRfac=1.414, 5 = fsrRedLo fsr:muRfac=1.414
                # 6 = isrDefHi isr:muRfac=0.5, 7 = fsrDefHi fsr:muRfac=0.5,  8 = isrDefLo isr:muRfac=2.0,   9 = fsrDefLo fsr:muRfac=2.0
                # 10 = isrConHi isr:muRfac=0.25, 11 = fsrConHi fsr:muRfac=0.25, 12 = isrConLo isr:muRfac=4.0, 13 = fsrConLo fsr:muRfac=4.0
                weight.id=str(20000 + cnt )
                event.LHE_weights.append(weight)
                
        return True

setattr(LHEWeightAnalyzer,"defaultConfig",
    cfg.Analyzer(LHEWeightAnalyzer,
                 useLumiInfo = False,
                 usePSweights = False
    )
)
