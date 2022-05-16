from django.db import models

class Comments(models.Model):
    post_id = models.ForeignKey("Post", on_delete=models.CASCADE)
    author_id = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_on = models.DateTimeField()