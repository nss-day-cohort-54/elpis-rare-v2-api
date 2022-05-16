from django.db import models

class PostTags(models.Model):
    tag_id = models.ForeignKey("Tags", on_delete=models.CASCADE)
    post_id = models.ForeignKey("Post", on_delete=models.CASCADE)