# coding=utf-8
import socket
import paramiko

class connector:
    def __init__(self,hostInfo):
        self.ip = hostInfo['ip']
        self.port = hostInfo['port']
        self.user = hostInfo['user']
        self.password = hostInfo['pass']
        #self.type = hostInfo['type']
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sshConnect()
        #print(ip+port+user+password)
    
    def sshConnect(self):
        #创建SSH连接
        try:
            self.ssh_client.connect(self.ip, self.port, self.user, self.password, timeout=10)
        except paramiko.ssh_exception.AuthenticationException:
            print("login fail, check account!!")
            return
        except socket.timeout:
            print("Time out, check network!!")
            return

    def doShell(self, command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        return stdout.read().decode('utf-8').rstrip().strip()
        

    def sshClose(self):
        self.ssh_client.close()