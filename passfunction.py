#By- Abhishek Gupta 7-1-23 XI-PROJECT
# -------------------------------------PASSFUNCTION MODULE / BACK END ----------------------------- 

import keyboard
from random import randrange
import maskpass

#NOTE :
'''
--------SAMPLE DATA HAS BEEN PRE-WRITTEN IN THIS PROGRAM. STORAGE IS Temporary TILL THE PERIOD OF RUNTIME ONLY
PLEASE USE FOLLOWING DATA FOR TESTING THE PROGRAM------
USER NAMES    MASTER PASSWORDS   account names       passwords
1. abcd           123123        google,amazon,fb     'a7slss/*dhjha','28djda%27e!','m$b&hs/*g28)0'
2. xyz            789789        google,amazon,fb     ')ksdfj3@&8','bsa%s7A7e!','m$b&paYJ)0'
'''

#sample
users_info={
    'xyz':['789789','xyz@gmail.com'],
    'abcd':['123123','abcd@gmail.com']
}


def sys_msg(msg=''):
    if msg != '':
        msg = '\n----------------------- '+msg+' -------------------------'
    else :
        msg = '-----------------------------------------------------------'
    print(msg)



# EXECUTED WITH PASS_GEN - PASSWORD GENERATOR
def welcome_passfunc():
    sys_msg('IMPORTANT')
    print('Press \'ENTER\' key to regenerate password')
    print('Press \'SPACEBAR\' key to change password length')
    print('Press \'m\' key to return to main menu')

    
# FUNCTION THAT MATCHES THE USER INPUT TO AVAILABLE OPTIONS AND RUNS THE FUNCTION CORRESPONDING TO IT.
# RUNS IN INFINTE LOOP
# DEFINED IN PASS FUNCTION --- IMPORTED IN PASS_MANAGER_MAIN

def try_again_inp(func,wrong_msg,inp_msg,no_of_ifs,ifs_var,ifs_values,func_exe):
    while True:
        func()
        ifs_var = int(input(inp_msg))
        if ifs_var == no_of_ifs:
            sys_msg('Thank you for using our services.')
            break
        else:
            for i in range(no_of_ifs-1):
                if ifs_var == ifs_values[i]:
                    func_exe[i]()
                    break
            else:
                sys_msg(wrong_msg)
    
    
        

#PASSWORD GENERATOR
def pass_gen():
            
            def randpass():
                
                gen_psd_orig = str()
                for i in range(lenpsd):
                    ch = chr(randrange(33,127))
                    gen_psd_orig += ch
                print(gen_psd_orig)
            keyboard.add_hotkey('enter',randpass)
            keyboard.add_hotkey('space',pass_param)
            randpass()  
            while True:
                
                x=keyboard.read_hotkey(suppress=True)
                if keyboard.is_pressed('enter'):
                    randpass()
                if keyboard.is_pressed('m'):
                     #keyboard.remove_hotkey('enter')
                     #keyboard.remove_hotkey('space')
                     keyboard.unhook_all_hotkeys()
                     break
               
                
                        
# FUNCTION TO INPUT PASSWORD LENGTH                    
def pass_param():
    welcome_passfunc()
    sys_msg('PASSWORD GENERATOR')
    global lenpsd
    while True:
        lenpsd = int(input('Enter length of password required (8 to 20) :  '))
        if lenpsd in range(8,21):
            pass_gen()
            break
        else:
            sys_msg('please try again. Length should be 8 to 20 only.')

class pass_vault:
    
    def __init__(self,name,user_dict):
        self.__dict = user_dict
        self.name = name
        
    def show_keys(self):
        sys_msg('Passwords stored for below URLs/portals/websites/accounts : ')
        if self.__dict == {}:
            print('None')
        else:
            for i in self.__dict:
                print(i)
    def search_rec(self):
        search_key = input('enter key for record to be viewed: ').lower()
        for k in self.__dict:
            if k == search_key:
                sys_msg('')
                print('Key: ',k)
                print('Password: ',self.__dict[k])
                

    def add_rec(self):
        key = input('Enter email/website URL/portal associated with password(*) : ').lower()
        __key_pass = maskpass.advpass('Password: ','*',True)
        if key not in self.__dict:
            self.__dict[key]=__key_pass
            sys_msg('ADDED.')
           
        else:
            sys_msg(f'{key} already present. Try again.')
        
            
    def delete_rec(self):
        search_key = input('enter key for which record to be deleted: ').lower()
        if search_key in self.__dict:
            del self.__dict[search_key]
            sys_msg(f'{search_key} deleted.')
           
    def edit_rec(self):
        edit_ch = int(input('Enter 1 to rename key, 2 to change password: '))
        if edit_ch == 1:
            search_key = input('enter key to be renamed: ').lower()
            new_key = input(f'{search_key},\'s new name: ').lower()
            if search_key in self.__dict:
                self.__dict.update({new_key:self.__dict[search_key]})
                del self.__dict[search_key]
                sys_msg(f'{search_key} changed to {new_key}')
             
        elif edit_ch == 2:
            while True:
                search_key = input('enter key for which password to be changed: ').lower()
                if search_key in self.__dict:
                    __mast_pass = maskpass.advpass('Enter your Master Password: ','*',True)
                    
                    if __mast_pass == users_info[self.name][0]:
                        sys_msg('Verified.')
                        while True:
                         
                            __new_pass = maskpass.advpass('Enter new password: ','*',True)
                            __cfm_new_pass = maskpass.advpass('Confirm new password: ','*',True)
                            if __new_pass == __cfm_new_pass:
                                self.__dict[search_key] = __new_pass
                                sys_msg('Password changed.')
                               
                                break
                            else:
                                sys_msg('Both of the passwords do not match each other. Please try again')
                               
                        break
                    else:
                        sys_msg('Incorrect Password. Please try again. ')
                       
                else:
                    sys_msg('Key not found. Try again.')
                    
#sample data
class storage_pass:
    def __init__(self):
        self.database = {
            'abcd' : pass_vault('abcd',{'google':'a7slss/*dhjha','amazon':'28djda%27e!','fb':'m$b&hs/*g28)0'}),
            'xyz' : pass_vault('xyz',{'google':')ksdfj3@&8','amazon':'bsa%s7A7e!','fb':'m$b&paYJ)0'})
            }
    def add_users(self,name):
        self.database[name] = pass_vault(name,{})

pass_database = storage_pass()        

        
        
























