from rest_framework import serializers

from commenting_app.models import Comment, Author


class AuthorSerializer:
    class Meta:
        model = Author
        fields = [
            "username"
        ]


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    author = serializers.CharField(source="author.username", read_only=True)
    created_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M', read_only=True)
    class Meta:
        model = Comment
        fields = [
            "id",
            "text",
            "likes",
            "author",
            "created_at",
            "replies",
            "head_comment",
            "file",
        ]

        read_only_fields = [
            "likes",
            "author",
            "created_at",
            "replies",
            "main_comment",
            "head_comment",

        ]

    def get_replies(self, obj):
        replies = Comment.objects.filter(main_comment=obj.id)
        serializer = CommentSerializer(replies, many=True)
        return serializer.data

    def create(self, validated_data):
        main_comment = self.context.get("main_comment")
        validated_data["main_comment"] = main_comment
        return super().create(validated_data)


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Author
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.pop('confirm_password', None)

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        return attrs

    def create(self, validated_data):
        user = Author.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user