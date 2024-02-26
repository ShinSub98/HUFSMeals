from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, google_id, family_name, given_name, language, nickname, email, password=None):
        user = self.model(
            google_id = google_id,
            family_name = family_name,
            given_name = given_name,
            language = language,
            nickname = nickname,
            email = email,
            password = password,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, google_id, family_name, given_name, language, nickname, email, password):
        user = self.model(
            google_id = google_id,
            family_name = family_name,
            given_name = given_name,
            # password = password,
            language = language,
            email = email,
            nickname = nickname
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    LANGUAGE_CODE = (
        ('ko', '한국어'),
        ('en', '영어'),
        ('ja', '일본어'),
        ('zh-CN','중국어'),
        ('zh-TW', '대만어'),
        ('vi', '베트남어'),
        ('id', '인도어'),
        ('th', '태국어'),
        ('de', '독일어'),
        ('ru', '러시아어'),
        ('es', '스페인어'),
        ('it', '이탈리아어'),
        ('fr', '프랑스어')
    )
    google_id = models.CharField(max_length = 30, unique = True, verbose_name = '구글 ID')
    family_name = models.CharField(max_length = 60, default = "", verbose_name = '성')
    given_name = models.CharField(max_length = 60, default = "", verbose_name = '이름')
    language = models.CharField(max_length = 10, choices = LANGUAGE_CODE, default = 'ko', verbose_name = '선호 언어')
    nickname = models.CharField(max_length = 60, verbose_name = '닉네임')
    email = models.EmailField(max_length = 255, unique = True, default = "", verbose_name = '이메일')
    is_banned = models.BooleanField(default = False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'language', 'google_id', 'family_name', 'given_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    
    class Meta:
        db_table = 'user'