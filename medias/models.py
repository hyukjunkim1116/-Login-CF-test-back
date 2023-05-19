from django.db import models


class Photo(models.Model):
    file = models.URLField()
    description = models.CharField(
        max_length=140,
    )

    def __str__(self) -> str:
        return str(self.id)


# Create your models here.
