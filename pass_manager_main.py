#By- Abhishek Gupta 7-1-23 XI-PROJECT

#----------------------------MAIN MODULE---------------------------

import passfunction
import time, maskpass


#WELCOME SCREEN - AUTHENTICATION - LOGIN/SIGNUP
def welcome_screen():
    passfunction.sys_msg('Welcome to Password Manager v.1.0.0')
    print('1. Login as an existing customer',
           '2. Sign up for the first time',
           '3. EXIT',sep='\n')
    passfunction.sys_msg('')

#MAIN MENU - NAVIGATIONS TO FUNCTIONS
def main_menu():
    passfunction.sys_msg('MAIN MENU')
    print('1. Password Generator',
    '2. Show all accounts/keys',
    '3. Search password in your vault',
    '4. Add account & password to your vault',
    '5. Change accounts & password',
    '6. Delete accounts & password',
    '7. Logout',
    '8. GO BACK',sep='\n')
    passfunction.sys_msg('')

# AUTENTICATE - LOGIN
def login():
    while True:
        passfunction.sys_msg('')
        user_inp = str.lower(input('Username: '))
        mstr_pass_inp = maskpass.advpass('Master Password: ','*',True,True)
        if user_inp in passfunction.users_info and mstr_pass_inp == passfunction.users_info[user_inp][0]:
            passfunction.sys_msg('Verified')
            passfunction.sys_msg('loading')
            
            user =  passfunction.pass_database.database[user_inp]
            time.sleep(2)
            passfunction.try_again_inp(main_menu,'Invalid Input. PLease try again.'\
                                       ,'Enter your choice(1/2/3/4/5/6/7/8): ',\
                                       8,'main_ch',[1,2,3,4,5,6,7,8],\
                                       [passfunction.pass_param, user.show_keys,\
                                        user.search_rec,user.add_rec, user.edit_rec,\
                                        user.delete_rec,welcome_input])
            break
        else:
            passfunction.sys_msg('Entered password or username is wrong. Please try again.')
        
    
        
def signup_auth():
       
        passfunction.sys_msg('IMPORTANT')
        print('>>>>> Please enter below a Master Password (4 to 10 digits long).',
                '>>>>> Master Password is the key to all your stored passwords.',
                '>>>>> Ensure you remember it. Once forgotten, your passwords cannot be recovered.',sep='\n')
        passfunction.sys_msg('')
        psd = maskpass.advpass('Enter your Master Password: ','*',True)
        psd_cfm = maskpass.advpass('Confirm your Master Password: ','*', True)
        if psd == psd_cfm :
            passfunction.users_info[uname] = [psd,email]
            passfunction.pass_database.add_users(uname) 
            user =  passfunction.pass_database.database[uname]
            print('Account successfully created. Thank you')
            passfunction.try_again_inp(main_menu,'Invalid Input. PLease try again.'\
                                       ,'Enter your choice(1/2/3/4/5/6/7/8): ',\
                                       8,'main_ch',[1,2,3,4,5,6,7,8],\
                                       [passfunction.pass_param, user.show_keys,\
                                        user.search_rec,user.add_rec, user.edit_rec,\
                                       user.delete_rec,welcome_input])
        else:
            passfunction.sys_msg('passwords do not match. Try again.')
            signup_auth()
        

#AUTHENTICATE - SIGN UP
def signup():
    global uname, email
    uname = input('Enter your username: ')
    email = input('Enter your email: ')
    if len((email,uname)) != 0 and uname not in passfunction.users_info:
         signup_auth()
        
       

# RUNNING WELCOME SCREEN AFTER BEING LOGGED OUT
def welcome_input():
    passfunction.try_again_inp(welcome_screen,'Invalid Input. Please try again.',\
                               'Enter your choice (1/2/3) : ',3,'wel_ch',[1,2,3],[login,signup])    
# RUNNING WELCOME SCREEN - 1ST TIME IN EXECUTION OF PROGRAM
welcome_input()

    


    
            








