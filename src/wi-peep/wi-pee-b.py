from scapy.all import *

SSID = 'ANIBAL' 
iface = 'en0'   
sender = 'b4:20:46:2a:58:a5'

dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff',
addr2=sender, addr3=sender)
beacon = Dot11Beacon()
essid = Dot11Elt(ID='SSID',info=SSID, len=len(SSID))

frame = RadioTap()/dot11/beacon/essid

sendp(frame, iface=iface, inter=0.100, loop=1)