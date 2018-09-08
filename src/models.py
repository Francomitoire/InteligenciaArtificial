from django.db import models




class Classroom(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    number = models.CharField(blank=True, default='2.1', max_length=5)
    floor = models.IntegerField()
    direction = models.CharField(default='French 628 puerko', max_length=100)
    feature = models.CharField(default='Capacidad: 30 personas', max_length=100)

    class Meta:
        ordering = ('created',)

