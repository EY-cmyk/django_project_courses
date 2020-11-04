import datetime
from django.db import models
from django.utils import timezone

class Course(models.Model):
    course_title = models.CharField('Name of course', max_length = 200)
    course_description = models.TextField("Descriptiom of cource")
    date_of_start = models.DateTimeField('Date of begining of course')
    # cost_of_course = models.TextField('Cost_of_course')
    # date_of_end = models.DateTimeField('Date of course end')
    # course_image = models.ImageField(null=True, blank=True, upload_to="imges/", verbose_name="Изображение")
    

    def __str__(self):
        return self.course_title
      

    def Meta():
        verbose_name = "Course"
        verbose_name_plural = "Courses"

