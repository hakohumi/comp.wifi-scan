#! /usr/bin/env python

# OSに合わせて、実行するpythonファイルを選択する

import os
import sys

from win_wifi_pkg import win_wifi as win
# from linux_wifi


class WiFiUtil:

    @staticmethod
    def win_main():
        return

    @staticmethod
    def linux_main():
        return

    def view_os():
        print("Python {0:s} {1:d}bit on {2:s}\n".format(" ".join(item.strip(
        ) for item in sys.version.split("\n")), 64 if sys.maxsize > 0x100000000 else 32, sys.platform))
        print("\nDone.")
        return


if __name__ == '__main__':
    print("start main")
    print("your os = ", os.name)
    if os.name == "nt":
        WiFiUtil.view_os()

    # win.main()

    # 現在のWiFiのSSIDを取得する
    # res = WiFiUtil.getUsingSSID()
    # print(res)

# else:
#     linux_main()
