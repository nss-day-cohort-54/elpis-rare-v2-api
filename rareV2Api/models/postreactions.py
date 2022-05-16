from tkinter import CASCADE
from django.db import models

class PostReactions(models.Model):
    user_id = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    post_id = models.ForeignKey("Post", on_delete=models.CASCADE)
    reaction_id = models.ForeignKey("Reaction", on_delete=models.CASCADE)