from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView

from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("posts/", include("posts.urls")),
    # path("", RedirectView.as_view(url="posts/", permanent=False), name="index")

    path('cms_admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    re_path(r'', include(wagtail_urls)),
]
