# Generated by Django 3.1 on 2020-08-26 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('image', models.ImageField(upload_to='cases/', verbose_name='Картинка')),
                ('image_cell', models.ImageField(upload_to='cases/cells/', verbose_name='Картинка ячейки')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('cost', models.IntegerField(verbose_name='Стоимость')),
                ('level', models.IntegerField(verbose_name='Уровень')),
                ('experience', models.IntegerField(verbose_name='Опыт')),
                ('prizes', models.TextField(default='[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', verbose_name='Призы')),
            ],
            options={
                'verbose_name': 'Кейс',
                'verbose_name_plural': 'Кейсы',
            },
        ),
    ]