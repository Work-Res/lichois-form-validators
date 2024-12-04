from django.db import models
from datetime import date
# from base_module.model_mixins import BaseUuidModel

class TestModel(models.Model):

    f1 = models.CharField(max_length=10)
    f2 = models.CharField(max_length=10)
    f3 = models.CharField(max_length=10, null=True, blank=False)
    f4 = models.CharField(max_length=10, null=True, blank=False)
    f5 = models.CharField(max_length=10)
    f5_other = models.CharField(max_length=10, null=True)


class Person(models.Model):

    first_name = models.CharField(max_length=190)

    last_name = models.CharField(max_length=190)

    middle_name = models.CharField(max_length=190, blank=True, null=True)

    maiden_name = models.CharField(max_length=190, blank=True, null=True)

    marital_status = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default='single',
    )

    dob = models.DateField(
        blank=True,
        null=True,
        # validations=date_not_future TODO: add validation (more than 18 years only )
    )

    gender = models.CharField(
        max_length=6,
        default='male',
        blank=True,
        null=True,
    )

    occupation = models.CharField(
        max_length=190,
        blank=True,
        null=True,
    )

    qualification = models.CharField(
        max_length=190,
        blank=True,
        null=True,
    )

    person_type = models.CharField(
        max_length=150,
        default="applicant",
    )

    deceased = models.BooleanField(default=False)

class Permit(models.Model):

    parent_object_id = models.UUIDField(
        null=True,
        blank=True,
        editable=False,
        help_text="Parent ID primary key.",
    )
    parent_object_type = models.CharField(max_length=200, null=True, blank=True)

    permit_type = models.CharField(max_length=190)
    permit_no = models.CharField(max_length=190)
    date_issued = models.DateField(default=date.today())
    date_expiry = models.DateField(null=True, blank=True)
    place_issue = models.CharField(max_length=190, null=True, blank=True)
    security_number = models.CharField(max_length=190, null=True, blank=True)
    applicant_type = models.CharField(
        max_length=200,
        default="applicant",
    )
    generated_pdf = models.FileField(upload_to="generated/", null=True, blank=True)
class VariationPermit(models.Model):
    existing_permit = models.ForeignKey(Permit, on_delete=models.CASCADE)
    expiry_date = models.DateField(default=date.today())
    current_company_name = models.CharField(max_length=250,null=True, blank=True)
    new_company_name = models.CharField(max_length=250,blank=True, null=True)
    new_company_location = models.CharField(max_length=250)
    has_separate_permises = models.CharField(max_length=10, default='yes')
    no_permises_reason = models.TextField(blank=True, null=True)
    new_company_services_provided = models.CharField(max_length=250, null=True, blank=True)

    current_employment_capacity = models.CharField(max_length=250,null=True, blank=True)
    upcoming_employment_capacity = models.CharField(max_length=250, null=True, blank=True)
    variation_for_same_employee = models.CharField(max_length=20, default='yes')
    understudies_situation = models.TextField(null=True, blank=True)

    draw_salary = models.CharField(max_length=10, default='yes')
    salary_per_annum = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    new_company_employee_count = models.IntegerField(blank=True, null=True)
    new_company_registration = models.DateField(blank=True, null=True)
    man_power_projection = models.TextField(blank=True, null=True)
    amount_invested = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    initial_capital_source = models.CharField(max_length=200, null=True, blank=True)
    financial_institution_name = models.CharField(max_length=250, null=True, blank=True)
    financial_institution_address = models.CharField(max_length=250, null=True, blank=True)

    subscriber = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)
    person_type = models.CharField(
        max_length=50, default="subscriber"
    )

    signature = models.CharField(max_length=150, null=True, blank=True)

    applicant_type = models.CharField(
        max_length=150, default="subscriber"
  )
