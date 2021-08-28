from accounts.api.serializers import UserSerializerForFriendship
from accounts.services import UserService
from friendships.models import Friendship
from friendships.services import FriendshipService
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


<<<<<<< Updated upstream
class BaseFriendshipSerializer(serializers.Serializer):
    user = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
=======
class FollowingUserIdSetMixin:

    @property
    def following_user_id_set(self: serializers.ModelSerializer):
        if self.context['request'].user.is_anonymous:
            return {}
        if hasattr(self, '_cached_following_user_id_set'):
            return self._cached_following_user_id_set
        user_id_set = FriendshipService.get_following_user_id_set(
            self.context['request'].user.id,
        )
        setattr(self, '_cached_following_user_id_set', user_id_set)
        return user_id_set


# 可以通过 source=xxx 指定去访问每个 model instance 的 xxx 方法
# 即 model_instance.xxx 来获得数据
# https://www.django-rest-framework.org/api-guide/serializers/#specifying-fields-explicitly
class FollowerSerializer(serializers.ModelSerializer, FollowingUserIdSetMixin):
    user = UserSerializerForFriendship(source='from_user')
    # created_at = serializers.DateTimeField()
>>>>>>> Stashed changes
    has_followed = serializers.SerializerMethodField()

    def update(self, instance, validated_data):
        pass

<<<<<<< Updated upstream
    def create(self, validated_data):
        pass

    def get_user_id(self, obj):
        raise NotImplementedError

    def _get_following_user_id_set(self):
        if self.context['request'].user.is_anonymous:
            return {}
        if hasattr(self, '_cached_following_user_id_set'):
            return self._cached_following_user_id_set
        user_id_set = FriendshipService.get_following_user_id_set(
            self.context['request'].user.id,
        )
        setattr(self, '_cached_following_user_id_set', user_id_set)
        return user_id_set

    def get_has_followed(self, obj):
        return self.get_user_id(obj) in self._get_following_user_id_set()
=======
    def get_has_followed(self, obj):
        return obj.from_user_id in self.following_user_id_set
>>>>>>> Stashed changes

    def get_user(self, obj):
        user = UserService.get_user_by_id(self.get_user_id(obj))
        return UserSerializerForFriendship(user).data

<<<<<<< Updated upstream
    def get_created_at(self, obj):
        return obj.created_at
=======
class FollowingSerializer(serializers.ModelSerializer, FollowingUserIdSetMixin):
    user = UserSerializerForFriendship(source='to_user')
    # created_at = serializers.DateTimeField()
    has_followed = serializers.SerializerMethodField()
>>>>>>> Stashed changes


<<<<<<< Updated upstream
class FollowingSerializer(BaseFriendshipSerializer):
    def get_user_id(self, obj):
        return obj.to_user_id


class FollowerSerializer(BaseFriendshipSerializer):
    def get_user_id(self, obj):
        return obj.from_user_id
=======
    def get_has_followed(self, obj):
        return obj.to_user_id in self.following_user_id_set
>>>>>>> Stashed changes


class FriendshipSerializerForCreate(serializers.ModelSerializer):
    from_user_id = serializers.IntegerField()
    to_user_id = serializers.IntegerField()

    class Meta:
        model = Friendship
        fields = ('from_user_id', 'to_user_id')

    def validate(self, attrs):
        if attrs['from_user_id'] == attrs['to_user_id']:
            raise ValidationError({
                'message': 'from_user_id and to_user_id should be different'
            })
        return attrs

    def create(self, validated_data):
        from_user_id = validated_data['from_user_id']
        to_user_id = validated_data['to_user_id']
        return FriendshipService.follow(
            from_user_id=from_user_id,
            to_user_id=to_user_id,
<<<<<<< Updated upstream
        )
=======
        )


>>>>>>> Stashed changes
