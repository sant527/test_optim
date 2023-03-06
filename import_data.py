import datetime

import csv
from ads.models import Ads
with open('./data_import_from_optim/Campaigns_Ads_Datast.csv') as file:
    reader = csv.reader(file)
    next(reader)  # Advance past the header

    Ads.objects.all().delete()

    for row in reader:
        print(row)
        
        ad = Ads(
            account_code=row[0],
            account_name=row[1],
            campaign_code=row[2],
            currency=row[3],
            cost=row[4],
            conversions=row[5],
            impressions=row[6],
            clicks=row[7],
            account_timezone=row[8],
            network_type=row[9],
            timestamp=datetime.datetime.strptime(row[10], "%Y-%m-%dT%H:%M:%S%z")
        )
        id_save = ad.save()
        print(id_save)
        