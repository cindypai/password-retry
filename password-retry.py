password = 'a123456'
x = 3 #剩餘機會
while x > 0:
    psw = input('請輸入密碼：')
    if psw == password:
        print('登入成功')
        break
    else:
        x = x - 1
        print('密碼錯誤！還有', x ,'次機會')