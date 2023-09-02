from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    STATUS_CHOICES = (
        ('not_done', 'Не выполнено'),
        ('done', 'Выполнено'),
    )
    status = models.CharField(choices=STATUS_CHOICES, default='not_done', max_length=10)

    def __str__(self):
        return self.title

