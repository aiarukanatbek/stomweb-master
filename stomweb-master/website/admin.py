from django.contrib import admin
from .models import prof_information
from .models import lt_service
from .models import id16200422
from .models import medical_card
from .models import appointment

# Register your models here.
admin.site.register(prof_information)
admin.site.register(lt_service)
admin.site.register(id16200422)
admin.site.register(medical_card)
admin.site.register(appointment)