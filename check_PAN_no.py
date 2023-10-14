s = str(input("Enter the PAN number: "))
chk = 0
if s.isupper() == True and len(s)==10:
    for i in range(len(s)):
        if i<5 and i >=0:
            if s[i].isupper() == False or s[i].isalpha() == False:
                chk = 1
                break
        if i>=5 and i<9:
            if s[i].isnum()== False:
                chk = 1
                break
        if i == 10:
            if s[i].isalpha() == False:
                chk = 1
                break
else:
    chk = 1

if chk == 0:
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")
                
                
            
