from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200,unique=True)
    social_links = models.URLField(max_length=200,blank=True)

    
    
    @property
    def Approved_Albums(self):
        return str(len(self.albums.filter(isApproved=True)))
    
    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name']
    
    

