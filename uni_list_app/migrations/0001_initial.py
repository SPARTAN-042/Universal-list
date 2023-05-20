# Generated by Django 4.2.1 on 2023-05-20 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('creation_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UniItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('uni_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_list_app.unilist')),
            ],
        ),
    ]