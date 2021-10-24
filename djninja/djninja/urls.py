from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from ninja import NinjaAPI

from project.viewsAPI.auth import api as auth_api
from project.viewsAPI.project import api as project_api
from project.viewsAPI.tasks import api as tasks_api


api = NinjaAPI()

api.add_router('auth/', auth_api)
api.add_router('project/', project_api)
api.add_router('task/', tasks_api)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', api.urls),
]
