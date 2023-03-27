from django.contrib import admin

from api.models import Camera, Feedback, Coder, Music, Light


@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    pass


@admin.register(Coder)
class CoderAdmin(admin.ModelAdmin):
    pass

@admin.register(Light)
class LightAdmin(admin.ModelAdmin):
    pass


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    pass


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'phone_number', 'email']
    list_max_show_all = 10
    ordering = ["-created_time"]
