from donor import *
from request import *
requesteval()
print('Welcome to Bloodpoint !')
while True:
    try:
        y=int(input('Register (new user) - 1\nLogin (existing user) - 2\nRequest blood(emergency) - 3\nNOTE : donation can also be requested after creating an account.\nExit - 4\n'))
        if y==1:
            register()
        elif y==2:
            ID=input('Enter login id :')
            if ID in member('ID','donor'):
                login(ID)
            else:
                    print('Account does not exist....Please recheck your id or register with us now')
        elif y==3:
            request_an()
        elif y==4:
            break
        else:
            print('Please select a valid option..')
        cont=int(input('Continue - 1\nExit - 2\n'))
        if cont==2:
            break
    except:
        print('Unexpected internal error occured\nRedirected to login page')