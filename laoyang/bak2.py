import paramiko


def ssh_client_con():
    """创建ssh连接，并执行shell指令"""
    # 1 创建ssh_client实例
    ssh_client = paramiko.SSHClient()
    # 自动处理第一次连接的yes或者no的问题
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    # 2 连接服务器
    ssh_client.connect(
        port=host_port,
        hostname=hostname,
        username=username,
        password=password
    )

    # 3 执行shell命令
    # 构造shell指令
    shell_command = """
    path='/tmp'
    tree ${path}
    # 如果tree命令执行失败，则安装tree后再执行
    if [ $? -ne 0 ]
    then
        yum install -y tree
        tree ${path}
    fi

    """
    # 执行shell指令
    stdin, stdout, stderr = ssh_client.exec_command(shell_command)
    # 输出返回信息
    stdout_info = stdout.read().decode('utf8')
    print(stdout_info)

    # 输出返回的错误信息
    stderr_info = stderr.read().decode('utf8')
    print(stderr_info)


def sftp_client_con():
    # 1 创建transport通道
    tran = paramiko.Transport((hostname, host_port))
    tran.connect(username=username, password=password)
    # 2 创建sftp实例
    sftp = paramiko.SFTPClient.from_transport(tran)

    # 3 执行上传功能
    local_path = "米汤.jpg"
    remote_path = "/home/333.jpg"
    put_info = sftp.put(local_path, remote_path, confirm=True)
    print(put_info)
    print(f"上传{local_path}完成")
    # 4 执行下载功能
    save_path = "7.jpg"
    sftp.get(remotepath=remote_path, localpath=save_path)
    print(f'下载{save_path}完成')

    # 5 关闭通道
    tran.close()


# 读取主机信息
try:
    with open('host_site.txt', 'r', encoding='utf8') as host_file:
        for host_info in host_file:
            line = host_info.strip('\n')
            hostname, host_port, username, password = line.split(',')
            print(f'---------------{hostname}执行结果-----------')
            ssh_client_con()   # 执行command并返回结果
            # 本例适合批量主机处理相同的command
except FileNotFoundError as e:
    print(e)