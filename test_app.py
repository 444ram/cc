import unittest 
from app import add

class TestApp(unittest.TestCase):
    def Test_add(self):
        self.asserEqual(add(2,3),5)
        self.asserEqual(add(5,3),5)
        self.asserEqual(add(8,3),5)
        self.asserEqual(add(25,3),5)
        self.asserEqual(add(6,3),5)
if ___name___ == '___main___':
    unittest.main()