from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# A Shortcut to creating serializers to create set of fields and simple default implementation for the create and update
#  methods
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

# class SnippetSerializer(serializers.Serializer):
#     # Define the fields that need to be serialized or deserialized
#     # Note how the class is similar to form class using similar validation flags
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    # these are the methods called after serializer.save() function for either creation or modification of instances
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Snippet.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance

    # We can use ModelSerializer class as well to control how serializer should be displayed in certain circumstances.


    # To Test your serializer and model connection
    # python manage.py shell
    #
    # from snippets.models import Snippet
    # from snippets.serializers import SnippetSerializer
    # from rest_framework.renderers import JSONRenderer
    # from rest_framework.parsers import JSONParser
    #
    # snippet = Snippet(code='foo = "bar"\n')
    # snippet.save()
    #
    # snippet = Snippet(code='print "hello, world"\n')
    # snippet.save()
    #
    # serializer = SnippetSerializer(snippet)
    # serializer.data
    # # {'id': 2, 'title': u'', 'code': u'print "hello, world"\n', 'linenos': False, 'language': u'python', 'style': u'friendly'}
    # content = JSONRenderer().render(serializer.data)
    # content
    # # '{"id": 2, "title": "", "code": "print \\"hello, world\\"\\n", "linenos": false, "language": "python", "style": "friendly"}'
    #
    # import io
    #
    # stream = io.BytesIO(content)
    # data = JSONParser().parse(stream)
    #
    # serializer = SnippetSerializer(data=data)
    # serializer.is_valid()
    # # True
    # serializer.validated_data
    # # OrderedDict([('title', ''), ('code', 'print "hello, world"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
    # serializer.save()
    # # <Snippet: Snippet object>
    #
    # #TO Serialize Query set instead of model instances we add many = True in serializer argument.
    # serializer = SnippetSerializer(Snippet.objects.all(), many=True)
    # serializer.data
    # # [OrderedDict([('id', 1), ('title', u''), ('code', u'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', u''), ('code', u'print "hello, world"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', u''), ('code', u'print "hello, world"'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]
    #