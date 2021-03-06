import foohid
import struct
import random
import time

joypad = (
    0x05, 0x01,
    0x09, 0x05,
    0xa1, 0x01,
    0xa1, 0x00,
    0x05, 0x09,
    0x19, 0x01,
    0x29, 0x10,
    0x15, 0x00,
    0x25, 0x01,
    0x95, 0x10,
    0x75, 0x01,
    0x81, 0x02,
    0x05, 0x01,
    0x09, 0x30,
    0x09, 0x31,
    0x09, 0x32,
    0x09, 0x33,
    0x15, 0x81,
    0x25, 0x7f,
    0x75, 0x08,
    0x95, 0x04,
    0x81, 0x02,
    0xc0,
    0xc0)

try:
    foohid.destroy("FooHID simple joypad")
except:
    pass
foohid.create("FooHID simple joypad", struct.pack('{0}B'.format(len(joypad)), *joypad))

while True:
    x = random.randrange(0,255)
    y = random.randrange(0,255)
    z = random.randrange(0,255)
    rx = random.randrange(0,255)
    foohid.send("FooHID simple joypad", struct.pack('H4B', 0, x, y, z, rx))
    time.sleep(1)
