import umsgpack
import sys

# s = b"\xf8\xe4\xfb\x2d\x49\x9d\x30\xd9\xd9\x0b\x9f\xaa\x08\x00\x45\x00" \
# b"\x00\x40\xaa\x1a\x00\x00\x40\x11\xc2\xe4\xc0\xa8\x01\x0d\xa9\x2c" \
# b"\xa2\xcc\xd4\x4d\x13\xc0\x00\x2c\xbb\xe1\xae\x3a\xcc\x01\x00\x00" \
# b"\x0e\x42\x40\x1e\x4f\x87\x43\x10\x4f\x36\x01\x00\x00\x04\x00\x00" \
# b"\x00\x14\x00\x00\x00\x00\x00\x00\x00\x50\x45\x9f\x5c\x86"

# s = "\xf8\xe4\xfb\x2d\x49\x9d\x30\xd9\xd9\x0b\x9f\xaa\x08\x00\x45\x00" \
# "\x00\x38\x6f\x3e\x00\x00\x40\x11\xfd\xc8\xc0\xa8\x01\x0d\xa9\x2c" \
# "\xa2\xcc\xd4\x4d\x13\xc0\x00\x24\xe7\xdd\xae\x3a\xcc\x01\x00\x00" \
# "\x12\x1a\x40\x1e\x4f\x87\x2f\xe2\xcf\x1b\x05\xff\x01\x04\x00\x00" \
# "\x00\x0c\x00\x00\x00\x03".encode("utf-8")

# s = "\x30\xd9\xd9\x0b\x9f\xaa\xf8\xe4\xfb\x2d\x49\x9d\x08\x00\x45\x00" \
# "\x02\x5c\x58\x8d\x00\x00\x75\x11\xdd\x55\xa9\x2c\xa2\xcc\xc0\xa8" \
# "\x01\x0d\x13\xc0\xd4\x4d\x02\x48\x96\x75\x00\x00\xcc\x01\x45\x9f" \
# "\x52\x06\x40\x1e\x4f\x87\xe5\xf8\x21\xdf\x08\x00\x01\x00\x00\x00" \
# "\x02\x30\x00\x00\x00\x3e\x00\x00\x00\x38\x00\x00\x00\x11\x00\x00" \
# "\x00\x06\x00\x00\x22\xf6\x00\x00\x0c\x60\x64\xd2\x06\x48\x5a\x54" \
# "\xa5\x6c\x65\x76\x65\x6c\x01\xa9\x61\x62\x69\x6c\x69\x74\x69\x65" \
# "\x73\x93\x82\xa2\x69\x64\xd2\x06\x8f\x3b\x37\xa5\x6c\x65\x76\x65" \
# "\x6c\x02\x82\xa2\x69\x64\xd2\x06\x8e\xc7\x34\xa5\x6c\x65\x76\x65" \
# "\x6c\x02\x82\xa2\x69\x64\xd2\x06\x90\x4c\x42\xa5\x6c\x65\x76\x65" \
# "\x6c\x00\xab\x65\x78\x41\x62\x69\x6c\x69\x74\x69\x65\x73\x91\x82" \
# "\xa2\x69\x64\xd2\x06\x05\x4a\x53\xa5\x6c\x65\x76\x65\x6c\x01\xaa" \
# "\x64\x72\x61\x67\x6f\x6e\x44\x61\x74\x61\xde\x00\x20\xa9\x6d\x61" \
# "\x78\x48\x70\x42\x61\x73\x65\xd1\x01\x2c\xaa\x61\x74\x74\x61\x63" \
# "\x6b\x42\x61\x73\x65\x62\xab\x64\x65\x66\x65\x6e\x73\x65\x42\x61" \
# "\x73\x65\x00\xaa\x61\x62\x69\x6c\x69\x74\x79\x4c\x76\x31\x02\xaa" \
# "\x61\x62\x69\x6c\x69\x74\x79\x4c\x76\x32\x00\xad\x66\x6f\x72\x74" \
# "\x4d\x61\x78\x48\x70\x50\x6c\x75\x73\x00\xae\x66\x6f\x72\x74\x41" \
# "\x74\x74\x61\x63\x6b\x50\x6c\x75\x73\x00\xaf\x66\x6f\x72\x74\x44" \
# "\x65\x66\x65\x6e\x73\x65\x50\x6c\x75\x73\x00\xb0\x72\x65\x6c\x69" \
# "\x61\x62\x69\x6c\x69\x74\x79\x4c\x65\x76\x65\x6c\x08\xac\x63\x68" \
# "\x61\x72\x61\x45\x6c\x65\x6d\x65\x6e\x74\x81\xa7\x76\x61\x6c\x75" \
# "\x65\x5f\x5f\x05\xa8\x67\x69\x66\x74\x54\x79\x70\x65\x81\xa7\x76" \
# "\x61\x6c\x75\x65\x5f\x5f\x07\xaa\x6f\x72\x69\x67\x69\x6e\x54\x79" \
# "\x70\x65\x81\xa7\x76\x61\x6c\x75\x65\x5f\x5f\x01\xa8\x6d\x61\x73" \
# "\x74\x65\x72\x49\x64\xd2\x01\x31\xcb\x37\xad\x6d\x61\x74\x63\x68" \
# "\x69\x6e\x67\x4b\x65\x79\x49\x64\xce\x00\x2d\xfa\xc1\xb0\x75\x73" \
# "\x65\x4d\x61\x74\x63\x68\x69\x6e\x67\x4b\x65\x79\x49\x64\xc3\xa5" \
# "\x6c\x65\x76\x65\x6c\x33\xa8\x6d\x61\x78\x4c\x65\x76\x65\x6c\x50" \
# "\xa3\x65\x78\x70\xd2\x00\x02\xb9\x44\xa5\x6d\x61\x78\x48\x70\xd1" \
# "\x01\x2c\xa6\x61\x74\x74\x61\x63\x6b\x62\xa7\x64\x65\x66\x65\x6e" \
# "\x73\x65\x00\xa7\x70\x6c\x75\x73\x56\x61\x6c\x00\xaf\x6c\x69\x6d" \
# "\x69\x74\x42\x72\x65\x61\x6b\x4c\x65\x76\x65\x6c\x04\xa8\x69\x73" \
# "\x4c\x6f\x63\x6b\x65\x64\xc2\xa6\x72\x61\x72\x69\x74\x79\x81\xa7" \
# "\x76\x61\x6c\x75\x65\x5f\x5f\x04\xab\x65\x6c\x65\x6d\x65\x6e\x74" \
# "\x54\x79\x70\x65\x81\xa7\x76\x61\x6c\x75\x65\x5f\x5f\x05\xaa\x77" \
# "\x65\x61\x70\x6f\x6e\x54\x79\x70\x65\x81\xa7\x76\x61\x6c\x75\x65" \
# "\x5f\x5f\x00\xa4\x6e\x61\x6d\x65\xa5\x53\x69\x6c\x6b\x65\xb3\x69" \
# "\x73\x56\x6f\x69\x63\x65\x4c\x6f\x61\x64".encode('utf-8')

