#!/usr/bin/python3

import unittest

from fake_modules.fake_email import email
from fake_modules.fake_id import make_id,check_id
from fake_modules.fake_ip import ip
from fake_modules.fake_name import name
from fake_modules.fake_number import number
from fake_modules.fake_phone import phone

class testProfaker(unittest.TestCase):
        
    def setUp(self):
    
            pass
            
    def test_email(self):
    
        self.assertTrue(email(),'email error')
        self.assertTrue(email(10),'email n error')

    def test_make_id(self):

        self.assertTrue(make_id(),'make id error')
        self.assertTrue(check_id(make_id()),'checkid error')
        self.assertFalse(check_id(123),'checkid error')
    
    def test_ip(self):

        self.assertTrue(ip(),'ip error')

    def test_name(self):

        self.assertTrue(name(),'name error')

    def test_number(self):

        self.assertTrue(number(),'number error')
        self.assertEqual(11,len(number(11)),'number error')

    def test_phone(self):

        self.assertTrue(phone(),'phone error')


if __name__ == '__main__':
    unittest.main()
