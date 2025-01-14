# Generated by Django 2.0.2 on 2018-05-24 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=4)),
                ('symbol', models.CharField(max_length=10)),
                ('volume', models.FloatField(blank=True, null=True)),
                ('averagePrice', models.FloatField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name', 'symbol'),
            },
        ),
        migrations.CreateModel(
            name='BotDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('cash', models.FloatField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='botaction',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading.BotDetail'),
        ),
    ]
