# Generated by Django 4.1.7 on 2023-03-27 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_category_equipment_delete_camera_delete_coder_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категории', 'verbose_name_plural': 'Категория'},
        ),
        migrations.AlterField(
            model_name='equipment',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='api.category', verbose_name='Категория'),
        ),
    ]
