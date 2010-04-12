from  xml.dom.minidom import parse,parseString,getDOMImplementation,Node
        
class frontierconfigParser(object):
    def __init__(self):
        self.__configstr=''
        self.__configfile=''
        ###parse result
        self.__parameterDict={}
    def handleFrontierConnect(self,dom):
        #print 'handleFrontierConnect'
        nodelist=dom.getElementsByTagName('frontier-connect')[0].childNodes
        #print nodelist
        for node in nodelist:
            if node.nodeType!=Node.TEXT_NODE:
                tagname=node.tagName
                attrs=node.attributes
                for attrName in attrs.keys():
                    attrNode=attrs.get(attrName)
                    attrValue=attrNode.nodeValue
                    if  self.__parameterDict.has_key(tagname):
                        self.__parameterDict[tagname].append((attrName,attrValue))
                    else:
                        valuelist=[]
                        valuelist.append((attrName,attrValue))
                        self.__parameterDict[tagname]=valuelist
    def parse(self,filename):
        """
        Parse an XML file by name
        """
        dom=parse(filename)
        self.handleFrontierConnect(dom)
        dom.unlink()
    def parseString(self,strbuff):
        dom=parseString(strbuff)
        self.handleFrontierConnect(dom)
        dom.unlink()
    def proxylist(self):
        return self.__parameterDict['proxy']
    def serverlist(self):
        return self.__parameterDict['server']
    def parameterdict(self):
        return self.__parameterDict
if __name__ == '__main__':
    mydocstr="""<frontier-connect><proxy url="http://cmst0frontier.cern.ch:3128"/><proxy url="http://cmst0frontier.cern.ch:3128"/><proxy url="http://cmst0frontier1.cern.ch:3128"/><proxy url="http://cmst0frontier2.cern.ch:3128"/><server url="http://cmsfrontier.cern.ch:8000/FrontierInt"/><server url="http://cmsfrontier.cern.ch:8000/FrontierInt"/><server url="http://cmsfrontier1.cern.ch:8000/FrontierInt"/><server url="http://cmsfrontier2.cern.ch:8000/FrontierInt"/><server url="http://cmsfrontier3.cern.ch:8000/FrontierInt"/><server url="http://cmsfrontier4.cern.ch:8000/FrontierInt"/></frontier-connect>"""
    p=frontierconfigParser()
    p.parseString(mydocstr)
    print 'proxies'
    print p.proxylist()
    print 'servers'
    print p.serverlist()
    print 'parameterdict'
    print p.parameterdict()

    p.parse('/afs/cern.ch/user/x/xiezhen/w1/lumical/CMSSW_3_5_0_pre5/src/RecoLuminosity/LumiDB/site-local-config.xml')
    print 'proxies'
    print p.proxylist()
    print 'servers'
    print p.serverlist()
    print 'parameterdict'
    print p.parameterdict()
