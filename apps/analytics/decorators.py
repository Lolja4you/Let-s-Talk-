from functools import wraps
from django.db.models import F
from django.db import transaction
from analytics.models import PageHit

def counted(f):

    @wraps(f)

    def decorator(request, *args, **kwargs):
        with transaction.atomic():
            counter = PageHit.objects.get_or_create(url=request.path)
            counter.count = F('count') + 1
            counter.save()
            print('qwwwwwwwwwwwwwwwwwwwww', counter)
        return f(request, *args, **kwargs)
    return decorator

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

