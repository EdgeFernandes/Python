from django.db import models

class books(models.Model):
    id_books = models.UUIDField(primary_key=True, editable=False )
    title = models.models.CharField( max_length=225)
    aurthor = models.CharField(max_length=225)
    relaese_year = models.IntegerField()
    state = models.CharField(max_length=225)
    pages = models.IntegerField()
    publishing_campany = models.CharField(max_length=225)
    create_at = models.DateTimeField(auto_now_add=True)
    
    
