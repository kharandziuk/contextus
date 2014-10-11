from marshmallow import Serializer, fields


class PostSerializer(Serializer):
    class Meta:
        fields = ('body',)
