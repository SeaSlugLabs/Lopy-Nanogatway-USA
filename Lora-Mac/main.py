from network import LoRa
import binascii
lora = LoRa(mode=LoRa.LORAWAN)
print("Lora MAC is: ")
print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))
