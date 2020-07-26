from django.db import models


class Home(models.Model):
    TYPES_OF_HOMES = [
        ('SingleFamily', ''),
        ('VacantResidentialLand', 'Vacant Land'),
        ('Miscellaneous', 'Miscellaneous'),
        ('MultiFamily2To4', 'Multi Family'),
        ('Condominium', 'Condo'),
        ('Apartment', 'Apartment'),
        ('Duplex', 'Duplex')
    ]

    # System Generated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Data Fields
    area_unit = models.TextField(blank=True, verbose_name='Area Unit')
    bathrooms = models.FloatField(blank=True, null=True, verbose_name='Number of Bathrooms')
    bedrooms = models.IntegerField(blank=True, null=True, verbose_name='Number of Bedrooms')
    home_size = models.IntegerField(blank=True, null=True, verbose_name='House Size')
    home_type = models.CharField(blank=True, null=True, max_length=50, choices=TYPES_OF_HOMES, verbose_name='Home Type')
    last_sold_date = models.DateField(blank=True, null=True, verbose_name='Last Sold Date')
    last_sold_price = models.IntegerField(blank=True, null=True, verbose_name='Last Sold Price')
    link = models.URLField(blank=True, verbose_name='Link')
    price = models.IntegerField(blank=True, null=True, verbose_name='Price $')
    property_size = models.IntegerField(blank=True, null=True, verbose_name='Property Size')
    rent_price = models.IntegerField(blank=True, null=True, verbose_name='Rent Price')
    rentzestimate_amount = models.IntegerField(blank=True, null=True)
    rentzestimate_last_updated = models.DateField(blank=True, null=True)
    tax_value = models.FloatField(blank=True, null=True, verbose_name='Tax Value')
    tax_year = models.IntegerField(blank=True, null=True, verbose_name='Tax Year')
    year_built = models.IntegerField(blank=True, null=True, verbose_name='Year Built')
    zestimate_amount = models.IntegerField(blank=True, null=True)
    zestimate_last_updated = models.DateField(blank=True, null=True)
    zillow_id = models.IntegerField(unique=True, blank=True, null=True, verbose_name='Zillow ID')
    address = models.TextField(blank=True, verbose_name='Address')
    city = models.TextField(blank=True, verbose_name='City')
    state = models.TextField(blank=True, verbose_name='State')
    zipcode = models.CharField(blank=True, max_length=5, verbose_name='Zip Code')