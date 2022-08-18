from django.db import models


class CaseAlert(models.Model):
    """Model for managing Alerts."""

    alert_name = models.CharField(max_length=100)
    category_id = models.IntegerField(default=1)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override table details."""

        db_table = 'case_alert'
        verbose_name = 'Case Alert'
        verbose_name_plural = 'Case Alerts'
