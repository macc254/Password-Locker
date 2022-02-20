#!/usr/bin/env python3
from user import User
from credential import Credential


def create_user(userId,fname,lname,username,password): #user functions
    '''
    Function to create a user
    '''
    new_user = User(userId,fname,lname,username,password)
    return new_user
def save_user(user):
    ''' Function to save a user'''
    user.save_user()
    
def delete_user(user):
    ''' Function to delete a user'''
    user.delete_user()

def display_user(user):
    ''' Function to display a user'''
    user.display_user()

def create_credential(accountId,account,accountUsername,accountPassword): #credential functions
    '''
    Function to create a credential
    '''
    new_credential = Credential(accountId,account,accountUsername,accountPassword)
    return new_credential

def save_credential(credential):
    ''' Function to save a credential'''
    credential.save_credential()
    
def delete_credential(credential):
    ''' Function to delete a credential'''
    credential.delete_credential()

def display_credential(credential):
    ''' Function to display a credential'''
    credential.display_credential()
    
def main():
    print("Hello Welcome to Password Locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    
    while True:
            print("Use these short codes : \n nu- create a new user,\n dc - display credentials,\n fc -find a credential,\n dl - delete a credential,\n ex -exit the Password Locker")

            short_code = input().lower()

            if short_code == 'nu':
                    print("New User")
                    print("-"*10)
                    
                    print("User Id ...")
                    userId = input()

                    print ("First name ....")
                    fname = input()

                    print("Last name ...")
                    lname = input()
                    
                    print("Username ...")
                    username = input()
                    
                    print("Password ...")
                    password = input()

                    save_user(create_user(userId,fname,lname, username, password)) # create and save new contact.
                    print ('\n')
                    print(f"New Password Locker for {fname} {lname} created")
                    print ('\n')
                    
if __name__ == '__main__':

    main()
