from django.contrib import admin

from api.models import Camera, Feedback, Coder, Music, Light


# @admin.register(Camera)
# class CameraAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'quantity', "price"]
#     list_max_show_all = 10
#     ordering = ["-created_time"]
#
#
# @admin.register(Coder)
# class CoderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'quantity', "price"]
#     list_max_show_all = 10
#     ordering = ["-created_time"]
#
#
# @admin.register(Light)
# class LightAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'quantity', "price"]
#     list_max_show_all = 10
#     ordering = ["-created_time"]
#
#
# @admin.register(Music)
# class MusicAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'quantity', "price"]
#     list_max_show_all = 10
#     ordering = ["-created_time"]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'phone_number', 'email']
    list_max_show_all = 10
    ordering = ["-created_time"]
