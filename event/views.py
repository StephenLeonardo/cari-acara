from .models import Event, Category, EventCategory
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (CategorySerializer,
                          EventSerializer,
                          EventCategorySerializer,
                          EventCategoryMappingSerializer,
                          UserSerializer)
from .permissions import IsOwnerOrReadOnly

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import Http404
from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework import generics

from rest_framework import permissions

from django.contrib.auth import get_user_model
User = get_user_model()


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


from rest_framework import renderers

class EventHighlight(generics.GenericAPIView):
    queryset = Event.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        event = self.get_object()
        return Response(event)


from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer



from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

class CategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        event = self.get_object()
        return Response(event.description)


    def create(self, validated_data):
        if '_mutable' in validated_data.data:
            validated_data.data._mutable = True
            
        print('huhuhuhuhuhuhu')
        print(validated_data.data)
        # validated_data.data['user'] = validated_data.user
        
        if 'user' in validated_data.data:
            print("OHOHOHOHOHOH")
            validated_data.data.pop('user')
        
        if 'user.email' in validated_data.data:
            validated_data.data.pop('user.email')
        
        if 'user.username' in validated_data.data:
            validated_data.data.pop('user.username')
            
        if 'csrfmiddlewaretoken' in validated_data.data:
            validated_data.data.pop('csrfmiddlewaretoken')
        
        
        categories = []
        if 'event_categories' in validated_data.data:
            categories = validated_data.data.pop('event_categories')
        
        print("XIXIXIXIX")
        
        event_date = None
        event_time = None
        
        # print(validated_data.data['event_date'])
        if validated_data.data['event_date'] == '':
            print('DISINI')
            validated_data.data['event_date'] = None
            
        else:
            print(validated_data.data['event_date'])
            
        if validated_data.data['event_time'] == '':
            print('DISANA')
            validated_data.data['event_time'] = None
        else:
            print(validated_data.data['event_time'])
            
        print(validated_data.data)
        
        event = Event.objects.create(user=validated_data.user, **validated_data.data)
        category_list = [] 
        for product_details in categories:
            # product_details['event'] = event.pk
            print(product_details)
            category = Category.objects.filter(pk=product_details)[0]
            category_list.append(EventCategory.objects.create(event=event,category=category))
        
        if '_mutable' in validated_data.data:
            validated_data.data._mutable = False
        return event
            
            
            
            
            
    def perform_create(self, serializer):
        print("HEEHHEHEHHEH")
        print(serializer['name'])
        serializer.save(user=self.request.user)
        serializer.save(event_categories=Category.objects.filter(pk__in=self.request.data['event_categories']))
        

class EventCategoryViewSet(viewsets.ModelViewSet):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategoryMappingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
                          