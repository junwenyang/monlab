# coding=utf-8
import sys

from TongYong import hosts_conf as hc 
from TongYong import getLinuxInfo as gli
import time

hostList=hc.getHosts()

def ssh_shell(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.read().decode('utf-8').rstrip().strip()

def run():
    while 1:
        #获取服务器信息列表
        for host in hostList:
            print(host)
            print("Time : %s" % time.asctime(time.localtime(time.time())))
            ip=hc.getInfoByKey(host,"IP")
            port=hc.getInfoByKey(host,"PORT")
            user=hc.getInfoByKey(host,"USER")
            pwd=hc.getInfoByKey(host,"PASS")

            hostInfo=hc.setHostInfo("","","",ip,port,user,pwd)

            res = gli.get_host_status(hostInfo)
            print("res=")
            print(res)
        #server_config_list = server_config.config
        #for obj in server_config_list:
        #    check(obj)
        #print("等待下一个监视周期")
        
        #check_server(server_info_list)
        #status=get_host_status()
        #print(status)
        time.sleep(5)

if __name__ == "__main__":
    run()