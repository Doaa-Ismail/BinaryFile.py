import os
import binascii
import zlib
import sys


'''
def CRC32_from_file(filename):
    buf = open(filename,'r').read()
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    return "%08X" % buf
'''	


def crc(fileName):
    fd = open(fileName,"rb")
    content = fd.readlines()
    fd.close()
    for eachLine in content:
        zlib.crc32(eachLine)

for eachFile in sys.argv[1:]:
    crc(eachFile)

	
a = os.path.getsize("E:\AL Kolia\Embedded Linux\Python\\B2.bin")
print(a)
b = crc("B2.bin")
print(b)
f = open("B2.bin","a")
f.write("a\n")
f.write("f\n")
f.close()
print(crc("B2.bin"))

f = open("B2.bin","a")
f.write("invalid\n")
