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
    hotel = Hotel.objects.get(status="Live", slug=slug)
    room_type = RoomType.objects.get(hotel=hotel, slug=rt_slug)
    rooms = Room.objects.filter(room_type=room_type, is_available=True)

    id = request.GET.get("hotel-id")
    checkin = request.GET.get("checkin")
    checkout = request.GET.get("checkout")
    adult = request.GET.get("adult")
    children = request.GET.get("children")
    room_type_=request.GET.get("room-type")

    print("checkin ======", checkin)

    if not all([checkin, checkout]):
        messages.warning(request, "Please enter your booking data to check availability.")
        return redirect("booking:booking_data", hotel.slug)

    context= {
        "hotels":hotel,
        "room_type":room_type,
        "rooms":rooms,
        "checkin": checkin,
        "checkout": checkout,
        "adult": adult,
        "children":children,
        "room_type_":room_type_,
    }
    return render(request, "hotel/room_type_detail.html", context)


def selected_rooms(request):
    # request.session.pop('selection_data_obj', None)

    total = 0
    room_count = 0
    total_days = 0
    adult = 0 
    children = 0 
    checkin = "0" 
    checkout = "" 
    children = 0 
    
    if 'selection_data_obj' in request.session:

        for h_id, item in request.session['selection_data_obj'].items():
                
            id = int(item['hotel_id'])
            hotel_id = int(item['hotel_id'])

            checkin = item["checkin"]
            checkout = item["checkout"]
            adult = int(item["adult"])
            children = int(item["children"])
            room_type_ = item["room_type"]
            room_id = int(item["room_id"])
            
            room_type = RoomType.objects.get(id=room_type_)

            date_format = "%Y-%m-%d"
            checkin_date = datetime.strptime(checkin, date_format)
            checout_date = datetime.strptime(checkout, date_format)
            time_difference = checout_date - checkin_date
            total_days = time_difference.days

            room_count += 1
            days = total_days
            price = room_type.price

            room_price = price * room_count
            total = room_price * days
            
            hotel = Hotel.objects.get(id=id)

        print("hotel ===", hotel)
        context = {
            "data":request.session['selection_data_obj'], 
            "total_selected_items": len(request.session['selection_data_obj']),
            "total":total,
            "total_days":total_days,
            "adult":adult,
            "children":children,   
            "checkin":checkin,   
            "checkout":checkout,   
            "hotel":hotel,   
        }

        return render(request, "hotel/selected_rooms.html", context)
    else:
        messages.warning(request, "You don't have any room selections yet!")
        return redirect("/")
