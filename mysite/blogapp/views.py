from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.contrib.syndication.views import Feed

from .models import Article


class ArticlesListView(ListView):
    template_name = "blogapp/article_list.html"
    model = Article
    context_object_name = "articles"
    queryset = (
        Article.objects
        .filter(pub_date__isnull=False)
        .select_related("author", "category")
        .prefetch_related("tags")
        .defer("content")
        .order_by("-pub_date")
    )


class ArticleDetailView(DetailView):
    model = Article


class LatestArticlesFeed(Feed):
    title = "Blog articles (latest)"
    description = "updates on changed and addition blog articles"
    link = reverse_lazy("blogapp:article-list")

    def items(self):
        return (
            Article.objects
            .filter(pub_date__isnull=False)
            .select_related("author", "category")
            .prefetch_related("tags")
            .order_by("-pub_date")[:5]
        )

    def item_title(self, item: Article):
        return item.title

    def item_description(self, item: Article):
        return item.content[:200]

    # def item_link(self, item: Article):
    #     return reverse_lazy("blogapp:article-detail", kwargs={"pk": item.pk})
