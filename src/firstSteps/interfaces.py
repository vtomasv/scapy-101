from scapy.all import *

# Obtener la lista de interfaces de red disponibles
interfaces = get_if_list()

# Buscar la interfaz de red WiFi
wifi_iface = None
for iface in interfaces:
    print(iface)
    if "wlan" in iface or "wifi" in iface or "en0" in iface:
        wifi_iface = iface
        break

# Mostrar el resultado
if wifi_iface:
    print("La interfaz de red WiFi es:", wifi_iface)
else:
    print("No se encontró ninguna interfaz de red WiFi.")