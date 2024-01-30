from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import datetime

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

def selected_rooms(request):
    total = 0
    room_count = 0
    total_days = 0
    adult = 0
    children = 0
    checkin = ""
    checkout = ""

    if 'selected_data_obj' in request.session:
        for h_id, item in request.session['session_data_obj'].items():
            id = int(item['hotel_id'])
            checkin = int(item['checkin'])
            checkout = int(item['checkout'])
            children = int(item['children'])
            room_type_ = int(item['room_type'])
            room_id = int(item['room_id'])

            room_type = RoomType.objects.get(id = room_type_)

            date_format = "%Y-%m-%d"
            checkin_date = datetime.strptime(checkin, date_format)
            checkout_date = datetime.strptime(checkout, date_format)
            time_difference = checkout_date - checkin_date
            total_days = time_difference.days

            print("checkin_date ========", checkin_date)
            print("checkout_date ========", checkout_date)
            print("total_days ========", total_days)
    else:
        messages.warning(request, "No selected room ")
        return redirect("/")
    return render(request, "hotel/selected_rooms.html")

