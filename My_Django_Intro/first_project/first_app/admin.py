from django.contrib import admin
from first_app.models import Topic,Website,AccessRecord
# Register your models here.

admin.site.register(Topic)
admin.site.register(Website)
admin.site.register(AccessRecord)
