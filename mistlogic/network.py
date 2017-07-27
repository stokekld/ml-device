from .tools import *

class Ip(object):

    def __init__(self, iface):
        self.__iface = iface

    def flush(self):
        return commandExe('ip addr flush dev %s' % self.__iface)

    def set(self, ip, netmask, broadcast):
        return commandExe('ip addr add %s/%s brd %s dev %s' % (ip, netmask, broadcast, self.__iface))

class HostAp(object):

    def __init__(self, confFile):
        self.__confFile = confFile

    def start(self):
        return commandExe('hostapd -B %s' % self.__confFile)

    def stop(self):
        return killProcess('hostapd')

class Wpa(object):

    __confFile = '/etc/wpa_supplicant/wpa_supplicant.conf'

    def __init__(self, iface):
        self.__iface = iface

    def passphrase(self, ssid, passphrase):
        f = open(self.__confFile, 'w')
        f.write('network={{\n    ssid="{}"\n    psk="{}"\n}}\n'.format(ssid, passphrase))
        f.close() 

    def start(self):
        return commandExe('wpa_supplicant -B -i %s -Dwext -c %s' % (self.__iface, self.__confFile))

    def stop(self):
        return killProcess('wpa_supplicant')

class Dhcp(object):

    def __init__(self, iface):
        self.__iface = iface

    def startServer(self, confFile):
        return commandExe('dhcpd -cf %s %s' % ( confFile, self.__iface ))

    def stopServer(self):
        return killProcess('dhcpd')

    def startClient(self):
        return commandExe('dhclient %s' % self.__iface)

    def stopClient(self):
        return killProcess('dhclient')
