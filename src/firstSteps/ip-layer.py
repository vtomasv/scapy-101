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

    dest_ip = "vtomasv.net"


    ip_layer = IP(src = src_ip, dst = dest_ip)
    icmp_req = ICMP(id=100)

    # Teardrop o fragmentacion
    load="FWHBBIT"*1300
    packet = ip_layer / icmp_req / load

    # «Destination Uunreachable» y  «Port Unreachable»
    icmp=ICMP(type=3,code=3)

    packet = ip_layer / icmp_req

    print("Envio")

    response = sr1(packet, iface=wifi_iface, timeout=2)

    print("Respuesta")
    

    if response:
        print(response.show())
else:
    print("No se encontró ninguna interfaz de red WiFi.")