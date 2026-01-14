from misc import *
def request_an():
    cd=cdate()
    print('DISCLAIMER : enter your information carefully as we might not be able to resolve your issue')
    print('incase there is any error from your side and your request might remain unrealized;|')
    print('Generating request id.....')
    name=input('Enter your name :')
    if name=="":
        name=='Anonymous'
    phone=input('Enter your contact no. :')
    city=input('Enter your current city :')
    bg=input('Enter required blood group :').upper()
    req_id=r_string(4)
    cur .execute(f'insert into request values("{req_id}","{name}","{phone}","{city}","{bg}","{cd}",NULL)')
    cur.execute('commit;')
    print('Request ID successfully generated....')
    print('Please check the following details :')
    print(f'Name : {name}\nPhone : {phone}\nCity : {city}\nRequest id : {req_id}\nBlood group : {bg}   ')
    print('ATTENTION : Please note the request id and only share with the person who fulfills your request.')