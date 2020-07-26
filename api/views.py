from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from housefinder.models import Home
from .serializers import HomeSerializer


class HomeViewSet(GenericViewSet,  # generic view functionality
                  CreateModelMixin,  # handles POSTs
                  RetrieveModelMixin,  # handles GETs for 1 Company
                  UpdateModelMixin,  # handles PUTs and PATCHes
                  ListModelMixin):  # handles GETs for many Companies):

    serializer_class = HomeSerializer

    def get_queryset(self):
        queryset = Home.objects.all()

        area_unit = self.request.query_params.get('area_unit', None)
        if area_unit is not None:
            queryset = queryset.filter(area_unit=area_unit)

        bathrooms = self.request.query_params.get('bathrooms', None)
        if bathrooms is not None:
            queryset = queryset.filter(bathrooms=bathrooms)

        bedrooms = self.request.query_params.get('bedrooms', None)
        if bedrooms is not None:
            queryset = queryset.filter(bedrooms=bedrooms)

        home_size = self.request.query_params.get('home_size', None)
        if home_size is not None:
            queryset = queryset.filter(home_size=home_size)

        home_type = self.request.query_params.get('home_type', None)
        if home_type is not None:
            queryset = queryset.filter(home_type=home_type)

        last_sold_date = self.request.query_params.get('last_sold_date', None)
        if last_sold_date is not None:
            queryset = queryset.filter(last_sold_date=last_sold_date)

        last_sold_price = self.request.query_params.get('last_sold_price', None)
        if last_sold_price is not None:
            queryset = queryset.filter(last_sold_price=last_sold_price)

        price = self.request.query_params.get('price', None)
        if price is not None:
            queryset = queryset.filter(price=price)

        property_size = self.request.query_params.get('property_size', None)
        if property_size is not None:
            queryset = queryset.filter(property_size=property_size)

        rent_price = self.request.query_params.get('rent_price', None)
        if rent_price is not None:
            queryset = queryset.filter(rent_price=rent_price)

        rentzestimate_amount = self.request.query_params.get('rentzestimate_amount', None)
        if rentzestimate_amount is not None:
            queryset = queryset.filter(rentzestimate_amount=rentzestimate_amount)

        rentzestimate_last_updated = self.request.query_params.get('rentzestimate_last_updated', None)
        if rentzestimate_last_updated is not None:
            queryset = queryset.filter(rentzestimate_last_updated=rentzestimate_last_updated)

        tax_value = self.request.query_params.get('tax_value', None)
        if tax_value is not None:
            queryset = queryset.filter(tax_value=tax_value)

        tax_year = self.request.query_params.get('tax_year', None)
        if tax_year is not None:
            queryset = queryset.filter(tax_year=tax_year)

        year_built = self.request.query_params.get('year_built', None)
        if year_built is not None:
            queryset = queryset.filter(year_built=year_built)

        zestimate_amount = self.request.query_params.get('zestimate_amount', None)
        if zestimate_amount is not None:
            queryset = queryset.filter(zestimate_amount=zestimate_amount)

        zestimate_last_updated = self.request.query_params.get('zestimate_last_updated', None)
        if zestimate_last_updated is not None:
            queryset = queryset.filter(zestimate_last_updated=zestimate_last_updated)

        zillow_id = self.request.query_params.get('zillow_id', None)
        if zillow_id is not None:
            queryset = queryset.filter(zillow_id=zillow_id)

        address = self.request.query_params.get('address', None)
        if address is not None:
            queryset = queryset.filter(address=address)

        city = self.request.query_params.get('city', None)
        if city is not None:
            queryset = queryset.filter(city=city)

        state = self.request.query_params.get('state', None)
        if state is not None:
            queryset = queryset.filter(state=state)

        zipcode = self.request.query_params.get('zipcode', None)
        if zipcode is not None:
            queryset = queryset.filter(zipcode=zipcode)

        return queryset
