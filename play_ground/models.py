from django.db import models


class Contestant(models.Model):
    twitter_handle = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    points = models.IntegerField(default=0)

    class Meta:
        db_table = 'contestants'
        verbose_name_plural = 'Contestants'

    def __str__(self):
        return self.twitter_handle


class Tweet(models.Model):
    twitter_handle = models.ForeignKey(Contestant, on_delete=models.CASCADE)
    tweet = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tweets'
        verbose_name_plural = 'Tweets'

    def __str__(self):
        return str(self.twitter_handle)
