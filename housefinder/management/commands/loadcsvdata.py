import csv
import datetime
from decimal import Decimal

from django.core.management.base import BaseCommand

from housefinder.models import Home

class Command(BaseCommand):
    help = 'Loads a CSV file with home data'

    # Format date to Django Model format of: yyyy-mm-dd
    def convertDate(self, dt):
        if not dt == '':
            new_date = datetime.datetime.strptime(dt, '%m/%d/%Y').strftime('%Y-%m-%d')
            return new_date

    # Format the price to show the exact price without K or M
    def convertPrice(self, price):
        if not price[0:1] == '$':
            return None

        # Get the price and the multiplier
        number = Decimal(price[1:len(price) - 1])
        multiplier = price[len(price) - 1]

        if multiplier == 'K':
            return number * 1000
        elif multiplier == 'M':
            return number * 1000000

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='The path to a .csv file containing homes')

    def handle(self, *args, **kwargs):
        file_name = kwargs['path']
        reader = csv.DictReader(open(file_name))
        homes_saved = 0

        for row in reader:
            home = Home()

            if row['area_unit']:
                home.area_unit = row['area_unit']
            if row['bathrooms']:
                home.bathrooms = row['bathrooms']
            if row['bedrooms']:
                home.bedrooms = row['bedrooms']
            if row['home_size']:
                home.home_size = row['home_size']
            if row['home_type']:
                home.home_type = row['home_type']
            if row['last_sold_date']:
                home.last_sold_date = self.convertDate(row['last_sold_date'])
            if row['last_sold_price']:
                home.last_sold_price = row['last_sold_price']
            if row['link']:
                home.link = row['link']
            if row['price']:
                home.price = self.convertPrice(row['price'])
            if row['property_size']:
                home.property_size = row['property_size']
            if row['rent_price']:
                home.rent_price = row['rent_price']
            if row['rentzestimate_amount']:
                home.rentzestimate_amount = row['rentzestimate_amount']
            if row['rentzestimate_last_updated']:
                home.rentzestimate_last_updated = self.convertDate(row['rentzestimate_last_updated'])
            if row['tax_value']:
                home.tax_value = row['tax_value']
            if row['tax_year']:
                home.tax_year = row['tax_year']
            if row['year_built']:
                home.year_built = row['year_built']
            if row['zestimate_amount']:
                home.zestimate_amount = row['zestimate_amount']
            if row['zestimate_last_updated']:
                home.zestimate_last_updated = self.convertDate(row['zestimate_last_updated'])
            if row['zillow_id']:
                home.zillow_id = row['zillow_id']
            if row['address']:
                home.address = row['address']
            if row['city']:
                home.city = row['city']
            if row['state']:
                home.state = row['state']
            if row['zipcode']:
                home.zipcode = row['zipcode']

            home.save()
            homes_saved += 1

        print('Successfully saved: ', homes_saved, 'homes')

