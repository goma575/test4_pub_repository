from django.db import models

#レビューの最高得点を5に設定。
MAX_RATE=5

RATE_CHOICES=[(x,str(x)) for x in range(0,MAX_RATE+1)]

class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
CATEGORY = (("business","ビジネス"),
            ("life","生活"),
            ("other","その他"),)


class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(max_length=100,
                                choices=CATEGORY)
    thumbnail = models.ImageField(null=True,blank=True)
    user = models.ForeignKey("auth.user",on_delete=models.CASCADE)
    # posted_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey("auth.user",on_delete=models.CASCADE)

    def __str__(self):
        return self.title
