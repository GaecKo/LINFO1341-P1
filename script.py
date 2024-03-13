import pyshark

# Live capture: captures all data 
cap = pyshark.LiveCapture(display_filter="ip.addr == 46.105.132.157")

cap.set_debug(True)

# will capture for 10 seconds
cap.sniff(timeout=10)

for packet in cap:
    print(packet)

cap.close()