ciphertexts = [["4af532671351e2e1","87a40cfa8dd39154"],["7b50baab07640c3d","ac343a22cea46d60"],["290b6e3a39155d6f","d6f491c5b645c008"],["2d1cfa42c0b1d266","eea6e3ddb2146dd0"]]
strings = ['The most direct computation would be for the enemy to try all 2^r possible keys, one by one.',
'The significance of this general conjecture, assuming its truth, is easy to see. It means that it may be feasible to design ciphers that are effectively unbreakable.',
'An enciphering-deciphering machine (in general outline) of my invention has been sent to your organization.',
'To consider the resistance of an enciphering process to being broken we should assume that at same times the enemy knows everything but the key being used and to break it needs only discover the key from this information.']

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

    
def main():
    for ctpair in ciphertexts:
        xortext = strxor(ctpair[0].decode('hex'),ctpair[1].decode('hex'));
        print xortext.encode('hex');

    for s in strings:
        print len(s);
    

