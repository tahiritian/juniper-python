from jnpr.junos.utils.start_shell import StartShell
from jnpr.junos import Device
dev=Device('192.168.56.151', user='root', passwd='Juniper')
ss = StartShell(dev)
ss.open()
ss.run('pwd')
ss.run('cli -c "show version"')
ss.run('cli -c "show configuration | save localfile.txt"')
ss.close()
