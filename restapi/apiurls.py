from rest_framework.routers import SimpleRouter
from restapi.views import Bookopretions

simplerouters = SimpleRouter()
simplerouters.register('book',Bookopretions)
urlpatterns=simplerouters.urls
