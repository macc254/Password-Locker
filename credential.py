class Credential:
    '''
    This is a class that generates new instances of Credentials
    '''
    credential_list = [] #empty credentials list  for the accounts
    
    def __init__(self,userId, account,username,password):
        self.accountId = accountId
        self.account = account
        self.username = username
        self.password = password
        
    def save_credential(self):
        '''
        save_credential method saves credentials objects into credentials_list
        '''
        Credential.save_credential.append(self)
        
    def delete_credential(cls,number):
        '''
        delete_credential method deletes credentials objects from credentials_list
        '''
        for credential in cls.credential_list:
            if credential.accountId == number:
                return credential.credential_list.remove(number)
            
                  
        