from mistlogic.config import *
from mistlogic.network import *

network = Config('network', {
    'ip': "192.168.1.1",
    'netmask': "255.255.255.0",
    'ap': True,
    'dhcp': True,
    'ssid': "",
    'passphrase': ""
})

hostap = HostAp('/etc/mistlogic/hostapd.conf')
wpa = Wpa('wlan0')
dhcp = Dhcp('wlan0')
ip = Ip('wlan0')

hostap.stop()
wpa.stop()
dhcp.stopServer()
dhcp.stopClient()

ip.flush()

network.setProp('ap', False)
network.setProp('ssid', "COORD")
network.setProp('passphrase', "$i$2016admin")

if network.getProp('ap'):
    ip.set("192.168.1.1", "24", "192.168.1.255")
    hostap.start()
    dhcp.startServer('/etc/mistlogic/dhcpd.conf')
else:
    wpa.passphrase(network.getProp('ssid'), network.getProp('passphrase'))
    wpa.start()
    if network.getProp('dhcp'):
        dhcp.startClient()
