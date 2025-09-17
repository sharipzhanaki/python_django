from django.core.management.base import BaseCommand
from blogapp.models import Author, Category, Tag


class Command(BaseCommand):
    """
    Create blog basics
    """
    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING("Create blog basics: Authors, Categories, Tags"))

        authors_data = [
            {"name": "Ivan Petrov", "bio": "Technical writer, DevOps and Infrastructure"},
            {"name": "John Smith", "bio": "Senior software engineer at Google"},
            {"name": "Anna Klochkova", "bio": "Java developer"},
        ]

        categories_data = [
            {"name": "Backend"},
            {"name": "Frontend"},
            {"name": "Fullstack"}
        ]

        tags_data = [
            {"name": "Golang"},
            {"name": "Java"},
            {"name": "Python"},
        ]

        for data in authors_data:
            author, created = Author.objects.get_or_create(
                name=data["name"],
                defaults={"bio": data["bio"]}
            )
            if not created:
                self.stdout.write(f"Author {author.name} already exists")
            else:
                self.stdout.write(f"Created author {author.name}")
        self.stdout.write(self.style.SUCCESS(f"Authors created."))

        for data in categories_data:
            category, created = Category.objects.get_or_create(
                name=data["name"],
            )
            if not created:
                self.stdout.write(f"Category {category.name} already exists")
            else:
                self.stdout.write(f"Created category {category.name}")
        self.stdout.write(self.style.SUCCESS(f"Categories created"))

        for data in tags_data:
            tag, created = Tag.objects.get_or_create(
                name=data["name"],
            )
            if not created:
                self.stdout.write(f"Tag {tag.name} already exists")
            else:
                self.stdout.write(f"Created tag {tag.name}")
        self.stdout.write(self.style.SUCCESS(f"Tags created"))
