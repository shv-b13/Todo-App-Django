# Generated by Django 2.1.7 on 2019-03-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('status', models.CharField(choices=[('active', 'active'), ('done', 'done'), ('cancled', 'cancled')], default='active', max_length=7)),
            ],
        ),
    ]
