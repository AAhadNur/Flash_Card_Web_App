from django.contrib import admin

# Register your models here.

from cards.models import Card, Set


admin.site.register(Set)
admin.site.register(Card)
