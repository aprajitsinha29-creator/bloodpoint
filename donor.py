from misc import *
def register():                                                                                                         #add a new donater to the database
    dor=cdate()
    mail=input('Enter your mail id :')
    phone=input('Enter your phone number :')
    print('Create Account -')
    name=input('Enter Name :')
    dob=input('Enter your date of birth(YYYY-MM-DD) :')
    age=datediff(dob,dor,'years')
    if age<18:
        print('You are not eligible to create an account')
        return
    bg=input('Enter your blood group :').upper()
    ldod=input('Enter the last time you donated your blood :')
    city=input('Enter your city :')
    while True:
        user_id=input('Enter User ID :')                                                            #checks whether the user id is already existing in the donor table to reduce redundancy
        if user_id in member('ID',"donor"):
            print('User ID is taken,please choose another User ID.')
        else:
            break
    pas=input('Enter Password :')
    while True:
        cnf=input('Confirm Password :')
        if pas==cnf:
            break
        else:
            print('Password does not match!')
    cur.execute(f'insert into donor values("{user_id}","{name}","{mail}","{phone}","{dob}","{pas}","{dor}",0,"None","{city}","{ldod}",0,"{bg}",{age});')
    cur.execute('commit;')
    print('Account successfully created !\nWelcome to Bloodpoint donor group!')
def av_request(ID):                                                                             #show blood requests according to the donors city in the sequence :1 - same city....2 - different cities
    l=['Name','Contact','City']
    cur.execute(f'select city,blood_group from donor where ID="{ID}"')
    for i in cur:
        x,y=i
    print('In your city :')
    cur.execute(f'select Name,Phone,City,bloodgrp from  request where City="{x}" and bloodgrp="{y}";')
    print(tabulate.tabulate(cur))
    print('In other cities :')
    cur.execute(f'select Name,Phone,City,bloodgrp from  request where City!="{x}" and bloodgrp="{y}";')
    print(tabulate.tabulate(cur))
def add_donation(ID):                                                                       #updates no. of donations and recieved awards of the donor by checking request id in the request table
    cd=cdate()
    cur.execute(f'select last_date_of_donation from donor where ID="{ID}"')
    ldod=str(curextract(cur))   
    if datediff(ldod,cd,'months')>=3:
        req_id=input('Enter corresponding request id :')
        if req_id in member('Request_id','request'):
            cur.execute(f'select no_donations from donor where ID="{ID}"')
            x=curextract(cur)
            cur.execute(f'update donor set no_donations={x+1} where ID="{ID}";')
            cur.execute('commit;')
            cur.execute(f'select Title,Prize from Award where  No_donation={x+1}')
            for i in cur:
                t,p=i
            cur.execute(f'update donor set Awards="{t}",Credit=Credit+{p},last_date_of_donation="{cd}" where ID="{ID}"')
            cur.execute('commit;')
            print('Donation successfully added !')
        else:
            print('Update failed!\nPlease recheck the request id or try again later..')
    else:
        print('You have not completed the tenure required to repeat donation....\nPlease wait till the tenure is completed and try again later')
def view_prof(ID):                                                                              #displays the stored information of the concerned donor
    l=['ID','Name','Mail','Phone','Date of birth','Age','Date of registration','No. of donations','Awards','City','Last date of donation','Credit']
    cur.execute(f'select ID,Name,Mail,Phone,DOB,Age,DOR,no_donations,Awards,city,last_date_of_donation,Credit from donor where ID="{ID}"')
    print(tabulate.tabulate(cur,headers=l,tablefmt='grid'))
