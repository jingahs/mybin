import os
import sys
import urllib
import math
import struct
import requests

# Monster Hunter Stories 2
def tex2dds( file ):
    f		= open(file, 'rb')

    magic   = f.read(4)
    head0   = struct.unpack("L", f.read(4))[0]
    head1   = struct.unpack("L", f.read(4))[0]
    head2   = struct.unpack("L", f.read(4))[0]

    version = head0 >> 0 & 0xfff
    unk0    = head0 >> 12 & 0xfff
    null0   = head0 >> 24 & 0xf
    alpFlag = head0 >> 28 & 0xf

    mipMaps = head1 >> 0 & 0x3f
    width   = head1 >> 6 & 0x1ffff
    height  = head1 >> 19 & 0x1ffff

    unk1    = head2 >> 0 & 0xff
    ddsType = head2 >> 8 & 0xff
    unk2    = head2 >> 16 & 0xffff

    #print( version, unk0, null0, alpFlag, mipMaps, width, height, unk1, ddsType, unk2 )

    for i in range(mipMaps):
        f.read(8)

    flags	= 0
    flags	= flags | 0x1			# CAPS
    if height:
        flags	= flags | 0x2			# HEIGHT
    if width:
        flags	= flags | 0x4			# WIDTH
    flags	= flags | 0x1000		# PIXELFORMAT
    flags	= flags | 0x80000		# LINEARSIZE
    if mipMaps:
        flags	= flags | 0x20000       # MIPMAPCOUNT

    if ddsType == 7 or ddsType == 9:
        pitch = height * width * 4
    elif ddsType == 19 or ddsType == 20:
        pitch = int(height * width / 2)
    else:
        pitch = height * width

    if ddsType == 9: # R8G8B8A8
        ddsFormat = 28
    elif ddsType == 19: # BC1
        ddsFormat = 71
    elif ddsType == 20: # BC1_SRGB
        ddsFormat = 72
    elif ddsType == 21: # BC2
        ddsFormat = 74
    elif ddsType == 22: # BC2_SRGB
        ddsFormat = 75
    elif ddsType == 23: # BC3
        ddsFormat = 77
    elif ddsType == 24: # BC3_SRGB
        ddsFormat = 78
    elif ddsType == 25: # BC4
        ddsFormat = 80
    elif ddsType == 26 or ddsType == 31: # BC5
        ddsFormat = 83
    elif ddsType == 55: # BC7
        ddsFormat = 98
    elif ddsType == 56: # BC7_SRGB
        ddsFormat = 99
    else:
        print(">>", ddsType)
        ddsFormat = 0xffffffff

    #print(flags, pitch, ddsFormat)

    save = open(file[:-4]+".dds","wb")
    save.write( "DDS ".encode('UTF-8') )
    save.write( struct.pack("L", 124) )
    save.write( struct.pack("L", flags) )
    save.write( struct.pack("L", height) )
    save.write( struct.pack("L", width) )
    save.write( struct.pack("L", pitch) )
    save.write( struct.pack("L", 1) )
    save.write( struct.pack("L", mipMaps) )
    save.write( struct.pack("11L", 0,0,0,0,0,0,0,0,0,0,0) )

    save.write( struct.pack("L", 32) )
    save.write( struct.pack("L", 4) )
    save.write( "DX10".encode('UTF-8') )
    save.write( struct.pack("L", 0) )
    save.write( struct.pack("L", 0) )
    save.write( struct.pack("L", 0) )
    save.write( struct.pack("L", 0) )
    save.write( struct.pack("L", 0) )
    save.write( struct.pack("L", 0x401008) )
    save.write( struct.pack("L", 0) )
    save.write( struct.pack("L", 0) )
    save.write( struct.pack("L", 0) )
    save.write( struct.pack("L", 0) )

    save.write( struct.pack("L", ddsFormat) )
    save.write( struct.pack("L", 3) )
    save.write( struct.pack("L", 0) )
    save.write( struct.pack("L", 1) )
    save.write( struct.pack("L", 0) )
    save.write( f.read() )
    save.close

print(sys.argv)
for i in range(0, len(sys.argv)):
	tex2dds(sys.argv[i])