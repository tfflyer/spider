# Generated by Django 2.0.6 on 2018-07-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_pub_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usname', models.CharField(max_length=8)),
                ('solotext', models.TextField(max_length=28, null=True)),
                ('upage', models.TimeField(auto_now=True)),
            ],
        ),
    ]
