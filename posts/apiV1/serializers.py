from rest_framework import serializers
from ..models import Posts,Comments


POST_DETAIL = serializers.HyperlinkedIdentityField("posts-api:post-detail",lookup_field="pk")
POST_DELETE = serializers.HyperlinkedIdentityField("posts-api:post-delete",lookup_field="pk")
POST_UPDATE = serializers.HyperlinkedIdentityField("posts-api:post-update",lookup_field="pk")

COMMENT_DELETE_UPDATE=serializers.HyperlinkedIdentityField("posts-api:comment-edit",lookup_field="pk")

class PostListSerializer(serializers.ModelSerializer):
    post_detail = POST_DETAIL
    post_delete = POST_DELETE
    post_update = POST_UPDATE
    user = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    class Meta:
        model=Posts
        fields=["post_detail","post_delete","post_update","user","title","content","comment_count","created_date"]

    def get_user(self,obj):
        return (obj.user.username)

    def get_comment_count(self,obj):
        return (obj.comments_set.all().count())

class PostDetailSerailizer(serializers.ModelSerializer):
    post_delete = POST_DELETE
    post_update = POST_UPDATE
    user = serializers.SerializerMethodField()
    comments =serializers.SerializerMethodField()
    class Meta:
        model=Posts
        fields=["post_update","post_delete","user","title","content","comments","created_date"]

    def get_user(self,obj):
        return obj.user.username

    def get_comments(self,obj):
     #   return obj.comments_set.all() böyle yaparsan hata alırsın
        return CommentListSerializer(obj.comments_set.all(),many=True).data

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Posts
        fields=["user","title","content"]

    def get_user(self,obj):
        return obj.user.username

class CommentListSerializer(serializers.ModelSerializer):
    comment_update = COMMENT_DELETE_UPDATE
    user = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = ["user","post","content","comment_update"]

    def get_user(self,obj):
        return obj.user.username

    def get_post(self,obj):
        return obj.post.title

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields=["post","content"]


class CommentDeleteUpdateSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()
    
    #def get_initial(self):
    #    super(CommentDeleteUpdateSerializer, self).get_initial()
    
    #def create(self, validated_data):
    #    super(CommentDeleteUpdateSerializer, self).create()
    
    #def save(self, **kwargs):
    #    super(CommentDeleteUpdateSerializer, self).save()

    class Meta:
        model = Comments
        fields=["user","post","content"]

    def get_user(self, obj):
        return obj.user.username

    def get_post(self, obj):
        return obj.post.title






