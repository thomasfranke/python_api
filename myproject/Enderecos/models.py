from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    cep = models.IntegerField()
    rua = models.CharField(max_length=255)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Endereço {self.rua}, Número {self.numero}, CEP {self.cep}"
    
    class Meta:
        db_table = 'endereco'
        
    # Método para criar um novo endereço
    @classmethod
    def criar_endereco(cls, cep, rua, numero, complemento=None):
        endereco = cls(cep=cep, rua=rua, numero=numero, complemento=complemento)
        endereco.save()
        return endereco

    # Método para buscar endereço por ID
    @classmethod
    def buscar_endereco_por_id(cls, id):
        try:
            return cls.objects.get(id=id)
        except ObjectDoesNotExist:
            return None

    # Método para buscar todos os endereços
    @classmethod
    def buscar_todos_enderecos(cls):
        return cls.objects.all()

    # Método para atualizar um endereço existente
    def atualizar_endereco(self, cep=None, rua=None, numero=None, complemento=None):
        if cep:
            self.cep = cep
        if rua:
            self.rua = rua
        if numero:
            self.numero = numero
        if complemento:
            self.complemento = complemento
        self.save()
        return self

    # Método para deletar um endereço
    @classmethod
    def deletar_endereco(cls, id):
        try:
            endereco = cls.objects.get(id=id)
            endereco.delete()
            return True
        except ObjectDoesNotExist:
            return False
