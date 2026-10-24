from sys import argv

asciis = ["0x"]

if len(argv) > 1:
    for c in argv[1]:
        asciis.append(hex(ord(c))[2:])
        asciis.append("00")

print("".join(asciis))

