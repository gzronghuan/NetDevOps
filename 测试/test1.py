#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import paramiko


def qytang_ssh(ip, username, password, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()                                          #创建实例
    ssh.load_system_host_keys()                                         #提取保存的公钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())           #如果没有密钥，加上一个
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


if __name__ == '__main__':
    print(qytang_ssh('192.168.142.133','root','170140Rh'))
#    print(qytang_ssh('172.16.1.102', 'root', 'Cisc0123',cmd='pwd'))