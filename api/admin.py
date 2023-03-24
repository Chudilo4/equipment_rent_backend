from django.contrib import admin

from api.models import Equipment, Feedback


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'quantity', "price"]
    list_max_show_all = 10
    ordering = ["-created_time"]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'phone_number', 'email']
    list_max_show_all = 10
    ordering = ["-created_time"]
