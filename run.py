#!/usr/bin/env python3
import random
import string
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
            print("Enter these short codes : \n su- To signup a new user,\n lg - To login, \n dc - display credentials,\n fc -find a credential,\n dl - delete a credential,\n ex -exit the Password Locker")

            short_code = input().lower()

            if short_code == 'su':
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
                    print(f"Name: {fname} {lname} \n Username:{username} \n Password:{password}")
                    print ('\n')
                    
            elif short_code == 'lg':
                print ("Enter your username")
                loginUsername = input()
                print ("Enter your password")
                loginPassword = input()
                if find_user_by_password(loginPassword):
                    print ("Welcome!!")
                    print ('\n')
                    print ("Would you like to create accounts? Enter - ca, \n or view accounts, Enter -va")
                    if short_code == 'ca':
                        print ("Create an account:")
                        print ('\n')
                        print ("Enter the Account Name:")
                        account = input()
                        print ("Your username is:")
                        accountUsername = loginUsername
                        print ('\n')
                        print ("Enter:\n gp - if you would like a generated password, \n Or ip - if you would like to input your own password")
                        if short_code == 'gp':
                            passcode = string.ascii_letters
                            accountPassword = ''.join((random.choice(passcode) for i in range(8)))
                            print(f"Password: {accountPassword}")
                        elif short_code == 'ip':
                            print("Enter your own password")
                            accountPassword = input()
                        else:
                            print("Please enter a valid choice")
                            save_credential(create_credential(account,accountUsername,accountPassword))
                            print('\n')
                            print(f"Account: {account},Username: {accountUsername},Password: {accountPassword}")
                            

                        

                        


if __name__ == '__main__':

    main()
