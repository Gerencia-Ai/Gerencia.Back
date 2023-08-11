from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class TipoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(_("Description"), max_length=200)

    def __str__(self):
        return str(self.id) + " " + self.descricao

class Usuario(AbstractUser):
    username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    cpf = models.CharField(_("CPF"), max_length=11, blank=True, null=True)
    telefone = models.CharField(_("Phone"), max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(
        _("Birth Date"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.PROTECT, related_name="usuario", default=1)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]

