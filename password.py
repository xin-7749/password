anr = "qwer1234"
pw = "a19283746"
enter_anr = input("為更改密碼請輸入帳號 : ")
while anr != enter_anr :
    print("帳號不對請重新輸入!!!!")
    enter_anr = input("為更改密碼請輸入帳號 : ")
while anr == enter_anr :
    enter_pw = input ("請輸入新密碼 : ")
    if enter_pw == input("再次輸入密碼 : ") :
        print("更換密碼成功!!!!!")
        break
    else :
        print("密碼不重複請重新輸入 : ")
        
        