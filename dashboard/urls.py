"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'product.views.home', name='home'),
    url(r'category/(\d+)$', 'product.views.show_category', name='show_category'),
    url(r'products/(\d+)$', 'product.views.show_products', name='show_products'),
    url(r'compare/$', 'product.views.compare', name='compare'),
    url(r'overview/$', 'product.views.overview', name='overview'),
    url(r'best_tested/$', 'product.views.best_tested', name='best_tested'),
    url(r'supply_demand/$', 'product.views.supply_demand', name='supply_demand'),
    url(r'forum/$', 'product.views.forum', name='forum'),
    url(r'lake/$', 'product.views.lake', name='lake'),
    url(r'offers/(\d+)$', 'product.views.offers', name='offers'),
]
