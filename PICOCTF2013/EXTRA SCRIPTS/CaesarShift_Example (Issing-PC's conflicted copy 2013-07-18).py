from CaesarShift import CaesarCipher

CS = CaesarCipher()
z=open("ManualEncyrpted.txt","r")
x=open("ManualDecrypted.txt","w")
for line in z:
    x.write(CS.decrypt(line,7))
