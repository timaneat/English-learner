from django.db import models

class Word(models.Model):
    en = models.CharField(max_length=255, verbose_name="English")
    ru = models.CharField(max_length=255, verbose_name="Russian")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.en} - {self.ru}"
