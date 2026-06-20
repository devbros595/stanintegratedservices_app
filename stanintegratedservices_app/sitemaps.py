# stanintegratedservices_app/sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # Match these exact names with your path names in urls.py
        return ['index', 'about', 'services', 'why_choose_us', 'contact']

    def location(self, item):
        return reverse(item)