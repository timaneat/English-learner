from django.db import models

class WordSet(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название набора")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Набор слов"
        verbose_name_plural = "Наборы слов"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

class Word(models.Model):
    word_set = models.ForeignKey(WordSet, on_delete=models.CASCADE, related_name='words', verbose_name="Набор", null=True, blank=True)
    en = models.CharField(max_length=255, verbose_name="English")
    ru = models.CharField(max_length=255, verbose_name="Russian")
    created_at = models.DateTimeField(auto_now_add=True)
    is_learned = models.BooleanField(default=False, verbose_name="Is learned")
    
    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.en} - {self.ru}"
