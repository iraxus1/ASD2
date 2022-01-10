def readTxt(filename):
    with open(filename, "r") as f:
        tekst = f.read()
        return tekst


def writeFileByte(filenamewrite):
    with open("tekstBit", "wb") as f:
        f.write(bitstring_to_bytes(filenamewrite))


def writeFileStr(filenamewritestr):
    with open("slownik", "a") as f:
        f.write((filenamewritestr))


def bitstring_to_bytes(s):
    b = bytearray()
    w = [int(s[i:i+8],2) for i in range(0, len(s), 8)]
    return(bytes(w))