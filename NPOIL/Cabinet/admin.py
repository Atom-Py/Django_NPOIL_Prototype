from django.contrib import admin
from .models import Order, Requisition, PersonalInfo, Message, Response

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'status_bool', 'client', 'fuel', 'date', 'address']

@admin.register(Requisition)
class RequisitionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'status_bool', 'order']

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'status', 'subject', 'date', 'user']

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['__str__']