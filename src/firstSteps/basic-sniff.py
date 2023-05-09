from scapy.all import *

# Obtener la lista de interfaces de red disponibles
interfaces = get_if_list()

# Buscar la interfaz de red WiFi
wifi_iface = None
for iface in interfaces:
    if "wlan" in iface or "wifi" in iface or "en0" == iface:
        wifi_iface = iface
        break


# Se manda el paquete de ping 
if wifi_iface:
    src_ip =  get_if_addr(wifi_iface)
    filename = "captura.pcap"

    def packet_handler(packet):
        print( packet.summary())
        wrpcap(filename, packet, append=True)

    sniff(count=30, iface=wifi_iface, prn=packet_handler)
    
    # Lee los paquetes desde el archivo PCAP
    packets = rdpcap(filename)

    print(packets)

else:
    print("No se encontró ninguna interfaz de red WiFi.")