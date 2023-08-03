
from django.utils import timezone
import datetime
import uuid


from django.db import models


class CPOVC_HES(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    employment_status = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    type_of_employment=models.CharField(
        max_length=50,

        blank=True,
        null=True
    )
    health_scheme=models.CharField(
        max_length=50,

        blank=True,
        null=True
    )
    health_scheme_type = models.CharField(
        max_length=50,

        blank=True,
        null=True
    )
    kitchen_garden = models.CharField(
        max_length=50,

        blank=True,
        null=True
    )
    social_safety_nets = models.CharField(
        max_length=50,

        blank=True,
        null=True
    )
    social_safety_nets_type = models.CharField(
        max_length=50,

        blank=True,
        null=True
    )
    linkage_to_vsls = models.CharField(
        max_length=50,

        blank=True,
        null=True
    )
    vsla = models.CharField(
        max_length=50,

        blank=True,
        null=True
    )
    date_of_linkage_to_vsla = models.DateField(blank=True, null=True)
    monthly_saving_average = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    average_cumulative_saving = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    loan_taken = models.CharField(
        max_length=50,

        blank=True,
        null=True
    )
    loan_taken_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    date_loan_taken = models.DateField(blank=True, null=True)
    loan_utilization = models.CharField(max_length=100, blank=True, null=True)
    startup = models.CharField(max_length=100, blank=True, null=True)
    type_of_startup = models.CharField(max_length=100, blank=True, null=True)
    date_startup_received = models.DateField(blank=True, null=True)
    emergency_cash_transfer = models.CharField(
        max_length=50,

        blank=True,
        null=True
    )
    amount_received_ect = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    use_of_ect = models.CharField(max_length=100, blank=True, null=True)
    received_startup_kit = models.CharField(
        max_length=50,

        blank=True,
        null=True
    )
    type_of_asset = models.CharField(max_length=100, blank=True, null=True)
    average_monthly_income_generated = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    received_business_grant = models.CharField(
        max_length=50,

        blank=True,
        null=True
    )
    amount_of_money_received = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    business_type_started = models.CharField(max_length=100, blank=True, null=True)
    linked_to_value_chain_activities_asset_growth = models.CharField(max_length=100, blank=True, null=True)
    sector_of_asset_growth = models.CharField(max_length=100, blank=True, null=True)
    linked_to_source_finance = models.CharField(max_length=100, blank=True, null=True)
    type_of_financial_institution = models.CharField(max_length=100, blank=True, null=True)
    loan_taken_income_growth = models.CharField(
        max_length=50,

        blank=True,
        null=True
    )
    date_loan_taken_income_growth = models.DateField(blank=True, null=True)
    linked_to_value_chain_activities_income_growth= models.CharField(max_length=100, blank=True, null=True)
    sector_of_income_growth = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        db_table = 'cpovc_hes'
        verbose_name = "CPOVS_HES"
        verbose_name_plural = "CPOVS_HES"
        app_label = "cpovc_hes"










