
ciphertext_1 = "00010101 00010100 00010011 00000000 00011101 00000011 00001010 00000010 00011100 00000011 00010101 00011001 00010111 00000001 00010001 00001001 00011111 00010010 00000100 00000000 00001001 00000111 00011010 00000000 00000001 00001110 00000000 00010101 00001011 00011111 00010000 00011000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000".split()
ciphertext_2 = "00010110 00001100 00000110 00000111 00001000 00000101 00001101 00001011 00000011 00011000 00011110 00001110 00010110 00001001 00010111 00001101 00011100 00010101 00001111 00010101 00010010 00010111 00011010 00001010 00011110 00000100 00000110 00000111 00001010 00000000 00010000 00000100 00011000 00011001 00000110 00001011 00000010 00001001 00000010 00001000 00011111 00001010 00011100 00010011 00000000 00011101".split()

uncomplete_1 = "p s t k r o e l l p a r e n t e s - - - - - - - - - - - - - - - k r o e l l p a r e n t e s".split(" ")
#uncomplete_1 = "- - - k r o e l l - - - - - - - - - - - - - - - - - - - - - - - k r o e l l - - - - - - - -".split(" ")
uncomplete_2 = "- - - - - - - - - - - - - - - - p e n g w y n o m a t s o l e n - - - - - - - - - - - - - -".split(" ")
#uncomplete_2 = "- - - - - - - - - - - - - - - - p e n g w y n - - a - - o l - n - - - - - - - - - - - - - -".split(" ")

def xor(a,b):
    return a ^ b

def fill_pad(pad, cipher, message):
    for i in range(len(cipher)):
        if message[i] != '-':
            c = int(cipher[i], 2)
            m = ord(message[i])
            pad[i] = xor(c,m)
    return pad

def decode(pad, cipher):
    message = []
    for i in range(len(cipher)):
        if pad[i] == '?':
            message.append('?')
        else:
            number = xor(pad[i], int(cipher[i], 2))
            letter = chr(number)
            message.append(letter)
    return message

pad = ['?'] * len(ciphertext_1)
pad = fill_pad(pad, ciphertext_1, uncomplete_1)
pad = fill_pad(pad, ciphertext_2, uncomplete_2)

pad_egg = ''
for n in pad:
    if n=='?':
        pad_egg+='?'
    else:
        pad_egg+=chr(n)

print('One time pad: '+pad_egg)

test = [];
for i in range(len(ciphertext_1)):
    c1 = int(ciphertext_1[i], 2)
    c2 = int(ciphertext_2[i], 2)
    test.append(xor(c1, c2))

decoded1 = decode(pad, ciphertext_1)
decoded2 = decode(pad, ciphertext_2)
print('Message 1: '+''.join(decoded1))
print('Message 2: '+''.join(decoded2))
