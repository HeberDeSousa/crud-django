from django.test import TestCase

def add_num(num):
    return num + 1

class SimpleTestCase(TestCase):


    def setUp(self):
        self.num = 1
        self.num2 = 2
    

    def test_add_num(self):
        valor = add_num(self.num)
        self.assertTrue(valor == 2)


    def test_add_num2(self):
        valor = add_num(self.num2)
        self.assertTrue(valor == 3)
