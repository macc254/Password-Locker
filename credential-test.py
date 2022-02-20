#!/usr/bin/env python3
import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credential("001","Facebook","fachelan","1234")
    def tearDown(self):
        Credential.credential_list = []
    def test_init(self):
        '''
        This will test if the credential has been properly initialized
        '''
        self.assertEqual(self.new_credential.accountId,"001")
        self.assertEqual(self.new_credential.account,"Facebook")
        self.assertEqual(self.new_credential.accountUsername,"fachelan")
        self.assertEqual(self.new_credential.accountPassword,"1234")
        
    def test_save_credential(self):
        '''
        This will test if the credential has been properly saved
        '''
        self.new_credential.save_credential() # save credential
        self.assertEqual(len(Credential.credential_list),1)
        
    def test_delete_credential(self):
        '''
        delete_credential will test if the credential has been deleted
        '''
        self.new_credential.save_credential() # save credential
        test_credential = Credential("002","Twitter","@macc254","44444") # A new credential
        test_credential.save_credential()
        
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)
        
    def test_display_credential(self):
        '''
        test to display credentials in the list of credentials
        '''
        self.assertEqual(Credential.display_credential(),Credential.credential_list)
        
    def test_get_credential(self):
        '''
        test to find credential by the specified accountId
        '''
        self.new_credential.save_credential()
        test_credential = Credential("002","Twitter","@macc254","44444") # A new credential
        test_credential.save_credential()
        
        found_credential = Credential.get_credential("44444")
        self.assertEqual(test_credential.accountPassword, found_credential.accountPassword)
        
    
    def test_account_exists(self):
        '''
        test to check if an account exists
        '''
        self.new_credential.save_credential()
        test_credential = Credential("002","Twitter","@macc254","44444") # A new credential
        test_credential.save_credential()
        
        account_exists = Credential.account_exists(test_credential.accountId)
        self.assertTrue(account_exists)
        
    
if __name__ == '__main__':
    unittest.main()

        