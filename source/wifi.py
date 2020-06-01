#! /usr/bin/env python

import subprocess
import os
import sys

from win32wifi import Win32Wifi as ww


def win_main():
    print("win_main() start")

    cmd = 'netsh wlan show'

    # os.system("dir")
    try:
        res = subprocess.run(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    except:
        print("subprocess.check_output() failed")

    print(res.stdout.decode('shift-jis'))

    return


def linux_main():
    return


def main():
    interfaces = ww.getWirelessInterfaces()
    print("WLAN Interfaces: {:d}".format(len(interfaces)))
    handle = ww.WlanOpenHandle()
    for idx, interface in enumerate(interfaces):
        print("\n  {:d}\n  GUID: [{:s}]\n  Description: [{:s}]".format(
            idx, interface.guid_string, interface.description))
        try:
            scan_result = ww.WlanScan(handle, interface.guid)
        except:
            print(sys.exc_info())
            continue
        print("\n  Scan result: {:d}".format(scan_result))
    ww.WlanCloseHandle(handle)


def smain():
    interfaces = ww.getWirelessInterfaces()
    print("WLAN Interfaces: {:d}".format(len(interfaces)))
    for idx0, interface in enumerate(interfaces):
        print("\n  {:d}\n  GUID: [{:s}]\n  Description:  [{:s}]\n  State: [{:s}]".format(
            idx0, interface.guid_string, interface.description, interface.state_string))
        try:
            networks = ww.getWirelessAvailableNetworkList(interface)
        except:
            print(sys.exc_info())
            continue

        print("\n  Networks: {:d}".format(len(networks)))

        for idx1, network in enumerate(networks):
            print("\n    {:d}\n    SSID: [{:s}]\n    Profile: [{:}]\n    Connectable: {:}\n    Signal quality: {:d}\n    Flags: {:d}\n    Security: {:}\n    Auth: {:}".format(
                idx1, network.ssid.decode(), network.profile_name, network.connectable, network.signal_quality, network.flags, network.security_enabled, network.auth))


if __name__ == '__main__':
    print("start main")
    print("your os = ", os.name)
    if os.name == "nt":
        # win_main()
        print("Python {0:s} {1:d}bit on {2:s}\n".format(" ".join(item.strip(
        ) for item in sys.version.split("\n")), 64 if sys.maxsize > 0x100000000 else 32, sys.platform))
        main()
        print("\nDone.")

        print("Python {0:s} {1:d}bit on {2:s}\n".format(" ".join(item.strip(
        ) for item in sys.version.split("\n")), 64 if sys.maxsize > 0x100000000 else 32, sys.platform))
        smain(*sys.argv[1:])
        print("\nDone.")

    else:
        linux_main()
