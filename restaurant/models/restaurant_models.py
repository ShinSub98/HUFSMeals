from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length = 90, default = "식당 이름")
    restaurant_image = models.CharField(max_length = 255, default = None, verbose_name = '식당 이미지')
    latitude = models.CharField(max_length = 90, default = None, verbose_name = '위도')
    longitude = models.CharField(max_length = 90, default = None, verbose_name = '경도')
    opening_hours = models.CharField(max_length = 255, default = None, verbose_name = '영업 시간')
    address = models.CharField(max_length = 255, default = None, verbose_name = '주소')
    phone = models.CharField(max_length = 90, default = None, verbose_name = '전화번호')
    review_cnt = models.IntegerField(default = 0, verbose_name = '리뷰 개수')
    score_accum = models.IntegerField(default = 0, verbose_name = '리뷰 합산 점수')
    score_avg = models.FloatField(default = 0.0, verbose_name = '리뷰 평균 점수')

    def save(self, *args, **kwargs):
        if self.review_cnt > 0:
            self.score_avg = round(self.score_accum / self.review_cnt, 2)
        else:
            self.score_avg = 0.0
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'restaurant'


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, null = False, on_delete = models.CASCADE, verbose_name = '식당')
    name = models.CharField(max_length = 60, default = None, verbose_name = '메뉴명')
    menu_image = models.CharField(max_length = 255, default = None, verbose_name = '메뉴 사진')

    class Meta:
        db_table = 'menu'

