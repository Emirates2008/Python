def maskstring(name,secret):
    maskname=[]
    name=list(name)
    for i in name:
        maskname.append(chr(ord(i)-secret%10))=
    return ''.join(maskname)

def unmaskstring(name,secret):
    unmaskname=[]
    name=list(name)
    for i in name:
        unmaskname.append(chr(ord(i)+secret%10))
    return ''.join(unmaskname)
mstring=maskstring(input("Enter a secret (letter,message,etc.), that can only revealed by entering the secret code."),1219404444)
print(mstring)
type(mstring)
print(unmaskstring(mstring,int(input("Enter Secret key to decipher the text"))))
