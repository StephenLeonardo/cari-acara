from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

app_name = 'events'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'users', views.UserViewSet)
router.register('eventcategories', views.EventCategoryViewSet)
router.register('categories', views.CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('', views.EventList.as_view(), name='list'),  
    # path('create/', views.EventCreate.as_view(), name='create'),
    # path('detail/<str:pk>/', views.EventDetail.as_view(), name='detail'),
    # path('', views.event_list),
    # path('<int:pk>/', views.event_detail),
    # path('', views.EventList.as_view(), name='list'),
    # path('<int:pk>/', views.EventDetail.as_view()),
    # path('users/', views.UserList.as_view(), name='users'),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
    # path('test/', views.api_root),
    # path('<int:pk>/highlight/', views.EventHighlight.as_view()),
]

# 
# 
# 
# from .views import EventViewSet, UserViewSet, api_root
# from rest_framework import renderers
# 
# event_list = EventViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# event_detail = EventViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# event_highlight = EventViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
# 
# 
# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('events/', event_list, name='event-list'),
#     path('events/<int:pk>/', event_detail, name='event-detail'),
#     path('events/<int:pk>/highlight/', event_highlight, name='event-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])