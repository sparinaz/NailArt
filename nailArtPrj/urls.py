"""
URL configuration for nailArtPrj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from nailApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view() , name='index'),
    path(
        "services/",
        ServiceListView.as_view(),
        name="service_list",
    ),
    path(
        "portfolio/",
        PortfolioListView.as_view(),
        name="portfolio_list",
    ),
    path(
        "blog/",
        BlogListView.as_view(),
        name="blog_list"
    ),
    path(
        "blog/<slug:slug>",
        BlogDetailView.as_view(),
        name="blog_detail"
    ),
    path(
            "blog/category/<slug:slug>/",
            CategoryBlogListView.as_view(),
            name="category_posts"
        ),
    path(
                "blog/tag/<slug:slug>/",
                TagBlogListView.as_view(),
                name="tag_posts"
            ),
            
    path(
        "about_us/",
        TemplateView.as_view(template_name="core/about_us.html"),
        name="about_us"
    ),
    path(
        "contact_us/",
        TemplateView.as_view(template_name="core/contact_us.html"),
        name="contact_us"
    )

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

