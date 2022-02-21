#!/usr/bin/env python3
import random
import string
from simple_colors import *
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

def display_user():
    ''' Function to display a user'''
    return User.display_user()
def check_user_exists(number):
    '''
    Function that check if a user exists with that number 
    '''
    return User.check_user_exists(number)

def find_user_by_password(number):
    ''' Function to find a user by password'''
    return User.find_user_by_password(number)

def create_credential(account,accountUsername,accountPassword): #credential functions
    '''
    Function to create a credential
    '''
    new_credential = Credential(account,accountUsername,accountPassword)
    return new_credential

def save_credential(credential):
    ''' Function to save a credential'''
    credential.save_credential()
    
def delete_credential(credential):
    ''' Function to delete a credential'''
    credential.delete_credential()

def display_credential():
    ''' Function to display a credential'''
    return Credential.display_credential()
    
def get_credential(number):
    '''
    Function to retrieve a credential
    '''
    return Credential.get_credential(number)
def check_credential_exists(number):
    '''
    Function that check if a credential exists with that number 
    '''
    return Credential.credential_exists(number)
    
def main():
    while True:
            print(cyan("Enter these short codes : \n su - To signup a new user,\n lg - To login, \n ca - create a new account and save, \n va - To view existing accounts,\n dl - delete a credential,\n ex -exit the Password Locker, \n "))

            short_code = input().lower()

            if short_code == 'su':
                    print(magenta("New User"))
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
                    print(f"New Password Locker for {fname} {lname} created")
                    print(f"Name: {fname} {lname} \n Username:{username} \n Password:{password}")
                    print ('\n')
                    
            elif short_code == 'lg':
                print ("Enter your username")
                loginUsername = input()
                print ("Enter your password")
                loginPassword = input()
                if find_user_by_password(loginPassword):
                    print(magenta(f"Welcome to password locker.\n Login successful!"))
                    print(yellow("To create a new account,Enter - ca, \n To view existing accounts, Enter - va"))
                    print('\n')
                else:
                    print(red("Invalid username or password"))
                
            elif short_code == 'ca':
                print (red("Create an account"))
                print('_' * 10)
                print ("Enter the Account Name:")
                account = input()
                print ("Your username is:")
                accountUsername = input()
                print ('\n')
                print("Enter your own password")
                accountPassword = input()
                save_credential(create_credential(account,accountUsername,accountPassword))
                print(f"New Account Successfully created \n Account: {account},\n Username: {accountUsername},\n Password: {accountPassword}")
            
            elif short_code == 'va':
                if display_credential():
                    for credential in display_credential():
                        print(f"Here are your Accounts: \n Account: {credential.account} \n Username: {credential.accountUsername} \n Password: {credential.accountPassword}")
                        print('\n')
                else:
                    print(red("You have no accounts available"))
                    print('\n')
           
            
            elif short_code == 'dl':
                    print("Enter the password for the account you want to delete")
                    search_number = input()
                    if check_credential_exists(search_number):
                            search_credential = get_credential(search_number)
                            delete_credential(search_credential)
                            print(yellow(f"You have deleted one account from the Credential List"))
                            print('\n')
                    else:
                        print(red("That account does not exist"))
                        print('\n')
                
            
            if short_code == 'ex':
                print("Bye .......")
                break
           
            
                

if __name__ == '__main__':

    main()
