from pythonwifi.iwlibs import Wireless

wifi = Wireless('eth1')
wifi.getEssid()
wifi.getMode()