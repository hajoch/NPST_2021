
mapping = {
    '\u200c' : '0',
    '\u200d' : '1'
}

binary = ''
with open('.\\brev.txt', mode="r", encoding="utf8") as f:
    for line in f:
        for char in line:
            if char in mapping:
                binary += mapping.get(char)

def bin_to_str(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

result = bin_to_str(binary)

with open('output.txt', 'w') as f:
    f.write(result)

print('output file written .. ')
print('\033[1m_____ DECODED MESSAGE _____ ')
print('\033[92m'+result+'\033[0m')
