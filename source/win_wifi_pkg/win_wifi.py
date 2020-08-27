import sys
from win32wifi import Win32Wifi as ww
# from win32wifi.Win32Wifi import *


class win_WiFi_class:
    # Wi-Fi関連ユーティリティ

    @staticmethod
    def main():
        interfaces = ww.getWirelessInterfaces()
        print("WLAN Interfaces: {:d}".format(len(interfaces)))

        handle = ww.WlanOpenHandle()
        for idx, interface in enumerate(interfaces):
            print("\n  {:d}\n  GUID: [{:s}]\n  Description:  [{:s}]\n  State: [{:s}]".format(
                idx, interface.guid_string, interface.description, interface.state_string))

            try:
                scan_result = ww.WlanScan(handle, interface.guid)

            except BaseException:
                print(sys.exc_info())
                continue

            print("\n  Scan result: {:d}".format(scan_result))

            print("scan end")

            try:
                networks = ww.getWirelessAvailableNetworkList(interface)

            except BaseException:
                print(sys.exc_info())
                continue

            print("\n  Networks: {:d}".format(len(networks)))

            for idx1, network in enumerate(networks):
                print("\n    {:d}\n    SSID: [{:s}]\n    Profile: [{:}]\n    Connectable: {:}\n    Signal quality: {:d}\n    Flags: {:d}\n    Security: {:}\n    Auth: {:}".format(
                    idx1, network.ssid.decode(), network.profile_name, network.connectable, network.signal_quality, network.flags, network.security_enabled, network.auth))

        ww.WlanCloseHandle(handle)

    def WifiScan():
        try:
            scan_result = ww.WlanScan(handle, interface.guid)

        except BaseException:
            print(sys.exc_info())

        print("\n  Scan result: {:d}".format(scan_result))

        print("scan end")
