import paramiko
import time
import getpass


host = input("Enter NW device MGMT IP: ")
username = input("username: ")
password = getpass.getpass()
#host = "192.168.56.151"
#username = "root"
#password = "Juniper"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,username=username,password=password)
print ("Successful connection", host)
remote_connection = ssh_client.invoke_shell()
remote_connection.send("cli\n")
remote_connection.send("show ver\n")
remote_connection.send("show configuration |display set |match ge-0/0/0.0\n")
remote_connection.send("show interfaces terse |match inet\n")
time.sleep(3)
output = remote_connection.recv(65535)
print (output)
remote_connection.send("exit")
ssh_client.close
