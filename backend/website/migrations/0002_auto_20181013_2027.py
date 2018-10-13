# Generated by Django 2.1.2 on 2018-10-13 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotFriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steam_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('steam_id', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bot',
            name='account',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bot',
            name='password',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bot',
            name='steam_id',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='bot',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='website.Bot'),
        ),
        migrations.AddField(
            model_name='botfriend',
            name='bot',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='website.Bot'),
        ),
        migrations.AddField(
            model_name='bot',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='website.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='friend',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='website.BotFriend'),
        ),
    ]
