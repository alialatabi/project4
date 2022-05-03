from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    post = models.CharField(max_length=255)
    time_stamp = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} || {self.time_stamp} || {self.post}"

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "post": self.post,
            "time_stamp": self.time_stamp.strftime("%b %d %Y, %H:%M:%S"),
            "like_count": self.like_count
        }


class Follower(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower', default=None)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following', default=None)

    class Meta:
        unique_together = (('follower', 'following'),)

    def __str__(self):
        return f"{self.follower} : {self.following}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment", default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment", default=None)
    comment = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user} || {self.post} || {self.comment}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like", default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like", default=None)

    class Meta:
        unique_together = (('post', 'user'),)

    def __str__(self):
        return f"{self.user} || {self.post}"
