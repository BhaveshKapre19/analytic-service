from django.urls import path
from .views import (
    RecordVisitView,
    DashboardSummaryView,
    DashboardLatestView,
    DashboardWebsitesView
)

urlpatterns = [
    path('analytics/visit/', RecordVisitView.as_view(), name='record-visit'),
    path('dashboard/summary/', DashboardSummaryView.as_view(), name='dashboard-summary'),
    path('dashboard/latest/', DashboardLatestView.as_view(), name='dashboard-latest'),
    path('dashboard/websites/', DashboardWebsitesView.as_view(), name='dashboard-websites'),
]
