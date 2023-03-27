from django.contrib import admin

from api.models import Equipment, Feedback, Category


@admin.register(Equipment)
class FeedbackAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class FeedbackAdmin(admin.ModelAdmin):
    pass


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'phone_number', 'email']
    list_max_show_all = 10
    ordering = ["-created_time"]
