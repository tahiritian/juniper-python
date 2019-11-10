import paramiko
import time

print ("Start : %s" % time.ctime())
time.sleep( 5 )
ip_address = "192.168.56.152"
port = "22"
username = "root"
password = "Juniper"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, port=22,username=username,password=password)
print ("Connected To Device", ip_address)
remote_connection = ssh_client.invoke_shell()
time.sleep(1.00)
remote_connection.send("cli\n")
remote_connection.send("show version |grep boot\n")
time.sleep(2)
print ("End : %s" % time.ctime())
remote_connection.send("exit")
time.sleep(1)
output = remote_connection.recv(65535)
print (output)
ssh_client.close
