
from django.urls import path,include
from rest_framework import routers 
from api import views

router = routers.DefaultRouter()
router2 = routers.DefaultRouter()
router.register(r'', views.companyViewsets)
router2.register(r'', views.EmployeeViewSets)

urlpatterns = [
    path('companies/', include(router.urls)),
    path('employees/', include(router2.urls))
]
# companies/{companies_id}/employees