# Generated by Django 3.0.5 on 2020-04-29 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20200427_1119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': '技能', 'verbose_name_plural': '技能'},
        ),
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name': '社交', 'verbose_name_plural': '社交'},
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_precent',
            field=models.CharField(default='%', max_length=50, verbose_name='百分比'),
        ),
        migrations.AlterField(
            model_name='social',
            name='social_icon',
            field=models.CharField(default='fas fa-envelope', max_length=50, verbose_name='社交图标'),
        ),
    ]
