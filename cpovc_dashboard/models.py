from django.db import models


class TestData(models.Model):
    """Test data."""

    dcount = models.IntegerField(default=0)
    exit_reason = models.CharField(max_length=150)
    agency = models.CharField(max_length=20)

    class Meta:
        """Override some params."""

        db_table = 'test_report'
        verbose_name = 'Test Report'
        verbose_name_plural = 'Test Reports'

    def __unicode__(self):
        """To be returned by admin actions."""
        return '%s' % (self.agency)
