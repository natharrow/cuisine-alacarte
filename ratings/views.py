from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib.auth import get_user_model

from .models import ItemRating
from customer.models import Customer
from delivery_person.models import Delivery
from cook.models import Cook
from item.models import Item, Dish

@method_decorator([login_required], name='dispatch')
class UserRatingListView(ListView):
    model = ItemRating

    def get_queryset(self, **kwargs):
        querry_type = type(None)
        if(querry_type == type(None)):
            pass

class ItemRatingListView(ListView):
    model = ItemRating

    def get_queryset(self, **kwargs):
        print(self.kwargs['item_id'])
        print('\n\n\n\n\n')
        ritem = Item.objects.get(id=self.kwargs['item_id'])
        return ritem.itemrating_set.all()