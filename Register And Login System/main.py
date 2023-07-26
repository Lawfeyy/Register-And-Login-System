from functions import login_user, register_user
from time import sleep


print('-='*18)
print('Select below if you want to register or login in your profile.')
print('''1. Register
2. Login''')
print('-='*18)

choose = input('-->  ')

if choose == '1':
    register_user()
elif choose == '2':
    login_user()
else:
    print('Invalid option!')