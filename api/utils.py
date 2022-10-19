from rest_framework import serializers
from .models import Advocate, Company,Companies, SocialMediaLinks


class SocialMediaLinksSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SocialMediaLinks
		fields = ['youtube', 'github', 'twitter']


class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
	links = SocialMediaLinksSerializer(source='social_links', many=True)
	
	class Meta:
		model = Advocate
		fields = ('url','id','name','short_bio','long_bio','advocate_years_exp', 'profile_pic','date_added','company', 'links' )

class CompaniesSerializer(serializers.HyperlinkedModelSerializer):
	advocates = DeveloperSerializer(source='advocate_set', many=True)
	class Meta:
		model= Company
		fields = ('url', 'company_name','description', 'logo', 'advocates')


class CompSerializer(serializers.HyperlinkedModelSerializer):
	class Meta :
		model = Companies
		fields = ['url','name','advocate']
