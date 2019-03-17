from django.shortcuts import render
from .models import Bid_desk

# Create your views here.
def post_list(request):
    bid_desks=Bid_desk.objects.order_by('name')
    return render(request, 'auction/post_list.html', {'bid_desks':bid_desks})
