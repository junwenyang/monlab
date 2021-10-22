# coding=utf-8
import socket
import paramiko
import time

def ssh_shell(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.read().decode('utf-8').rstrip().strip()

def get_host_status(hostInfo):
    ip = hostInfo['IP']
    port = hostInfo['PORT']
    user = hostInfo['USER']
    password = hostInfo['PASS']
    #print(ip+port+user+password)

    #创建SSH连接
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(ip, port, user, password, timeout=10)
    except paramiko.ssh_exception.AuthenticationException:
        print("login fail, check account!!")
        return
    except socket.timeout:
        print("Time out, check network!!")
        return

    # CPU使用
    cpu_raw = ssh_shell(ssh_client, "top -bn1|grep 'Cpu'| awk '{print $2}'")
    cpu = cpu_raw

    # 硬盘使用
    hard_disk_raw = ssh_shell(ssh_client, "df -h|awk '{print $4,$5}'|grep '%'")
    hard_disk_raw_list = hard_disk_raw.split('\n')
    hard_disk_raw_tem_list = hard_disk_raw_list[1].split(" ")
    if hard_disk_raw_tem_list[0].endswith("G"):
        hard_disk = hard_disk_raw_tem_list[1]
    else:
        hard_disk = hard_disk_raw_tem_list[0]

    # 内存使用
    free_cache_raw = ssh_shell(ssh_client, "free -m |grep 'Mem'|awk '{print $3}'")
    free_cache = int(int(free_cache_raw)/1024)

    #关闭连接，返回资源
    ssh_client.close()
    
    res = (cpu, hard_disk, free_cache)
    return res


# def run():
#     while 1:
#         print("hehe")
#         print(get_host_status({'IP':"10.1.1.1", 'PORT':"22", 'USER':"user", 'PASS':"pwd"}))
#         time.sleep(3)

# if __name__ == "__main__":
#     run()