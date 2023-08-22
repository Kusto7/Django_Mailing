# Generated by Django 4.2.4 on 2023-08-22 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Cодержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Превью статьи')),
                ('article_date_creation', models.DateTimeField(auto_now_add=True)),
                ('publication', models.BooleanField(blank=True, default=True, null=True, verbose_name='Признак публикации')),
                ('views_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
