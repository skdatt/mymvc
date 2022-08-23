from rest_framework.routers import SimpleRouter
from student.views import studentoperation

simplerouter=SimpleRouter()
simplerouter.register('std',studentoperation)
urlpatterns=simplerouter.urls