verify_arr = [193, 35, 9, 33, 1, 9, 3, 33, 9, 225]
all_chars = range(0, 255)

for hash1 in verify_arr:
    for char1 in all_chars:
        charHash = ((char1 << 5 | char1>> 3) ^111) & 255
        if charHash == hash1:
            print (unichr(char1))
