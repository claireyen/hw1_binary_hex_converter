#轉二進制
def decimal_to_bi(num):
    ans = []
    for i in range(7, -1, -1):
        if (num - 2**i) >=  0:
            num = num - 2**i
            ans.append(1)
        else:
            ans.append(0)
    return ans

#轉十六進制
def decimal_to_hex(num):
    a = num // 16
    num = num % 16
    if num == 15:
        b = 'F'
    elif num == 14:
        b = 'E'
    elif num == 13:
       b = 'D'
    elif num == 12:
        b = 'C'
    elif num == 11:
        b = 'B'
    elif num == 10:
        b = 'A'
    else:
        b = num
    return( str(a) + str(b) )

#主程式碼
def Start():
    while True:
        input_ = input('Plz enter a number between 0~255\nOr enter Stop to quit\nEnter:')
        if input_ == "Stop":
            break
        elif ( int(input_) > 255 ) or ( int(input_) < 0 ):
            continue
        else:
            print('This number decimal to binary is : ', decimal_to_bi(int(input_)))
            print('This number decimal to hex is : ', decimal_to_hex(int(input_)))

Start()
    