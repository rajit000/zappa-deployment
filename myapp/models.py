from django.db import models

# Create your models here.
# ID, StudentUUID, FirstName, LastName, Class, Section, City, District, State, Pincode, About, IsDeleted, CreatedAt, CreatedBy, UpdatedAt, UpdatedBy
class testmodel(models.Model):
    FirstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    Class = models.CharField(max_length = 50)
    Section = models.CharField(max_length = 50)
    City = models.CharField(max_length = 50)
    # created_at = models.DateTimeField(auto_now_add = True, null = True)
    # updated_at = models.DateTimeField(auto_now_add = True, null = True)
    def __str__(self):
            return str(self.name)