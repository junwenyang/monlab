# coding=utf-8
import configparser
import os

class HostInfo:

    base_dir = os.path.abspath('.')  
    conf_path = os.path.join(base_dir, "conf\hosts.ini")
    conf = configparser.ConfigParser()
    conf.read(conf_path)

    def getHostMap(self):
        hostMap= {}
        options = {}
        try:
            for host in self.getHosts():
                for option in self.getOptions(host):
                    options[option] = self.getInfoByKey(host,option)
                hostMap[host] = options
        except Exception:
            print('配置项可能重复定义！请检查文件' + self.conf_path)
        else:
            return hostMap

    def getHosts(self):
        hosts = self.conf.sections()  
        return hosts

    def getOptions(self,host):
        options = self.conf.options(host)  
        return options

    def getItems(self,host):
        items = self.conf.items(host)  
        return items

    def getInfoByKey(self,host,key):
        val = self.conf.get(host,key)  
        return val

    # def setHostInfo(DESC, OS, TYPE, IP, PORT, USER, PASS):
    #     hostInfo = {'DESC':DESC,'OS':OS,'TYPE':TYPE,'IP':IP,'PORT':PORT,'USER':USER,'PASS':PASS}
    #     return hostInfo

    # # def run():
    # #     getHosts()

    # # if __name__ == "__main__":
    # #     run()

    ## configparser.DuplicateSectionError