from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        verbose_name='이메일'
    )
    name = models.CharField(
        max_length=20,
        verbose_name='이름'
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='가입일'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='활성화 여부'
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name='관리자 여부'
    )

    class Meta:
        db_table = 'users'
        verbose_name = '유저'
        verbose_name_plural = '유저들'

    def __str__(self):
        return self.email
