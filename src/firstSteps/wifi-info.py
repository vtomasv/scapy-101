from scapy.all import *


# Obtener la lista de interfaces de red disponibles
interfaces = get_if_list()

# Buscar la interfaz de red WiFi
wifi_iface = None
for iface in interfaces:
    if "wlan" in iface or "wifi" in iface or "en1" == iface:
        wifi_iface = iface
        break


# Mostrar el resultado
if wifi_iface:
    print("La interfaz de red WiFi es:", wifi_iface)
    # Obtener el nombre de la interfaz de red WiFi
    wifi_iface_hwaddr = get_if_hwaddr(wifi_iface)

    print("Local MAC / MAC", wifi_iface_hwaddr)

    # Obtener información de la interfaz de red WiFi
    wifi_iface_ip = get_if_addr(wifi_iface)

    # Mostrar el resultado
    print("IP de la interfaz WiFi:", wifi_iface_ip)
else:
    print("No se encontró ninguna interfaz de red WiFi.")