s = "\xf8\xe4\xfb\x2d\x49\x9d\x30\xd9\xd9\x0b\x9f\xaa\x08\x00\x45\x00" \
"\x02\x5c\x25\x07\x00\x00\x40\x11\x45\xdc\xc0\xa8\x01\x0d\xa9\x2c" \
"\xa2\xcc\xd4\x4d\x13\xc0\x02\x48\xc4\xd1\xae\x3a\xcc\x01\x00\x00" \
"\x02\xdd\x40\x1e\x4f\x87\x85\x0d\xb2\x5c\x08\x00\x01\x04\x00\x00" \
"\x02\x30\x00\x00\x00\x06\x00\x00\x00\x04\x00\x00\x00\x12\x00\x00" \
"\x00\x02\x00\x00\x23\x3f\x00\x00\x04\x20\x06\x39\x18\x14\xa5\x6c" \
"\x65\x76\x65\x6c\x02\xa9\x61\x62\x69\x6c\x69\x74\x69\x65\x73\x93" \
"\x82\xa2\x69\x64\xd2\x06\x94\x1c\xd5\xa5\x6c\x65\x76\x65\x6c\x02" \
"\x82\xa2\x69\x64\xd2\x06\x8e\xc7\x36\xa5\x6c\x65\x76\x65\x6c\x02" \
"\x82\xa2\x69\x64\xd2\x06\x94\x6e\xdc\xa5\x6c\x65\x76\x65\x6c\x01" \
"\xab\x65\x78\x41\x62\x69\x6c\x69\x74\x69\x65\x73\x91\x82\xa2\x69" \
"\x64\xd2\x06\x05\x98\x73\xa5\x6c\x65\x76\x65\x6c\x01\xaa\x64\x72" \
"\x61\x67\x6f\x6e\x44\x61\x74\x61\xde\x00\x20\xa9\x6d\x61\x78\x48" \
"\x70\x42\x61\x73\x65\xd1\x01\x98\xaa\x61\x74\x74\x61\x63\x6b\x42" \
"\x61\x73\x65\xd1\x00\x84\xab\x64\x65\x66\x65\x6e\x73\x65\x42\x61" \
"\x73\x65\x00\xaa\x61\x62\x69\x6c\x69\x74\x79\x4c\x76\x31\x01\xaa" \
"\x61\x62\x69\x6c\x69\x74\x79\x4c\x76\x32\x00\xad\x66\x6f\x72\x74" \
"\x4d\x61\x78\x48\x70\x50\x6c\x75\x73\x00\xae\x66\x6f\x72\x74\x41" \
"\x74\x74\x61\x63\x6b\x50\x6c\x75\x73\x00\xaf\x66\x6f\x72\x74\x44" \
"\x65\x66\x65\x6e\x73\x65\x50\x6c\x75\x73\x00\xb0\x72\x65\x6c\x69" \
"\x61\x62\x69\x6c\x69\x74\x79\x4c\x65\x76\x65\x6c\x1e\xac\x63\x68" \
"\x61\x72\x61\x45\x6c\x65\x6d\x65\x6e\x74\x81\xa7\x76\x61\x6c\x75" \
"\x65\x5f\x5f\x05\xa8\x67\x69\x66\x74\x54\x79\x70\x65\x81\xa7\x76" \
"\x61\x6c\x75\x65\x5f\x5f\x07\xaa\x6f\x72\x69\x67\x69\x6e\x54\x79" \
"\x70\x65\x81\xa7\x76\x61\x6c\x75\x65\x5f\x5f\x01\xa8\x6d\x61\x73" \
"\x74\x65\x72\x49\x64\xd2\x01\x31\xf2\x4a\xad\x6d\x61\x74\x63\x68" \
"\x69\x6e\x67\x4b\x65\x79\x49\x64\xce\x00\x2e\x48\x71\xb0\x75\x73" \
"\x65\x4d\x61\x74\x63\x68\x69\x6e\x67\x4b\x65\x79\x49\x64\xc3\xa5" \
"\x6c\x65\x76\x65\x6c\x46\xa8\x6d\x61\x78\x4c\x65\x76\x65\x6c\x46" \
"\xa3\x65\x78\x70\xd2\x00\x06\x7d\x9a\xa5\x6d\x61\x78\x48\x70\xd1" \
"\x01\x98\xa6\x61\x74\x74\x61\x63\x6b\xd1\x00\x84\xa7\x64\x65\x66" \
"\x65\x6e\x73\x65\x00\xa7\x70\x6c\x75\x73\x56\x61\x6c\x00\xaf\x6c" \
"\x69\x6d\x69\x74\x42\x72\x65\x61\x6b\x4c\x65\x76\x65\x6c\x02\xa8" \
"\x69\x73\x4c\x6f\x63\x6b\x65\x64\xc2\xa6\x72\x61\x72\x69\x74\x79" \
"\x81\xa7\x76\x61\x6c\x75\x65\x5f\x5f\x05\xab\x65\x6c\x65\x6d\x65" \
"\x6e\x74\x54\x79\x70\x65\x81\xa7\x76\x61\x6c\x75\x65\x5f\x5f\x05" \
"\xaa\x77\x65\x61\x70\x6f\x6e\x54\x79\x70\x65\x81\xa7\x76\x61\x6c" \
"\x75\x65\x5f\x5f\x00\xa4\x6e\x61\x6d\x65\xaa\x4d\x61\x72\x69\x73" \
"\x68\x69\x74\x65\x6e\xb3\x69\x73\x56\x6f".encode('utf-8')

# usage: unpacker.py [truncated bytes]
# truncate n bytes from the end of the message?

s = bytearray(s)
if len(sys.argv) > 1:
    for i in range(int(sys.argv[1])):
        del s[len(s)-1]
ln = len(s)

for i in range(ln):
    del s[0]
    try:
        tmp = umsgpack.unpackb(s)
        if type(tmp) is dict:
            print(f"offset[{i+1}]: {tmp}")
    except:
        # print(f"offset[{i+1}]: ---crash!")
        pass