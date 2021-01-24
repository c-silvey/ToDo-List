from django.db import models

class List(models.Model):
    item = models.CharField(max_length=200)
    person = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)

    def __str__(self):
        if self.completed == False:
            return self.item + ' | ' + 'To-doer: ' + self.person  + ' | ' + 'Incomplete'
        else:
            return self.item + ' | ' + 'To-doer: ' + self.person  + ' | ' + 'Complete'