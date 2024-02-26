from django.db import models
import uuid

def restaurant_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"대표이미지_{instance.pk}.{ext}"
    return f"restaurant/{instance.name}/{filename}"


def menu_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name}_{instance.pk}.{ext}"
    return f"restaurant/{instance.restaurant.name}/{filename}"


class Restaurant(models.Model):
    name = models.CharField(max_length = 90, default = "식당 이름")
    restaurant_image = models.ImageField(upload_to = restaurant_upload_to, null = True, blank = True, verbose_name = '식당 이미지')
    latitude = models.CharField(max_length = 90, default = None, verbose_name = '위도')
    longitude = models.CharField(max_length = 90, default = None, verbose_name = '경도')
    opening_hours = models.CharField(max_length = 255, default = None, verbose_name = '영업 시간')
    address = models.CharField(max_length = 255, default = None, verbose_name = '주소')
    phone = models.CharField(max_length = 90, default = None, verbose_name = '전화번호')
    review_cnt = models.IntegerField(default = 0, verbose_name = '리뷰 개수')
    score_accum = models.IntegerField(default = 0, verbose_name = '리뷰 합산 점수')
    score_avg = models.FloatField(default = 0.0, verbose_name = '리뷰 평균 점수')

    def __str__(self):
        return self.name

    def add_review(self, score):
        self.review_cnt += 1
        self.score_accum += score
        self.score_avg = round(self.score_accum / self.review_cnt, 2)
        self.save()

    class Meta:
        db_table = 'restaurant'


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, null = False, on_delete = models.CASCADE, verbose_name = '식당')
    name = models.CharField(max_length = 60, default = None, verbose_name = '메뉴명')
    menu_image = models.ImageField(upload_to = menu_upload_to, null = True, blank = True, verbose_name = '메뉴 이미지')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'menu'

