from rest_framework import serializers
from .models import Visitor

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        # We exclude fields that are determined server-side
        exclude = ['visitor_ip', 'browser', 'browser_version', 'operating_system', 'device_type', 'device_brand', 'device_model', 'is_mobile', 'is_tablet', 'is_pc', 'visit_timestamp', 'created_at', 'updated_at']

    def validate_website_name(self, value):
        if not value:
            raise serializers.ValidationError("website_name is required.")
        return value

    def validate_user_agent(self, value):
        if not value:
            raise serializers.ValidationError("user_agent is required.")
        return value
