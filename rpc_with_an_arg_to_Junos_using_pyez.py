from lxml import etree
from jnpr.junos import Device
dev=Device(host="192.168.56.151", user="root", password='Juniper')
dev.open()
result=dev.rpc.get_interface_information(level_extra="descriptions")
type(result)
print (etree.tostring(result))
etree.dump(result)
dev.close()