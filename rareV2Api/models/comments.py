from django.db import models

class Comments(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    author = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    
    @property
    def is_current(self):
        return self.__is_current
    
    @is_current.setter
    
    def is_current(self, value):
        self.__is_current=value