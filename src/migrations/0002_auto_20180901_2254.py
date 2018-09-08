# Generated by Django 2.0.7 on 2018-09-02 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('number', models.CharField(blank=True, default='2.1', max_length=5)),
                ('floor', models.IntegerField()),
                ('direction', models.CharField(default='French 628 puerko', max_length=100)),
                ('feature', models.CharField(default='Capacidad: 30 personas', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
