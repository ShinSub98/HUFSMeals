# Generated by Django 4.2.7 on 2024-02-25 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='식당 이름', max_length=90)),
                ('restaurant_image', models.CharField(default=None, max_length=255, verbose_name='식당 이미지')),
                ('latitude', models.CharField(default=None, max_length=90, verbose_name='위도')),
                ('longitude', models.CharField(default=None, max_length=90, verbose_name='경도')),
                ('opening_hours', models.CharField(default=None, max_length=255, verbose_name='영업 시간')),
                ('address', models.CharField(default=None, max_length=255, verbose_name='주소')),
                ('phone', models.CharField(default=None, max_length=90, verbose_name='전화번호')),
                ('review_cnt', models.IntegerField(default=0, verbose_name='리뷰 개수')),
                ('score_accum', models.IntegerField(default=0, verbose_name='리뷰 합산 점수')),
                ('score_avg', models.FloatField(default=0.0, verbose_name='리뷰 평균 점수')),
            ],
            options={
                'db_table': 'restaurant',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=60, verbose_name='메뉴명')),
                ('menu_image', models.CharField(default=None, max_length=255, verbose_name='메뉴 사진')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant', verbose_name='식당')),
            ],
            options={
                'db_table': 'menu',
            },
        ),
    ]