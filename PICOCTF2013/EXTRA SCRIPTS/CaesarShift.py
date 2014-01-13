class CaesarCipher():
    
    global symbols
    symbols="?><,./;:[]{}\|=+-_() *&^%$#@!''1234567890"

    def __init__(self):
        pass
    def decrypt(self,cifered,shift):
        if shift>26:
            shift=shift%26
        cifered=cifered.lower()
        decryptedText=''
        for x in cifered:
            if x in symbols:
                decryptedText+=x
            else:
                if ord(x)-shift<97:
                    shift2=((26)-shift)
                    z=ord(x)+shift2
                else:
                    z=ord(x)
                    shift2=shift*-1
                    z=z+shift2
                decryptedText+=chr(z)
        return decryptedText
    def encrypt(self,text,shift):
        if shift>26:
            shift=shift%26
        text=text.lower()
        encryptedText=""
        for x in text:
            if x in symbols:
                encryptedText+=x
            else:
                if ord(x)+shift>122:
                    shift2=(26)-shift
                    z=ord(x)-shift2
                else:
                   z=ord(x)
                   shift2=shift*-1
                   z=z-shift2
            encryptedText+=chr(z)
        return encryptedText
