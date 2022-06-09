from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Poster(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.username


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.ForeignKey("self", blank=True, null=True, related_name="id", on_delete=models.PROTECT)  # type: ignore
    poster_id = models.ForeignKey(Poster, on_delete=models.PROTECT)  # type: ignore
    commented_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
    comment_text = models.CharField(max_length=1000)


class Upvote(models.Model):
    id = models.AutoField(primary_key=True)
    comment_id = models.ForeignKey(Comment, on_delete=models.PROTECT)  # type: ignore
    poster_id = models.ForeignKey(Poster, on_delete=models.PROTECT)  # type: ignore
    modifier = models.IntegerField(
        default=1, validators=[MinValueValidator(-1), MaxValueValidator(1)]
    )
