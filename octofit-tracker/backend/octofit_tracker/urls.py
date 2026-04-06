import os
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.http import JsonResponse
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet

def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    base_url = f'https://{codespace_name}-8000.app.github.dev' if codespace_name != 'localhost' else 'http://localhost:8000'
    return JsonResponse({
        'users': f'{base_url}/api/users/',
        'teams': f'{base_url}/api/teams/',
        'activities': f'{base_url}/api/activities/',
        'leaderboards': f'{base_url}/api/leaderboards/',
        'workouts': f'{base_url}/api/workouts/',
    })

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboards', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]
