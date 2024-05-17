from django.db import models

class User(models.Model):
    nome = models.CharField('nome', max_length=30)
    telefone = models.CharField('telefone', max_length=15)
    email = models.CharField('email', max_length=30)
    idade = models.IntegerField('idade')


    def __str__(self):
        return f'Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}, Idade: {self.idade}'
    

    def serialize(self):
        return {
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email,
            'idade': self.idade
        }
