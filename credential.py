class Credential:
    '''
    This is a class that generates new instances of Credentials
    '''
    credential_list = [] #empty credentials list  for the accounts
    
    def __init__(self, accountId, account,accountUsername,accountPassword):
        self.accountId = accountId
        self.account = account
        self.accountUsername = accountUsername
        self.accountPassword = accountPassword
        
    def save_credential(self):
        '''
        save_credential method saves credentials objects into credentials_list
        '''
        Credential.credential_list.append(self)
        
    def delete_credential(self):
        '''
        delete_credential method deletes credentials objects from credentials_list
        '''
        Credential.credential_list.remove(self)
        
    @classmethod
    def display_credential(cls):
        '''
        display_user method displays credentials in the list
        '''
        return cls.credential_list
               

    @classmethod
    def get_credential(cls,number):
        '''
        This is  a method that returns an account that matches the number entered
        Args:
            number: The accountId of the account
        Return:
            Account that matches the number entered
        '''
        for credential in cls.credential_list:
            if credential.accountId == number:
                return credential
            
    @classmethod
    def account_exists(cls,number):
        '''
        This is a method that checks an account if it exists in the credential list
        Args: 
            Number: The accountId that will be used to search if an account account_exists
        Returns: 
            Boolen: True if the account exists and false if it does not
        '''
        for credential in cls.credential_list:
            if credential.accountId == number:
                return True
        return False
    
                  
        