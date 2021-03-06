from rest_framework import serializers

from affiliates.models import AffiliateEntity, AffiliateMembership, AffiliateInvite


class AffiliateEntitySerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()

    class Meta:
        model = AffiliateEntity

    def get_country(self, obj):
        return str(obj.country)


class AffiliateMembershipSerializer(serializers.ModelSerializer):
    member = serializers.SerializerMethodField()

    class Meta:
        model = AffiliateMembership

    def get_member(self, obj):
        return {
            'username': obj.member.username,
            'email': obj.member.email,
        }


class AffiliateInviteSerializer(serializers.ModelSerializer):
    readable_invited_at = serializers.SerializerMethodField()

    class Meta:
        model = AffiliateInvite

    def get_readable_invited_at(self, obj):
        # Example: January 12, 2018
        return obj.invited_at.strftime('%B %d, %Y')
