from django.shortcuts import render

from hotel.models import  Hotel, Room, Booking, RoomType

def index(request):
    hotel = Hotel.objects.filter(status="Live")
    context = {
        "hotel":hotel
    }
    return render(request, "hotel/hotel.html", context)

def hotel_detail(request, slug):
    hotel = Hotel.objects.get(status="Live", slug=slug)
    context = {
        "hotel":hotel,
    }
    return render(request, "hotel/hotel_detail.html", context)

# def room_type_detail(request, slug, rt_slug):
#     hotel = Hotel.objects.get(status="Live", slug=slug)
#     room_type = RoomType.objects.get(hotel=hotel, slug=rt_slug)
#     rooms = Room.objects.filter(room_type=room_type, is_available=True)

#     id = request.GET.get("hotel-id")
#     adult = request.GET.get("adult")
#     children = request.GET.get("children")
#     room_type_ = request.GET.get("room-type")

