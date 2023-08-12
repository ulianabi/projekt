from django.contrib import admin
from .models import Advertisement
from django.db.models.query import QuerySet


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auctin', 'created_date', 'updated_date']
    list_filter = ['auctin', 'creted_at', 'price']
    actions = ['make_action_as_false', 'make_action_as_true']
    fieldsets = (
        ('Общие', { # блок 1
            "fields": (
                'title', 'description'     # поля блока
            ),
        }),
        ('Финансы', {  # блок 1
            "fields": (
                'price', 'auctin'  # поля блока
            ),
        }),
    )



    @admin.action(description='Убрать возможность торга')
    def make_action_as_false(self, request, queryset: QuerySet):
        queryset.update(auctin=False)

    @admin.action(description='Добавить возможность торга')
    def make_action_as_true(self, request, queryset: QuerySet):
        queryset.update(auctin=True)

admin.site.register(Advertisement, AdvertisementAdmin)
