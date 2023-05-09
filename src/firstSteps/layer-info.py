from scapy.all import *
    
dest_ip = "vtomasv.net"

ip_layer = IP(dst = dest_ip)
print(ls(ip_layer))  # Información completa de la capas

# Accedemos a los atributos
print("Destination  = ", ip_layer.dst)

print("Summary  = ",ip_layer.summary())

