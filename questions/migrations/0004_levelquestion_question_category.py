# Generated by Django 2.0.4 on 2018-04-29 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20180426_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='levelquestion',
            name='question_category',
            field=models.IntegerField(choices=[('', '---------'), (1, 'comprehension'), (2, 'vocabulary'), (3, 'grammar')], default=1),
            preserve_default=False,
        ),
    ]
