pd = 'a123456'
x = 0
y = 3

while True:
    uspd = input('請輸入密碼： ')
    if uspd == pd:
        print('密碼確認，已成功登入！')
        break
    elif uspd != pd:
        x = x + 1
        y = y - 1
        print('密碼錯誤', x,'次','您有剩', y,'次登入機會')
        if x >= 3:
            print('哦喔，亂踹密碼者必誅之，登入中斷')
            break

    

