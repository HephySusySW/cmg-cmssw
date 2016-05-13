from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.transferLogs = True
config.General.requestName = 'heppy'
config.General.workArea = config.General.requestName

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'heppy_crab_fake_pset.py'
config.JobType.scriptExe = 'heppy_crab_script.sh'
# config.JobType.sendPythonFolder = True  #doesn't work, not supported yet? do it by hand
import os
os.system("tar czf python.tar.gz --dereference --directory $CMSSW_BASE python --exclude '*.root' --exclude '*.pdf'")
#os.system("tar czf cmgdataset.tar.gz --directory $HOME .cmgdataset")
#os.system("tar czf cafpython.tar.gz --directory /afs/cern.ch/cms/caf/ python")
#config.JobType.inputFiles = ['FrameworkJobReport.xml','heppy_config.py','heppy_crab_script.py','cmgdataset.tar.gz', 'python.tar.gz', 'cafpython.tar.gz']
config.JobType.inputFiles = ['FrameworkJobReport.xml','heppy_config.py','heppy_crab_script.py','python.tar.gz' ]
config.JobType.outputFiles = ['output.log.tgz'] # susySingleLepton.root is automatically send because of the pset file

config.section_("Data")
config.Data.ignoreLocality = False
#config.Data.inputDBS = 'global'
config.Data.inputDBS = os.environ["INPUT_DBS"]
config.Data.splitting = 'FileBased'

import subprocess
user = os.environ["USER"]
p = subprocess.Popen(["crab","checkusername"],stdout=subprocess.PIPE)
for l in p.stdout.readlines():
  if l.startswith("Username is: "):
    fields = l[:-1].split()
    if len(fields)==3:
      user = fields[-1]

config.Data.outLFNDirBase = '/store/user/' + user+'/cmgTuples/'
remoteDir = os.environ["CMG_REMOTE_DIR"]
if remoteDir!='':
  config.Data.outLFNDirBase+=remoteDir.rstrip('/')+'/'
config.Data.publication = False
#config.Data.primaryDataset = 'MyTest'
#config.Data.totalUnits = 5
#config.Data.unitsPerJob = 5
#config.Data.totalUnits = 2
config.Data.unitsPerJob = 1

config.section_("Site")#config.Site.blacklist = ['T2_US_Purdue', 'T2_BE_IIHE', 'T2_US_Wisconsin', 'T2_UK_SGrid_Bristol', 'T2_US_Nebraska', 'T2_US_UCSD', 'T2_US_Florida', 'T2_US_Caltech', 'T2_UK_London_IC', 'T2_KR_KNU', 'T2_IT_Legnaro', 'T2_US_UCSD']
config.Site.blacklist = ['T2_US_Purdue', 'T2_BE_IIHE', 'T2_US_Wisconsin', 'T2_UK_SGrid_Bristol', 'T2_US_Nebraska', 'T2_US_UCSD', 'T2_US_Florida', 'T2_US_Caltech', 'T2_UK_London_IC', 'T2_KR_KNU', 'T2_IT_Legnaro', 'T2_US_UCSD']
#config.Site.whitelist=  ['T2_DE_DESY', 'T2_FR_IPHC', 'T2_BE_UCL', 'T2_CH_CERN', 'T2_BR_SPRACE', 'T2_FR_IPHC', 'T2_CH_CSCS', 'T2_FR_GRIF_LLR', 'T2_AT_Vienna' ]
#config.Site.whitelist=  ['T2_DE_DESY', 'T2_FR_IPHC', 'T2_BE_UCL', 'T2_CH_CERN', 'T2_BR_SPRACE', 'T2_FR_IPHC', 'T2_CH_CSCS', 'T2_FR_GRIF_LLR' ]
#config.Site.whitelist=  ['T2_AT_Vienna' , 'T2_CH_CERN' ]
config.Site.storageSite = 'T2_AT_Vienna'
#config.Data.ignoreLocality = True

