from django.db import models


# Create your models here.
class App(models.Model):
    name = models.CharField(
        max_length= 30,
        db_comment= 'The name of the app',
        help_text= 'The name of the app',
        primary_key= True,
    )
    entryPoint = models.CharField(
        max_length= 30,
        db_comment= 'The entry point of the app in the webServer',
        help_text= 'The entry point of the app in the webServer',
    )
    displayName = models.CharField(
        max_length= 30,
        db_comment= 'The name to be displayed in the menu',
        help_text= 'The name to be displayed in the menu',
    )

    def __str__(self) -> str:
        return f'{self.displayName}({self.entryPoint})'