def edit_profile(ID):                                                                           #allows the donor to edit their existing information in the database
    fn=int(input('Name - 1\nDate of birth - 2\nMail - 3\nPhone - 4\nPassword - 5'))
    if fn==1:                                                                                           #edit name
        n_name=input('Enter your new name :')
        cur.execute(f'update donor set Name="{n_name}" where ID="{ID}"')
        cur.execute('commit;')
        print('Your name has been successfully updated !')
    elif fn==2:                                                                                         #edit date of birth
        cur.execute(f'select DOR from donor where ID="{ID}"')
        dor=str(curextract(cur))
        n_dob=input('Enter your new date of birth :')
        age=datediff(n_dob,dor,'years')
        cur.execute(f'update donor set DOB="{n_dob}",Age="{age}" where ID="{ID}"')
        cur.execute('commit;')
        print('Your date of birth has been successfully updated !')
    elif fn==3:                                                                                         #edit mail id
        n_mail=input('Enter your new mail :')
        cur.execute(f'update donor set Mail="{n_mail}" where ID="{ID}"')
        cur.execute('commit;')
        print('Your mail id has been successfully updated !')
    elif fn==4:                                                                                     #edit phone no.
        n_no=input('Enter your new phone no. :')
        cur.execute(f'update donor set Phone ="{n_no}" where ID="{ID}"')
        cur.execute('commit;')
        print('Your phone no. has been successfully updated !')
    elif fn==5:                                                                                     #edit password
        while True:
            p_password=input('Enter your previous password :')
            cur.execute(f'select Password from donor where ID="{ID}"')
            if p_password==curextract(cur):
                n_password=input('Enter your new password :')
                cur.execute(f'update donor set Password="{n_password}" where ID="{ID}"')
                cur.execute('commit;')
                print('Your password has been successfully updated !')
                break
            else:
                print('Incorrect password !')
def del_ac(ID):                                                                                     #allows the donor to delete their account
    cf=input('WARNING! all the information will be lost !\nDelete account?\nYes -1\nNo - 2\n')
    if cf=='1':
        cur.execute(f'delete from donor where ID="{ID}"')
        cur.execute('commit;')
        print('Account successfully deleted!')
    else:
        function(ID)
def request(ID):
    a=input('Request donation - 1\nManage requests - 2\n')
    if a=='1':
        print('Generating request id.....')
        cur.execute(f'select Name,Phone,blood_group from donor where ID="{ID}"')
        for i in cur:
            name,phone,bg=i
        city=input('Enter your current city :')
        req_id=r_string(4)
        cd=cdate()
        cur .execute(f'insert into request values("{req_id}","{name}","{phone}","{city}","{bg}","{cd}","{ID}")')
        cur.execute('commit')
        print('Request ID successfully generated....')
        print('Please check the following details :')
        print(f'Name : {name}\nPhone : {phone}\nCity : {city}\nRequest id : {req_id}')
        print('ATTENTION : Please note the request id and only share with the person who fulfills your request.')
    elif a=='2':
        x=int(input('View requests - 1\nDelete request - 2\n'))
        l=['Request id','Name','Phone','city','bloodgroup','date of request']
        if x==1:
            cur.execute(f'select Request_id,Name,Phone,city,bloodgrp,date_of_request from request where ID="{ID}"')
            print(tabulate.tabulate(cur,headers=l,tablefmt='grid'))
        elif x==2:
            reqid=input('Enter the request id to be deleted:')
            cur.execute(f'delete from request where Request_id="{reqid}"')
            cur.execute('commit')
            print('Request successfully deletedx')
def function(ID):                                                                                   #allows the donor to choose between different fucntions
    while True:
        fn=int(input('Available requests - 1\nAdd donation - 2\nCurrent requests - 3\nView profile - 4\nEdit profile - 5\nDelete account - 6\nExit - 7\n'))
        if fn==1:
            av_request(ID)
        elif fn==2:
            add_donation(ID)
        elif fn==3:
            request(ID)
        elif fn==4:
            view_prof(ID)
        elif fn==5:
            edit_profile(ID)
        elif fn==6:
            del_ac(ID)
            break
        elif fn==7:
            break
def login(ID):                                                                                      #allows and existing donor account holder to access their account through above defined function (function())
    pas=input('Enter password :')
    cur.execute(f'select Password from donor where ID="{ID}"')
    c_pass=curextract(cur)
    if pas==c_pass:
        print('Welcome !...What would you like to do?')
        function(ID)
    else:
        print('Password incorrect !..Please try again')
        login(ID)
def requesteval():                                                                              #removes request from the request table that are more than 3 months old
    cur.execute('select Request_id,date_of_request from request')
    for i in cur.fetchall():
        if datediff(str(i[1]),str(cdate()),'months')>3:
            cur.execute(f'delete from request where Request_id="{i[0]}"')
            cur.execute('commit')
