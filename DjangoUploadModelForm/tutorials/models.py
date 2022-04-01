from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    feature_image = models.ImageField(upload_to='tutorial/images/')
    attachment = models.FileField(upload_to='tutorial/attachments/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.feature_image.delete()
        self.attachment.delete()
        super().delete(*args, **kwargs)
