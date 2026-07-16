from django.db import models

class Visitor(models.Model):
    website_name = models.CharField(max_length=255)
    visitor_ip = models.GenericIPAddressField()
    
    # Optional Location
    country = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    # Device and Browser Information (parsed from User-Agent)
    browser = models.CharField(max_length=100, null=True, blank=True)
    browser_version = models.CharField(max_length=50, null=True, blank=True)
    operating_system = models.CharField(max_length=100, null=True, blank=True)
    device_type = models.CharField(max_length=50, null=True, blank=True)
    device_brand = models.CharField(max_length=100, null=True, blank=True)
    device_model = models.CharField(max_length=100, null=True, blank=True)
    
    is_mobile = models.BooleanField(default=False)
    is_tablet = models.BooleanField(default=False)
    is_pc = models.BooleanField(default=False)
    
    # Raw Data
    user_agent = models.TextField()
    language = models.CharField(max_length=50, null=True, blank=True)
    screen_resolution = models.CharField(max_length=50, null=True, blank=True)
    timezone = models.CharField(max_length=100, null=True, blank=True)
    referrer = models.URLField(max_length=1024, null=True, blank=True)
    current_page = models.CharField(max_length=1024, null=True, blank=True)
    
    # Tracking
    session_id = models.CharField(max_length=255, null=True, blank=True)
    visit_timestamp = models.DateTimeField(auto_now_add=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.visitor_ip} on {self.website_name} at {self.visit_timestamp}"

    class Meta:
        ordering = ['-visit_timestamp']
