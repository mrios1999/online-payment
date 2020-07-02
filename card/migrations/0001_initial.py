# Generated by Django 3.0.6 on 2020-07-01 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0011_delete_cards'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=100)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
        ),
    ]