from django.db import models

# Create your models here.

class Ads(models.Model):
	account_code = models.PositiveBigIntegerField()
	account_name = models.TextField()
	campaign_code = models.PositiveBigIntegerField()
	currency = models.TextField()
	cost = models.FloatField()
	conversions = models.FloatField()
	impressions = models.FloatField()
	clicks = models.IntegerField()
	account_timezone = models.TextField()
	network_type = models.TextField()
	timestamp = models.DateTimeField()



# import datetime
# device = Devices(account_code=8696941810,
# account_name="MIA Clothings",
# campaign_code=9715444785,
# currency="GBP",
# cost=345,
# conversions=1,
# impressions=222,
# clicks=47,
# account_timezone="(GMT+00:00) Etc/GMT",
# network_type="google",
# timestamp=datetime.datetime.strptime("2022-12-19T22:28:06Z", "%Y-%m-%dT%H:%M:%S%z"))
# Devices.save()



