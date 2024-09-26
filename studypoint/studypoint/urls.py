
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from cms.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("filter/<int:topic_id>", filter, name="filter"),
    path("", homepage, name="homepage"),
    path("search/", search, name="search"),
    path("login/", loginView, name="login"),
    path("logout/", logoutView, name="logout"),
    path("register/", register, name="register"),
    path("show/<int:content_id>", showPost, name="show"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
