from django.db import models  # import the models package

class Page(models.Model):  # create Page class, which inherits from Model class
  title = models.CharField(max_length=60)                  # define
  permalink = models.CharField(max_length=12, unique=True) # the
  update_date = models.DateTimeField('Last Updated')       # model's
  bodytext = models.TextField('Page Content', blank=True)  # fields
  def __str__(self):   # create class method for human-readable class obj name
      return self.title
