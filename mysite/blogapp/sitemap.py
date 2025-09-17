from django.contrib.sitemaps import Sitemap

from .models import Article


class BlogSitemap(Sitemap):
    changefreg = "never"
    priority = 0.5

    def items(self):
        return (
            Article.objects
            .filter(pub_date__isnull=False)
            .select_related("author", "category")
            .prefetch_related("tags")
            .order_by("-pub_date")
        )

    def lastmod(self, obj: Article):
        return obj.pub_date
