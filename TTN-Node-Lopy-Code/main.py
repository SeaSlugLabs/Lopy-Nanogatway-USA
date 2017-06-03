from network import LoRa
import socket
import binascii
import struct
import time

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# create an ABP authentication params. Copy this from the TTN Device you created

dev_addr = struct.unpack(">l", binascii.unhexlify('XX XX XX XX'.replace(' ','')))[0]
nwk_swkey = binascii.unhexlify('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'.replace(' ',''))
app_swkey = binascii.unhexlify('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'.replace(' ',''))

for channel in range(0, 72):
    lora.remove_channel(channel)

# set the  channels  frequency
lora.add_channel(0, frequency=903900000, dr_min=0, dr_max=4)
# join a network using ABP (Activation By Personalization)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

# remove all the non-default channels
for i in range(1, 16):
    lora.remove_channel(i)


# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 3)# parameter changed from the original Code

# make the socket blocking
s.setblocking(False)

while True:
    #s.send(b'Hola LORAWAN')
    s.send(bytes([0xFF,0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]))#Send some sample Bytes
    print("packet send")
    time.sleep(4)
    time.sleep(4)
    time.sleep(4)
    time.sleep(4)
