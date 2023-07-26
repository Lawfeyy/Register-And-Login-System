from time import sleep

def validate_password(password):
    if(len(password) >= 8 and len(password) <= 16):
        return True
    return False

def check_user(user, users_list):
    for search in users_list:
        username = search.strip('\n').split(';')[0]
        if username == user:
            return True
    return False

def register_user():
    with open('registered.txt', 'r+', encoding='utf-8') as list:
        print('-='*18)
        print('Enter a username for your registration!')
        print('-='*18)
        user = input('Username:  ')
        sleep(1)
        checklist = list.readlines()
        while check_user(user, checklist):
            user = input('This username already exists!')
            break
        
        print('-='*18)
        password = input('Enter your password (must contain a minimum of 8 characters and a maximum of 16 characters):  ')
        print('-='*18)
        while not validate_password(password):
            password = input('Invalid password! Try again according to the norms:  ')
        list.write(f'{user};{password}\n')
        print('Registered Succesfully.')

def login_user():
    with open('registered.txt', 'r', encoding='utf-8') as login:
        print('-='*18)
        print('Enter your username to access your profile.')
        print('-='*18)
        username = input('Username:  ')
        sleep(1)
        print('-='*18)
        print('Enter your current password.')
        print('-='*18)
        user_password = input('Password:  ')
        sleep(1)
        checklist = login.readlines()
        if check_user(username, checklist):
            for search in checklist:
                user, password = search.strip('\n').split(';')
                if username == user and user_password == password:
                    print('-='*18)
                    print('Welcome back, {}!'.format(username))
                    print('-='*18)
                elif username == user and user_password != password:
                    print('Incorret password! Try again.')
        else:
            print('This user does not exist!')