from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from .models import Visitor
from .serializers import VisitorSerializer
from .utils import get_client_ip, parse_user_agent

class RecordVisitView(APIView):
    def post(self, request):
        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            visitor_ip = get_client_ip(request)
            user_agent_data = parse_user_agent(request.data.get('user_agent', ''))
            
            serializer.save(
                visitor_ip=visitor_ip,
                **user_agent_data
            )
            return Response({"success": True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DashboardSummaryView(APIView):
    def get(self, request):
        today = timezone.now().date()
        
        # Total Visits
        total_visits = Visitor.objects.count()
        
        # Visits Today
        visits_today = Visitor.objects.filter(visit_timestamp__date=today).count()
        
        # Unique IPs (All time)
        unique_visitors = Visitor.objects.values('visitor_ip').distinct().count()
        
        return Response({
            "total_visits": total_visits,
            "visits_today": visits_today,
            "unique_visitors": unique_visitors
        })

class DashboardLatestView(APIView):
    def get(self, request):
        latest = Visitor.objects.all()[:10]
        data = [
            {
                "id": v.id,
                "website": v.website_name,
                "ip": v.visitor_ip,
                "country": v.country,
                "browser": v.browser,
                "device": v.device_type,
                "timestamp": v.visit_timestamp
            } for v in latest
        ]
        return Response(data)

class DashboardWebsitesView(APIView):
    def get(self, request):
        stats = Visitor.objects.values('website_name').annotate(
            total_visits=Count('id'),
            unique_ips=Count('visitor_ip', distinct=True)
        ).order_by('-total_visits')
        
        return Response(stats)
