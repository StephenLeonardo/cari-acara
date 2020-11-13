from .models import Event, Category, EventCategory
from rest_framework import serializers

from django.contrib.auth import get_user_model
User = get_user_model()




class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class EventCategorySerializer(serializers.ModelSerializer):
    # category = serializers.ReadOnlyField(source='category.name')
    category = CategorySerializer()
    class Meta:
        model = EventCategory
        # fields = '__all__'
        fields = ['category']

class EventCategoryMappingSerializer(serializers.ModelSerializer):
    event = serializers.CharField(source='event.name')
    category = serializers.CharField(source='category.name')
    class Meta:
        model = EventCategory
        fields = ['event', 'category']



class UserOnlySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EventSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    user = UserOnlySerializer()
    event_categories = EventCategorySerializer(many=True)
    # event_categories = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = ['id',
                'user',
                'created_at',
                'name',
                'description',
                'event_date',
                'event_time',
                'image',
                'event_categories']
            
    def create(self, validated_data):
        print("HAHAHHAHHAHAH")
                
    def validate_user(self, value):
        # The `validate` method is where we make sure that the current
        # instance of `LoginSerializer` has "valid". In the case of logging a
        # user in, this means validating that they've provided an email
        # and password and that this combination matches one of the users in
        # our database.
        
        user = User

        # The `validate` method should return a dictionary of validated data.
        # This is the data that is passed to the `create` and `update` methods
        # that we will see later on.
        return user
                


class EventNoUserSerializer(serializers.ModelSerializer):
    event_categories = EventCategorySerializer(many=True)
    # event_categories = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = ['id',
                'created_at',
                'name',
                'description',
                'event_date',
                'event_time',
                'image',
                'event_categories']
        


class UserSerializer(serializers.ModelSerializer):
    
    
    events = EventNoUserSerializer(many=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'events']
    
    
    # 
    # id = serializers.IntegerField(read_only=True)
    # created_at = serializers.DateTimeField(read_only=True)
    # name = serializers.CharField(required=True, allow_blank=False, max_length=255)
    # description = serializers.CharField(style={'base_template': 'textarea.html'})
    # event_date = serializers.DateField(required=False)
    # event_time = serializers.TimeField(required=False)
    # image = serializers.ImageField(allow_empty_file=True)
    # 
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Event.objects.create(**validated_data)
    # 
    # 
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.event_date = validated_data.get('event_date', instance.event_date)
    #     instance.event_time = validated_data.get('event_time', instance.event_time)
    #     instance.image = validated_data.get('image', instance.image)
    #     instance.save()
    #     return instance
    # 
    
    
    # class Meta:
    #     model = Event
    #     fields = ['id',
    #             'user',
    #             'created_at',
    #             'name',
    #             'description',
    #             'event_date',
    #             'event_time',
    #             'image']


        
        
