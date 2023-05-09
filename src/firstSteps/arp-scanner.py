from scapy.all import *


# Obtener la lista de interfaces de red disponibles
interfaces = get_if_list()

# Buscar la interfaz de red WiFi
wifi_iface = None
for iface in interfaces:
    if "wlan" in iface or "wifi" in iface or "en1" == iface:
        wifi_iface = iface
        break


# Se manda el paquete de ping 
if wifi_iface:
    src_ip =  get_if_addr(wifi_iface)

    broadcast = "FF:FF:FF:FF:FF:FF"
    ether_layer = Ether(dst = broadcast)
    ip_range = "192.168.4.1/24"
    arp_layer = ARP(pdst = ip_range)

    packet = ether_layer / arp_layer

    ans, unans = srp(packet, iface = wifi_iface, timeout=10)

    for snd, rcv in ans:
        ip = rcv[ARP].psrc
        mac = rcv[Ether].src
        print("IP = ", ip, " MAC = ", mac)
else:
    print("No se encontró ninguna interfaz de red WiFi.")

