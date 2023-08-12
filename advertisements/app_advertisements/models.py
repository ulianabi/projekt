from django.db import models

from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html


class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auctin = models.BooleanField("торг", help_text="Отметьте, если торг уместен", default=False)
    creted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='дата создания')
    def created_date(self):
        if self.creted_at.date() == timezone.now().date():
            created_time = self.creted_at.time().strftime('%H: %M: %S')  # 19:30:15
            return format_html(
                "<span style='color:green; font-weight: bold'>Сегодня в {}</span>",
                created_time
            )
        return self.creted_at.strftime('%d.%m.%Y at %H: %M: %S')  # 12.08.2023 at 22:09:15

    @admin.display(description='дата обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H: %M: %S')  # 19:30:15
            return format_html(
                "<span style='color:green; font-weight: bold'>Сегодня в {}</span>",
                updated_time
            )
        return self.updated_at.strftime('%d.%m.%Y at %H: %M: %S')





    def __str__(self) -> str:
        return f"Advertisements(id = {self.id}, title = {self.title}, price = {self.price})"

    class Meta:
        db_table = 'advertisements'  # переименование таблицы

# from app_advertisements.models import Advertisements
