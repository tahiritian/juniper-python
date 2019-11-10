from jnpr.junos import Device
from lxml import etree
dev=Device(host="192.168.56.151", user="root", password='Juniper')
dev.open()
test1=dev.rpc.ping(host="8.8.8.8")
print etree.tostring(test1)
test2=dev.rpc.traceroute(host="8.8.8.8")
print etree.tostring(test2)