from django.db import models

# Create your models here.
class ANIMAL(models.Model):

    class especie(models.TextChoices):
        dogs = "CÃES", "Cães"
        cats = "GATOS", "Gatos"

    class sexo(models.TextChoices):
        m = "M", "Masculino"
        f = "F", "Feminino"

    class porte(models.TextChoices):
        g = "G", "Grande"
        m = "M", "Médio"
        p = "P", "Pequeno"

    nome = models.CharField(max_length=15, null=False)
    especie = models.CharField(max_length=5, choices=especie.choices, default=especie.dogs, null=False)
    sexo = models.CharField(max_length=1, choices=sexo.choices, default=sexo.m, null=False)
    porte = models.CharField(max_length=1, choices=porte.choices, default=porte.m, null=False)
    #microchip
    isMichip = models.BooleanField(default=True, null=True)
    isCastrado = models.BooleanField(default=True, null=True)
    isAdopted = models.BooleanField(default=False, null=True)
    pelagem = models.CharField(max_length=20, null=True)
    #data de cadastro
    data_cad = models.DateTimeField(auto_now_add=True)
    foto_url = models.ImageField(upload_to="images/", null=True)

    class Meta:
        ordering = ["-data_cad"]
        verbose_name_plural = 'ANIMALS'

    def __str__(self):
        return self.nome