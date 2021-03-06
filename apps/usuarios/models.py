from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.urls import reverse

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Insira um e-mail válido para continuar!')

        usuario = self.model(
            email=self.normalize_email(email),
        )
        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False
        if password:
            usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, email,  password, **kwargs):
        usuario = self.create_user(
            email=self.normalize_email(email),
            password=password,
            **kwargs
        )
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.set_password(password)
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name = "E-mail:",
        max_length = 194,
        unique = True,
    )

    nome = models.CharField(
        verbose_name = "Nome Completo:",
        max_length = 194,
        null = False,
    )

    cpf = models.CharField(
        verbose_name = "CPF:",
        max_length = 14,
        unique = True,
        null = True,
    )

    data_nascimento = models.DateField(
        verbose_name = "Data de Nascimento:",
        auto_now_add = False,
        auto_now = False,
        null = True,
    )

    is_active = models.BooleanField(
        verbose_name="Usuário está ativo",
        default = True,
    )

    is_staff = models.BooleanField(
        verbose_name = "Usuário é da equipe de desenvolvimento",
        default = False,
    )

    is_superuser = models.BooleanField(
        verbose_name = "Usuário é um superusuário",
        default = False,
    )

    USERNAME_FIELD = "email"

    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuario"

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('index')
        # return reverse('index', args=[str(self.id)]) CASO NECESSITASSE PASSAR ID