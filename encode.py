#encode function
run = True


def encode(inpu):
    ret = ""
    for i in range(0, len(inpu)):
        temp_num = int(inpu[i]) + 3
        if temp_num > 9:
            ret += str((10-temp_num))
        else:
            ret += str((temp_num))
    return ret


while run == True:
    raw = input("Enter value to encode: ")
    print(str(encode(raw)))