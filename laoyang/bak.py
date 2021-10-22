# coding=utf-8
import socket
import server_config
import paramiko
import mysql
import time


def check_server(server_info_list):
    server_status_info = []
    for server in server_info_list:
        server_status_info.append(get_server_status(server))
    if len(server_status_info) > 0:
        for server in server_status_info:
            if server:
                print("%s��������CPU����%s%%\tӲ��ʹ��%s\t�����ڴ�%sG" % (server[0], server[1], server[2], server[3]))


def check_db(db_info_list):
    sync_key = None
    for db_info in db_info_list:
        host = db_info['host']
        user = db_info['user']
        passwd = db_info['passwd']
        db = db_info['db']
        port = db_info['port']
        ssh_info = db_info['ssh']
        if sync_key is None:
            command = "select id,userid,pageid from xxx order by createtime desc limit 500"
            sync_key = mysql.query(host=host, user=user, passwd=passwd, db=db, port=port, ssh_info=ssh_info,
                                   sql=command)
            if sync_key is None:
                print("���ݿ�����ʧ��")
                break
        else:
            index_id, user_id, page_id = sync_key[0]
            command = "select * from xxx where id=%s and userid=%s and pageid=%s" % (index_id, user_id, page_id)
            res = mysql.query(host=host, user=user, passwd=passwd, db=db, port=port, ssh_info=ssh_info, sql=command)
            if res:
                print("ͬ������")
            else:
                print("ͬ���쳣")


def check(server_info):
    server_name = server_info['server_name']
    server_info_list = [server_info['server_1'], server_info['server_2']]
    db_info_list = [server_info['db_1'], server_info['db_2']]
    print("\n���ڼ�顾%s��" % server_name)
    check_server(server_info_list)
    check_db(db_info_list)


def check_db_sync(db_obj_1, db_obj_2):
    res_list = db_obj_1.query("select id,userid,pageid from xxx order by createtime desc limit 500")
    if res_list:
        index_id, user_id, page_id = res_list[0]
        res = db_obj_2.query("select * from xxx where id=%s and userid=%s and pageid=%s"
                             % (index_id, user_id, page_id))
        if res:
            print("����ͬ��")
        else:
            print("ͬ���쳣")


def ssh_shell(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.read().decode('utf-8').rstrip().strip()


def get_server_status(server_info):
    name = server_info['name']
    ip = server_info['host']
    port = server_info['port']
    user = server_info['user']
    password = server_info['passwd']
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(ip, int(port), user, password, timeout=10)
    except paramiko.ssh_exception.AuthenticationException:
        print("��½ʧ�ܣ��˺��������")
        return
    except socket.timeout:
        print("���ӳ�ʱ�������Ƿ���Ҫʹ��VPN")
        return
    # CPU������
    cpu_raw = ssh_shell(ssh_client, "top -bn1|grep 'Cpu'| awk '{print $5}'")
    cpu = cpu_raw.split("%")[0]
    # Ӳ��ʹ��
    hard_disk_raw = ssh_shell(ssh_client, "df -h|awk '{print $4,$5}'|grep '%'")
    # ��ͬ������use%λ�ò�ͬ,��Ҫ�ֶ�����
    hard_disk_raw_list = hard_disk_raw.split('\n')
    hard_disk_raw_tem_list = hard_disk_raw_list[1].split(" ")
    if hard_disk_raw_tem_list[0].endswith("G"):
        hard_disk = hard_disk_raw_tem_list[1]
    else:
        hard_disk = hard_disk_raw_tem_list[0]
    # �����ڴ�
    free_cache_raw = ssh_shell(ssh_client, "free -m |grep 'buffers/cache'|awk '{print $4}'")
    free_cache = int(int(free_cache_raw)/1024)
    ssh_client.close()
    res = (name, cpu, hard_disk, free_cache,)
    return res


def run():
    while 1:
        # ��ȡ��������Ϣ�б�
        print("����ʱ�䣺%s" % time.asctime(time.localtime(time.time())))
        server_config_list = server_config.config
        for obj in server_config_list:
            check(obj)
        print("�ȴ���һ����������")
        time.sleep(60*60)


if __name__ == "__main__":
    run()