from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt, RadioTap

beacon = Dot11Beacon()

tim_bitmap = Dot11Elt(ID='TIM', info='\xff')


def handle_packet(pkt):
    if pkt.haslayer(Dot11Beacon):
        # Obtener los elementos del paquete
        timestamp = pkt[Dot11Beacon].timestamp
        ssid = pkt[Dot11Elt][Dot11Elt:3].info.decode('utf-8')
        tim = pkt[Dot11Elt:][Dot11Elt][ID == "TIM"]
        # Comprobar si el paquete es una respuesta TIM
        if tim and tim.info == b'\xff':
            print(f"TIM response received from {pkt.addr2} with SSID {ssid} and timestamp {timestamp}")


beacon.add_payload(tim_bitmap)

ssid = Dot11Elt(ID='SSID', info='CataConi')
freq = Dot11Elt(ID='DSset', info='\x03')
rates = Dot11Elt(ID='Rates', info='\x82\x84\x8b\x96\x0c\x12\x18\x24')

beacon.add_payload(ssid)
beacon.add_payload(freq)
beacon.add_payload(rates)

radiotap = RadioTap()


pkt = radiotap/beacon



sendp(pkt, iface='en1', inter=0.1, loop=1)

sniff(iface='en1', prn=handle_packet, timeout=10)
