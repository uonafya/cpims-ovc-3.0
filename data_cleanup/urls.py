"""Data cleanup section urls."""
from django.contrib.auth.decorators import login_required
from django.urls import path
# from django.conf.urls import patterns

from .views import DataQualityView, CasePlanDataQualityView

urlpatterns = [
    # 'data_cleanup.views',
    path('filter/', login_required(DataQualityView.as_view()), name='data_cleanup'),
    path('filter/case_plan', login_required( CasePlanDataQualityView.as_view()), name='data_cleanup_case_plan')
]
