# Generated by Django 4.2.7 on 2024-02-24 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('google_id', models.IntegerField(max_length=255, unique=True)),
                ('language', models.CharField(choices=[('ko', '한국어'), ('en', '영어'), ('ja', '일본어'), ('zh-CN', '중국어'), ('zh-TW', '대만어'), ('vi', '베트남어'), ('id', '인도어'), ('th', '태국어'), ('de', '독일어'), ('ru', '러시아어'), ('es', '스페인어'), ('it', '이탈리아어'), ('fr', '프랑스어')], default='ko', max_length=10)),
                ('nickname', models.CharField(max_length=60)),
                ('is_banned', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
