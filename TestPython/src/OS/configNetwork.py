"""
@author: zhi chen
@requires: PyWin32 Module, Python WMI Module
WMI is Microsoft's implementation of Web-Based Enterprise Management,
provide pretty much information about a computer system.
Python WMI module is a lightweight wrapper for PyWin32 module,
it hides some messy plumbing needed to get Python to talk to the WMI API.

To know more about Python WMI module, you can see this page
http://timgolden.me.uk/python/wmi/index.html

A useful link about WMI Win32_NetworkAdapterConfiguration class
http://msdn.microsoft.com/en-us/library/aa394217%28v=vs.85%29.aspx
"""

import wmi
# Obtain network adaptors configurations
nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

ip = u'10.214.25.190'
subnetmask = u'255.255.255.0'
gateway = u'10.214.25.1'
dnsserver = u'10.10.0.21'

# Find  network adaptor
nic = None
for nic in nic_configs:
    if 'Wireless-N 2200' in nic.caption:
        break

print nic

# Set IP address, subnetmask and default gateway
# Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
nic.SetGateways(DefaultIPGateway=[gateway])
nic.SetDNSServerSearchOrder(DNSServerSearchOrder=[dnsserver])

print 'config finished.'
print nic