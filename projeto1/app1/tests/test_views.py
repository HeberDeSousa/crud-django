from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from app1.models import User

class ViewTest(TestCase):


    def setUp(self):
        self.dados = {
            'nome': 'nome',
            'telefone': '12345',
            'email': 'email',
            'idade': 0
        }

        self.client = Client()
    

    def test_index(self):
        request = self.client.get(reverse_lazy('indexUsuario'))
        self.assertEqual(request.status_code, 200)
    

    def test_criar(self):
        request = self.client.post(reverse_lazy('criarUsuario'), data=self.dados)
        self.assertEqual(request.status_code, 302)
