import uuid
from django.db import models
from django.utils import timezone
from cpovc_registry.models import RegPerson, RegOrgUnit
from cpovc_auth.models import AppUser





class CPOVC_HES(models.Model):
    person = models.ForeignKey(RegPerson, on_delete=models.CASCADE)
    cbo = models.ForeignKey(RegOrgUnit, on_delete=models.CASCADE)
    employment_status = models.CharField(max_length=50,null=False)
    type_of_employment = models.CharField(max_length=50, blank=True,null=True)
    health_scheme = models.CharField(max_length=50,null=False)
    health_scheme_type = models.CharField( max_length=50, blank=True,null=True)
    kitchen_garden = models.CharField(max_length=50,null=False)
    social_safety_nets = models.CharField( max_length=50,null=False)
    social_safety_nets_type = models.CharField(max_length=50,blank=True,null=True)
    linkage_to_vsls = models.CharField(max_length=50,null=False)
    vsla = models.CharField(max_length=50,blank=True,null=True)
    date_of_linkage_to_vsla = models.DateField(blank=True, null=True)
    monthly_saving_average = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True, default=0.0)
    average_cumulative_saving = models.DecimalField(max_digits=10,decimal_places=2, blank=True,null=True,default=0.00)
    loan_taken = models.CharField( max_length=50,blank=True,null=True)
    loan_taken_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)
    date_loan_taken = models.DateField(blank=True, null=True)
    loan_utilization = models.CharField(max_length=100, blank=True, null=True)
    startup = models.CharField(max_length=100, blank=True, null=True)
    type_of_startup = models.CharField(max_length=100, blank=True, null=True)
    date_startup_received = models.DateField(blank=True, null=True)
    emergency_cash_transfer = models.CharField(max_length=50, blank=True,null=True)
    amount_received_ect = models.DecimalField( max_digits=10, decimal_places=2, blank=True, null=True,default=0.00)
    use_of_ect = models.CharField(max_length=100, blank=True, null=True)
    received_startup_kit = models.CharField(max_length=50,blank=True, null=True)
    type_of_asset = models.CharField(max_length=100, blank=True, null=True)
    average_monthly_income_generated = models.DecimalField( max_digits=10,decimal_places=2,blank=True,null=True, default=0.00)
    received_business_grant = models.CharField(max_length=50,blank=True,null=True)
    amount_of_money_received = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True,default=0.00)
    business_type_started = models.CharField(max_length=100, blank=True, null=True)
    linked_to_value_chain_activities_asset_growth = models.CharField(max_length=100, blank=True, null=True)
    sector_of_asset_growth = models.CharField(max_length=100, blank=True, null=True)
    linked_to_source_finance = models.CharField(max_length=100, blank=True, null=True)
    type_of_financial_institution = models.CharField(max_length=100, blank=True, null=True)
    loan_taken_income_growth = models.CharField(max_length=50,blank=True,null=True)
    date_loan_taken_income_growth = models.DateField(blank=True, null=True)
    linked_to_value_chain_activities_income_growth = models.CharField(max_length=100, blank=True, null=True)
    sector_of_income_growth = models.CharField(max_length=100, blank=True, null=True)

    created_by = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True)

    created_at = models.DateField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        db_table = 'cpovc_hes_registration'
        verbose_name = "HouseHold Economic Strengthening"
        verbose_name_plural = "HouseHold Economic Strengthening"

    def __str__(self):
        return str(self.id)

