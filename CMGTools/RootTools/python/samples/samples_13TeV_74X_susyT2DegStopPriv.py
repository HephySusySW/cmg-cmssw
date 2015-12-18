
import PhysicsTools.HeppyCore.framework.config as cfg
#xsec from: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom 
import subprocess

#basedir="root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/"
#basedir="root://xrootd.unl.edu//"
#basedir="root://cms-xrd-global.cern.ch/"

#import gfal2

def makePrivateMCComponentFromDPM(name,dataset,dpmdir,subdirs=[''],xSec=1):
    basedir="root://hephyse.oeaw.ac.at//cms/"
    #basedir="root://xrootd.unl.edu//"
    #basedir="root://cms-xrd-global.cern.ch/"
    #ctx = gfal2.create_context()
    #ctx.listdir(basedir+"/")
    dirs={  }
    allfiles=[]
    for subdir in subdirs:
        gfalout  = subprocess.Popen(["gfal-ls "+ basedir+"/"+dpmdir+'/'+subdir ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for f in gfalout.stdout.readlines():
            f = f[:-1]
            if not f.endswith("root"):
                continue
            allfiles.append( basedir+"/"+dpmdir+'/'+subdir+'/'+f )
    print "looked for files in :", basedir+"/"+dpmdir+'/'+subdir
    if len(allfiles) == 0:
       raise RuntimeError, "Trying to make a component %s with no files" % name
    print "Found: %s"%len(allfiles)
    component = cfg.MCComponent(
        dataset=dataset,
        name = name,
        files = allfiles, 
        xSection = xSec,
        nGenEvents = 1,
        triggers = [],
        effCorrFactor = 1,
    )
    return component

T2DegStop_300_270 = makePrivateMCComponentFromDPM(
                        name    = 'T2DegStop_300_270',                            
                        dataset =  "/T2DegStop_300_270_GEN-SIM/nrad-T2DegStop_300_270_MINIAODv2-RunIISpring15-MCRUN2_74_V9-25ns-4dc17ff0fe241c35c03aa547f2361414/USER" ,
                        dpmdir  =  "/store/user/nrad/T2DegStop_300_270_GEN-SIM/T2DegStop_300_270_MINIAODv2-RunIISpring15-MCRUN2_74_V9-25ns/4dc17ff0fe241c35c03aa547f2361414/"  ,
                        subdirs =[''],
                        xSec    = 8.51615 ,
                    )

T2DegStop_300_240_FastSim = makePrivateMCComponentFromDPM(
                        name    = 'T2DegStop_300_240_FastSim',                            
                        dataset = '/T2DegStop_300_240_FastSim_v3/nrad-T2DegStop_300_240FS-eb69b0448a13fda070ca35fd76ab4e24/USER'  ,
                        dpmdir  = '/store/user/nrad/T2DegStop_300_240_FastSim_v3/T2DegStop_300_240FS/151202_112132/0000/'  ,
                        xSec    = 8.51615,
                    )
T2DegStop_300_270_FastSim = makePrivateMCComponentFromDPM(
                        name    = 'T2DegStop_300_270_FastSim',                            
                        dataset = '/T2DegStop_300_270_FastSim_v3/nrad-T2DegStop_300_270FS-eb69b0448a13fda070ca35fd76ab4e24/USER'  ,
                        dpmdir  = '/store/user/nrad/T2DegStop_300_270_FastSim_v3/T2DegStop_300_270FS/151202_111759/0000/'  ,
                        xSec    = 8.51615,
                    )
T2DegStop_300_290_FastSim = makePrivateMCComponentFromDPM(
                        name    = 'T2DegStop_300_290_FastSim',                            
                        dataset = '/T2DegStop_300_290_FastSim_v3/nrad-T2DegStop_300_290FS-eb69b0448a13fda070ca35fd76ab4e24/USER'  ,
                        dpmdir  = '/store/user/nrad/T2DegStop_300_290_FastSim_v3/T2DegStop_300_290FS/151202_112032/0000/'   ,
                        xSec    = 8.51615,
                    )




