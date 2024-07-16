from django.contrib import admin
from .models import Worker, Store, Visit
# Register your models here.

class WorkerAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'phone_number',)

class StoreAdmin(admin.ModelAdmin):
    search_fields = ('title', )

class VisitAdmin(admin.ModelAdmin):
    fields = ('data_time', 'worker', 'store', 'latitude', 'longitude')
    search_fields = ['worker__full_name', 'store__title']


#     return f'{self.data_time} {self.worker} {self.store} {self.latitude} {self.longitude}'
admin.site.register(Worker,WorkerAdmin)
admin.site.register(Store,StoreAdmin,)
admin.site.register(Visit,VisitAdmin)
# ,Store, Visit,StoreAdminпоиск по имени Работника
# поиск по названию Торговой точк