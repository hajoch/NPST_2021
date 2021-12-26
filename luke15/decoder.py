output = ''
with open('./manual_output.txt') as f:
    for line in f:
        for num in line.split(' '):
            output += chr(int(num))

print('\033[1m_____ DECODED MESSAGE _____ ')
print('\033[92m'+output+'\033[0m')
