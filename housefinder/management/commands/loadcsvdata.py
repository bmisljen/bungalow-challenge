import csv
import datetime
from decimal import Decimal

from django.core.management.base import BaseCommand

from housefinder.models import Home

class Command(BaseCommand):
    help = 'Ingests house data from a CSV file'

    # Takes dates formatted in MM/DD/YY to Django model friendly format of yyyy-mm-dd
    def convert_date_format(self, input):
        if not input == '':
            output = datetime.datetime.strptime(input, '%m/%d/%Y').strftime('%Y-%m-%d')
            return output

    # Converts price format of $150k or $1.2M to 150000 and 12000000
    def convert_price_format(self, input):
        if not input[0:1] == '$':
            return None
        number_portion = Decimal(input[1:len(input) - 1])
        multiplier = input[len(input) - 1]

        if multiplier == 'K':
            return number_portion * 1000
        elif multiplier == 'M':
            return number_portion * 1000000

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)

    def handle(self, *args, **options):
        file_name = options['file']

        reader = csv.DictReader(open(file_name))
        num_houses = 0
        for row in reader:
            house = Home()
            house.area_unit = row['area_unit']
            if row['bathrooms']:
                house.bathrooms = row['bathrooms']
            if row['bedrooms']:
                house.bedrooms = row['bedrooms']
            if row['home_size']:
                house.home_size = row['home_size']
            if row['home_type']:
                house.home_type = row['home_type']
            if row['last_sold_date']:
                house.last_sold_date = self.convert_date_format(row['last_sold_date'])
            if row['last_sold_price']:
                house.last_sold_price = row['last_sold_price']
            if row['link']:
                house.link = row['link']
            if row['price']:
                house.price = self.convert_price_format(row['price'])
            if row['property_size']:
                house.property_size = row['property_size']
            if row['rent_price']:
                house.rent_price = row['rent_price']
            if row['rentzestimate_amount']:
                house.rentzestimate_amount = row['rentzestimate_amount']
            if row['rentzestimate_last_updated']:
                house.rentzestimate_last_updated = self.convert_date_format(row['rentzestimate_last_updated'])
            if row['tax_value']:
                house.tax_value = row['tax_value']
            if row['tax_year']:
                house.tax_year = row['tax_year']
            if row['year_built']:
                house.year_built = row['year_built']
            if row['zestimate_amount']:
                house.zestimate_amount = row['zestimate_amount']
            if row['zestimate_last_updated']:
                house.zestimate_last_updated = self.convert_date_format(row['zestimate_last_updated'])
            if row['zillow_id']:
                house.zillow_id = row['zillow_id']
            if row['address']:
                house.address = row['address']
            if row['city']:
                house.city = row['city']
            if row['state']:
                house.state = row['state']
            if row['zipcode']:
                house.zipcode = row['zipcode']

            house.save()
            num_houses += 1

        self.stdout.write(self.style.SUCCESS('Successfully ingested {} Houses from: {}'.format(num_houses, file_name)))