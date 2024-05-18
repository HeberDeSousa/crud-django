from django.test import TestCase
from app1.models import User

class StrTest(TestCase):


    def setUp(self):
        self.user = User(nome = "Usuario", telefone = "1223423", email = "usuario@user.com.br", idade = 20)

    
    def test_str(self):
        self.assertEqual(str(self.user), 'Nome: Usuario, Telefone: 1223423, Email: usuario@user.com.br, Idade: 20')

    
    def test_serialize(self):
        self.assertEqual(self.user.serialize(), {
            'nome': 'Usuario',
            'telefone': '1223423',
            'email': 'usuario@user.com.br',
            'idade': 20
        })
