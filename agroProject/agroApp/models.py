from django.db import models


class Work(models.Model):
    createAt = models.DateTimeField()
    modifiedAt = models.DateTimeField(auto_now_add=True)
    recipe = models.TextField()

    def __str__(self):
        return self.recipe
