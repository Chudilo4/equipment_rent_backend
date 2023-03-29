from django.contrib import admin

from api.models import Equipment, Feedback, Category


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'phone_number', 'email']
    list_max_show_all = 10
    ordering = ["-created_time"]
