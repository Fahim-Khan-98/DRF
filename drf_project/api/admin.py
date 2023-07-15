from django.contrib import admin
from api.models import Employee,Company
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','address')
    list_filter=('company',)

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Company,CompanyAdmin)
