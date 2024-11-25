import os
import django
from django.urls import get_resolver

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

def list_urls():
    resolver = get_resolver()
    for pattern in resolver.url_patterns:
        try:
            print(pattern.pattern)
        except AttributeError:
            pass

if __name__ == '__main__':
    list_urls()