# Generated by Django 3.2.4 on 2022-01-28 12:08

from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, unique=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('backgroud_image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='category-backgrounds')),
                ('is_delete', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='category.category')),
            ],
        ),
    ]
