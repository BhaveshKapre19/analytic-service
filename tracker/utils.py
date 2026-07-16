from user_agents import parse

def get_client_ip(request):
    """
    Extracts the true client IP from the Django request.
    Handles X-Forwarded-For if behind a proxy (like Nginx/Load Balancer).
    Falls back to REMOTE_ADDR.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # X-Forwarded-For can be a comma-separated list of IPs.
        # The first one is the original client IP.
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def parse_user_agent(user_agent_string):
    """
    Parses the raw user_agent string and returns a dictionary of
    browser and device properties.
    """
    user_agent = parse(user_agent_string)
    
    return {
        'browser': user_agent.browser.family,
        'browser_version': user_agent.browser.version_string,
        'operating_system': user_agent.os.family,
        'device_type': 'Mobile' if user_agent.is_mobile else ('Tablet' if user_agent.is_tablet else ('PC' if user_agent.is_pc else 'Unknown')),
        'device_brand': user_agent.device.brand,
        'device_model': user_agent.device.model,
        'is_mobile': user_agent.is_mobile,
        'is_tablet': user_agent.is_tablet,
        'is_pc': user_agent.is_pc,
    }
