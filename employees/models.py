from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}"


class StaffBase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True

    def get_role(self):
        return "Staff"

class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def get_role(self):
        return "Manager"

class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.CASCADE)
    internship_end = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def get_role(self):
        return "Intern"
