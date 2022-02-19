#!/usr/bin/env python3
import unittest
from user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User("001","Mercy","Bore")
        
    def tearDown(self):
        User.user_list = []
        
    def test_init(self):
        self.assertEqual(self.new_user.userId,"001")
        self.assertEqual(self.new_user.first_name,"Mercy")
        self.assertEqual(self.new_user.last_name,"Bore")
        
    def test_save_user(self):
        self.new_user.save_user() # save user
        self.assertEqual(len(User.user_list),1)
        
    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User("002","Joan","Muteti") # A new user with
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
        
        
    
    
if __name__ == '__main__':
    unittest.main()
