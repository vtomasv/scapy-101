from scapy.all import *

# Define la función de controlador de paquetes
def packet_handler(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet[Dot11Elt].info.decode()
        bssid = packet[Dot11].addr3
        channel = int(ord(packet[Dot11Elt:3].info))
        print("SSID: %s, BSSID: %s, Channel: %d" % (ssid, bssid, channel))

# Captura los paquetes de beacon y extrae la información de la red WiFi
sniff(iface="en0", prn=packet_handler)