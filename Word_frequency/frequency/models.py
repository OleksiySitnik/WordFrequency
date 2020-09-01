from django.db import models


class Text(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('text-details', args=[str(self.id)])

    def __str__(self):
            return self.text[:30] + "..." if len(self.text) > 30 else self.text


class Token(models.Model):
    word = models.TextField()
    frequency = models.PositiveIntegerField()
    text = models.ForeignKey(Text, related_name='tokens', on_delete=models.CASCADE)

    def __str__(self):
        return self.word