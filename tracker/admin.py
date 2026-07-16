from django.contrib import admin
from .models import Visitor

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('website_name', 'visitor_ip', 'browser', 'device_type', 'country', 'visit_timestamp')
    search_fields = ('visitor_ip', 'website_name', 'browser', 'country')
    list_filter = ('website_name', 'country', 'device_type', 'visit_timestamp')
    readonly_fields = ('visit_timestamp', 'created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('website_name', 'visitor_ip', 'session_id', 'visit_timestamp')
        }),
        ('Location', {
            'fields': ('country', 'region', 'city', 'latitude', 'longitude')
        }),
        ('Device & Browser', {
            'fields': (
                'browser', 'browser_version', 'operating_system', 
                'device_type', 'device_brand', 'device_model',
                'is_mobile', 'is_tablet', 'is_pc', 'screen_resolution'
            )
        }),
        ('Routing', {
            'fields': ('current_page', 'referrer', 'language', 'timezone', 'user_agent')
        }),
        ('System', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
