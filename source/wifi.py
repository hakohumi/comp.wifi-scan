#! /usr/bin/env python


import os
import sys

from win_wifi
from linux_wifi


class WiFiUtil:
    # Wi-Fi関連ユーティリティ

    @staticmethod
    def linux_main():
        return


if __name__ == '__main__':
    print("start main")
    print("your os = ", os.name)
    if os.name == "nt":
        # win_main()
        print("Python {0:s} {1:d}bit on {2:s}\n".format(" ".join(item.strip(
        ) for item in sys.version.split("\n")), 64 if sys.maxsize > 0x100000000 else 32, sys.platform))
        WiFiUtil.main()
        print("\nDone.")

        win.main()

        # 現在のWiFiのSSIDを取得する
        # res = WiFiUtil.getUsingSSID()
        # print(res)

    else:
        linux_main()
