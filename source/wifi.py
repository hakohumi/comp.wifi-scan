#! /usr/bin/env python

import subprocess
import os
import sys
import re

from win32wifi import Win32Wifi as ww


class WiFiUtil:
    # Wi-Fi関連ユーティリティ

    @staticmethod
    def win_main():
        print("win_main() start")

        cmd = 'netsh wlan show networks mode=Bssid'

        # os.system("dir")
        try:
            res = subprocess.run(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        except:
            print("subprocess.check_output() failed")

        print(res.stdout.decode('shift-jis'))

        return

    @staticmethod
    def linux_main():
        return

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

            except:
                print(sys.exc_info())
                continue

            print("\n  Scan result: {:d}".format(scan_result))

    #   fafafa
            print("scan end")

            try:
                networks = ww.getWirelessAvailableNetworkList(interface)

            except:
                print(sys.exc_info())
                continue

            print("\n  Networks: {:d}".format(len(networks)))

            for idx1, network in enumerate(networks):
                print("\n    {:d}\n    SSID: [{:s}]\n    Profile: [{:}]\n    Connectable: {:}\n    Signal quality: {:d}\n    Flags: {:d}\n    Security: {:}\n    Auth: {:}".format(
                    idx1, network.ssid.decode(), network.profile_name, network.connectable, network.signal_quality, network.flags, network.security_enabled, network.auth))

        ww.WlanCloseHandle(handle)

    @staticmethod
    def getUsingSSID():
        # 現在接続中のWi-FiのSSIDを取得する
        # returns:
        #   str -- SSID

        # wifiの状況を確認するコマンドを実行する
        cmd = ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I']
        cmd_res = subprocess.run(cmd, stdout=subprocess.PIPE)

        # コマンドの実行結果をoutputに保存する
        output = cmd_res.stdout.decode('utf-8')

        # 文字列から、SSIDと書かれた部分を取得する
        matchs = re.findall(r' +SSID: .+', output)
        res = ""

        if len(matchs) > 0:
            res = matchs[0]
            res = re.sub(r'^ +SSID: ', '', res)
            res = res.rstrip()
        return res


if __name__ == '__main__':
    print("start main")
    print("your os = ", os.name)
    if os.name == "nt":
        # win_main()
        print("Python {0:s} {1:d}bit on {2:s}\n".format(" ".join(item.strip(
        ) for item in sys.version.split("\n")), 64 if sys.maxsize > 0x100000000 else 32, sys.platform))
        WiFiUtil.main()
        print("\nDone.")

        win_main()

        # 現在のWiFiのSSIDを取得する
        # res = WiFiUtil.getUsingSSID()
        # print(res)

    else:
        linux_main()
