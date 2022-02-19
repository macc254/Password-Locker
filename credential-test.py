#!/usr/bin/env python3
from credential import Credential

class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credential("001","Facebook","fachelan","1234")
    def tearDown(self):
        Credential.credential_list = []
    def test_init(self):
        self.assertEqual(self.new_credential.accountId,"001")
        self.assertEqual(self.new_credential.account,"Facebook")
        self.assertEqual(self.new_credential.username,"fachelan")
        self.assertEqual(self.new_credential.password,"1234")
        