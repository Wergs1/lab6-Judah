#encode function
run = True


def encode(inpu):
    ret = ""
    for i in range(0, len(inpu)):
        temp_num = int(inpu[i]) + 3 #basic encode (raw)
        if temp_num > 9:
            ret += str((temp_num-10)) #Makes encoded number (final)
        else:
            ret += str((temp_num))
    return ret


while run == True:
    raw = input("Enter value to encode: ")
    print(str(encode(raw)))