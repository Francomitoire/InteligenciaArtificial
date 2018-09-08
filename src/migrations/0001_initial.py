# Generated by Django 2.0.7 on 2018-09-02 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('number', models.CharField(blank=True, default='2.1', max_length=5)),
                ('floor', models.IntegerField(blank=True, default=1)),
                ('direction', models.CharField(default='French 628 puerko', max_length=100)),
                ('feature', models.CharField(default='python', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
