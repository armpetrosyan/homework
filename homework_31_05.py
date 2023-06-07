file = open('reaganomics.txt')
fs = open('copy.txt', 'w+')


for sentence in file:
    if 'Federal income tax and payroll tax levels' in sentence:
        break
    else:
        fs.write(sentence)

fs.seek(0)

print(fs.read())

file.close()
fs.close()
