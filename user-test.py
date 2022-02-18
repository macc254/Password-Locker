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
        
    
    
if __name__ == '__main__':
    unittest.main()
