# coding=utf-8
import configparser
import os

base_dir = os.path.abspath('.')  # 获取当前文件所在目录
#(base_dir)
conf_path = os.path.join(base_dir, "conf\hosts.ini")
#print(conf_path)
conf = configparser.ConfigParser()

conf.read(conf_path)  

def getHosts():
    hosts = conf.sections()  
    #print("hosts=")
    #print(hosts)
    return hosts

def getOptions(host):
    options = conf.options(host)  # 获取某个section名XX所对应的键
    #print("options=")
    #print(options)
    return options

def getItems(host):
    items = conf.items(host)  # 获取section名为所对应的全部键值对
    #print(items)
    return items

def getInfoByKey(host,key):
    val = conf.get(host,key)  # 获取[xx]中host对应的值
    #print(val)
    return val

def setHostInfo(DESC, OS, TYPE, IP, PORT, USER, PASS):
    hostInfo = {'DESC':DESC,'OS':OS,'TYPE':TYPE,'IP':IP,'PORT':PORT,'USER':USER,'PASS':PASS}
    return hostInfo

# def run():
#     getHosts()

# if __name__ == "__main__":
#     run()