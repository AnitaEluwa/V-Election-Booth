# Generated by Django 3.1.1 on 2020-09-29 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cla', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clatokens',
            name='token',
            field=models.CharField(blank=True, default='8cCyhJ8FF4PbgWJcTyzQqLVFKU8gA2KZ', max_length=32),
        ),
    ]