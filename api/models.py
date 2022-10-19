from django.db import models

# Create your models here.

class Company(models.Model):
	company_name = models.CharField(max_length = 100, null=True)
	description =  models.TextField(null=True)
	logo = models.ImageField()
	# advocate = models.ManyToManyField(Advocate)

	def __str__(self):
		return self.company_name


class Advocate(models.Model):
	name = models.CharField(max_length = 100, null=True)
	short_bio = models.CharField(max_length = 100, null=True)
	long_bio = models.TextField(null=True)
	advocate_years_exp = models.IntegerField(null=True)
	profile_pic = models.ImageField()
	date_added = models.DateTimeField(auto_now_add=True)
	company = models.ManyToManyField(Company)

	def __str__(self):
		return self.name

class SocialMediaLinks(models.Model):
	advocate = models.ForeignKey(Advocate, on_delete=models.CASCADE, related_name='social_links')
	youtube = models.URLField(max_length=1000)
	github = models.URLField(max_length=1000)
	twitter = models.URLField(max_length=1000)

class Companies(models.Model):
	name = models.ForeignKey(Company, on_delete=models.CASCADE)
	advocate = models.ForeignKey(Advocate, on_delete = models.CASCADE)