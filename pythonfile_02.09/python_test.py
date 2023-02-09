
#test_02.09

import transcrypt 
print("これはテストです")

while True:
    
    num = input("正の整数を入力してください。")
    int_num = int(num)

    if int_num >= 100:
        print("入力された数は100以上!!")
        break
    elif 1 <= int_num < 100:
        print("入力された数は100ミマン!!")
        break
    else :
        print("なに? もう一度ちゃんと正の整数入力して!!!!!")
        

