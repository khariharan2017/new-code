name="k.hariharan"
Account_No='00001'
pin_no=3252
int newmoney
newmoney = 10,000
card_number='098776'
print('please insert the ATM card ')
print('enter the pin no:')
pin =int(input(""))
if(pin_no==pin):
    print('enter the money')
    amount=int(input(""))
    newmoney=newmoney-amount
    print(newmoney)
    print('\n')
else:
    print('worng pin_number, Try Again')



