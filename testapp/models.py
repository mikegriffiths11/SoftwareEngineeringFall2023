from django.db import models
from django.db import models

class Term(models.Model):
    school_year = models.IntegerField()
    term_id = models.IntegerField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def year_term(self):
        return str(self.school_year) + str(self.term_id)




# Create your models here.
class StepInTheProcess(models.Model):
class vegitableCustomization(StepInTheProcess):
    pass
class sauceCustomization(StepInTheProcess):
    pass
class baseBuild(StepInTheProcess):
    pass