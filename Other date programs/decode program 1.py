Secret="kiv"
counter = 0
decrypt = ""
while(counter<len(Secret)):
    value = ord(Secret[counter])
    value = value-8
    if (value<97):
        value = value +26
    value = chr(value)
    decrypt = decrypt +value
    counter = counter +1
print(decrypt)
