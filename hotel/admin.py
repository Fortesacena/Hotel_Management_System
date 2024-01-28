from django.contrib import admin
from hotel.models import Hotel, Booking, Room, RoomType

class HotelAdmin(admin.ModelAdmin):
    # inlines = [HotelGallery_Tab, HotelFeatures_Tab, RoomType_Tab ,Room_Tab, HotelFAQs_Tab]
    # search_fields = ['user__username', 'name']
    # list_filter = ['featured', 'status']
    # list_editable = ['status']
    list_display = ['thumbnail' ,'user',  'name', 'status', 'featured' ,'views']
    # list_per_page = 100
    prepopulated_fields = {"slug": ("name", )}



# Register your models here.
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(RoomType)
