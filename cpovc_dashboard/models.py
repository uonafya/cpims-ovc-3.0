from django.db import models
from cpovc_forms.models import RegOrgUnit


class IPInfo(models.Model):
    """IP and agency linkages. Parent == 2(DCS) means is IP"""

    agency = models.IntegerField(
        default=1, choices=[(1, 'USAID'), (2, 'CDC'), (3, 'DOD')])
    parent_unit = models.ForeignKey(
        RegOrgUnit, on_delete=models.CASCADE, related_name='ip')
    org_unit = models.ForeignKey(
        RegOrgUnit, on_delete=models.CASCADE, related_name='lip')
    targets = models.TextField(max_length=250, null=True, blank=True)
    fyear = models.IntegerField(default=2022)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override some params."""

        db_table = 'report_ip'
        verbose_name = 'IP Report'
        verbose_name_plural = 'IP Reports'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s : %s' % (self.agency, self.org_unit)


class COPTarget(models.Model):
    """IP and agency linkages. Parent == 2(DCS) means is IP"""

    agency_id = models.IntegerField(
        default=1, choices=[
            (1, 'USAID'), (2, 'CDC'), (3, 'DOD'), (4, 'PC'), (5, 'State/AF')])
    agency = models.CharField(max_length=100)
    mech = models.ForeignKey(
        RegOrgUnit, null=True, blank=True, on_delete=models.CASCADE)
    mechanism = models.CharField(max_length=255)
    county_id = models.IntegerField()
    county = models.CharField(max_length=100)
    hiv_burden = models.CharField(
        default='Low', max_length=10,
        choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    ovc_serv = models.IntegerField(default=0, null=True, blank=True)
    ovc_serv_under_1 = models.IntegerField(default=0, null=True, blank=True)
    ovc_serv_1_9 = models.IntegerField(default=0, null=True, blank=True)
    ovc_serv_10_14 = models.IntegerField(default=0, null=True, blank=True)
    ovc_serv_15_17 = models.IntegerField(default=0, null=True, blank=True)
    ovc_serv_18_24 = models.IntegerField(default=0, null=True, blank=True)
    ovc_serv_coarse = models.IntegerField(default=0, null=True, blank=True)
    ovc_serv_uk = models.IntegerField(default=0, null=True, blank=True)
    ovc_serv_active = models.IntegerField(default=0, null=True, blank=True)
    ovc_serv_graduated = models.IntegerField(default=0, null=True, blank=True)
    ovc_serv_over_18 = models.IntegerField(default=0, null=True, blank=True)
    ovc_serv_under_18 = models.IntegerField(default=0, null=True, blank=True)
    tx_curr = models.IntegerField(default=0, null=True, blank=True)
    tx_curr_under_1 = models.IntegerField(default=0, null=True, blank=True)
    tx_curr_1_9 = models.IntegerField(default=0, null=True, blank=True)
    tx_curr_10_14 = models.IntegerField(default=0, null=True, blank=True)
    tx_curr_15_19 = models.IntegerField(default=0, null=True, blank=True)
    fyear = models.IntegerField(default=2022)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override some params."""

        db_table = 'report_cop_targets'
        verbose_name = 'COP Target'
        verbose_name_plural = 'COP Targets'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s : %s' % (self.agency_id, self.mechanism)
