# Generated by Django 4.2.4 on 2023-11-03 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=4, unique=True, verbose_name='mbti')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255, verbose_name='上传类型')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app0.type', to_field='type')),
            ],
        ),
    ]