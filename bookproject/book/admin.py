from django.contrib import admin
from .models import SampleModel,Book,Review

admin.site.register(SampleModel)
admin.site.register(Book)
admin.site.register(Review)
