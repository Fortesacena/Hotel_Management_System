from django.shortcuts import render

from hotel.models import  Hotel, Room, Booking, RoomType

def index(request):
    hotels = Hotel.objects.all()
    context = {
        "hotels":hotels
    }
    return render(request, "hotel/hotel.html", context)

def hotel_detail(request, slug):
    hotel = Hotel.objects.get(status="Live", slug=slug)
    context = {
        "hotel":hotel,
    }
    return render(request, "hotel/hotel_detail.html", context)

def room_type_detail(request, slug, rt_slug):
    hotels = Hotel.objects.get(status="Live", slug=slug)
    room_type = RoomType.objects.get(hotel=hotels, slug=rt_slug)
    rooms = Room.objects.filter(room_type=room_type, is_available=True)

    id = request.GET.get("hotel-id")
    checkin = request.GET.get("checkin")
    checkout = request.GET.get("checkout")
    adult = request.GET.get("adult")
    children = request.GET.get("children")

    context= {
        "hotels":hotels,
        "room_type":room_type,
        "rooms":rooms,
        "checkin": checkin,
        "checkout": checkout,
        "adult": adult,
        "children":children,
    }
    return render(request, "hotel/room_type_detail.html", context)

