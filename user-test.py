#!/usr/bin/env python3
import unittest
from user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User("001","Mercy","Bore","macc254","123456")
        
    def tearDown(self):
        User.user_list = []
        
    def test_init(self):
        '''
        This will test if the use has been properly initialized
        '''
        self.assertEqual(self.new_user.userId,"001")
        self.assertEqual(self.new_user.first_name,"Mercy")
        self.assertEqual(self.new_user.last_name,"Bore")
        self.assertEqual(self.new_user.username,"macc254")
        self.assertEqual(self.new_user.password,"123456")
        
    def test_save_user(self):
        '''
        This will test if the use has been properly saved
        '''
        self.new_user.save_user() # save user
        self.assertEqual(len(User.user_list),1)
        
    def test_delete_user(self):
        '''
        delete_user will test if the user has been deleted
        '''
        self.new_user.save_user()
        test_user = User("002","Joan","Muteti","jm","44444") # A new user 
        test_user.save_user()
        
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
        
    def test_display_user(self):
        '''
        test to display users in the list of users
        '''
        self.assertEqual(User.display_user(),User.user_list)
        
    def test_find_user_by_id(self):
        '''
        test to find users by the specified userId
        '''
        self.new_user.save_user()
        test_user = User("002","Joan","Muteti","jm","44444") # A new user 
        test_user.save_user()
        
        found_user = User.find_user_by_number("002")
        self.assertEqual(test_user.userId, found_user.userId)
        
    
    def test_check_user_exists(self):
        '''
        test to check if a user exists
        '''
        self.new_user.save_user()
        test_user = User("002","Joan","Muteti","jm","44444") # A new user 
        test_user.save_user()
        
        check_user_exists = User.check_user_exists(test_user.userId)
        self.assertTrue(check_user_exists)
        
    
if __name__ == '__main__':
    unittest.main()
