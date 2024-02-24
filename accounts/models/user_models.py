from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, google_id, language, nickname, password=None):
        user = self.model(
            google_id = google_id,
            language = language,
            nickname = nickname,
            password = password,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, google_id, language, nickname, password=None):
        user = self.model(
            google_id = google_id,
            password = password,
            language = language,
            nickname = nickname
        )
        user.is_staff = True
        user.save(using = self.db)
        return user


class User(AbstractBaseUser):
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
    google_id = models.IntegerField(max_length = 255, unique = True)
    language = models.CharField(max_length = 10, choices = LANGUAGE_CODE, default = 'ko')
    nickname = models.CharField(max_length = 60)
    is_banned = models.BooleanField(default = False)

    USERNAME_FIELD = 'google_id'
    REQUIRED_FIELDS = ['nickname', 'language']

    objects = UserManager()

    def __str__(self):
        return self.nickname
    
    def has_perm(self, perm, obj=None):
        """
        스태프에게는 전권한 부여
        """
        return self.is_staff
    
    class Meta:
        db_table = 'user'