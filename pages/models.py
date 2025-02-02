from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)  # Portfolio, Hizmetler, Takım vb.
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Content(models.Model):
    CONTENT_TYPES = [
        ('portfolio', 'Portfolio Card'),
        ('hero_slide', 'Hero Slayt'),
        ('service', 'Service'),
        ('team_member', 'Team Member'),
        ('clients', 'Clients'),
        ('comments', 'Comments'),
        ('features', 'Features'),
        ('blog', 'Blog'),
    ]
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.CharField(null=True,max_length=50, blank=False)
    extra_data = models.JSONField(blank=True, null=True)  # Ekstra alanlar için
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
