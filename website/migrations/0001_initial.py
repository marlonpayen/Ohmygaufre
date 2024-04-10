# Generated by Django 4.0.4 on 2024-04-10 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foodtruck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=20)),
                ('adresse', models.TextField()),
                ('numero_de_telephone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=80)),
                ('heure_d_ouverture', models.CharField(max_length=10)),
                ('heure_de_fermeture', models.CharField(max_length=10)),
                ('a_propos', models.TextField()),
                ('phrase_d_accroche', models.TextField()),
                ('proprietaires', models.TextField()),
                ('image_accueil', models.ImageField(upload_to='')),
                ('image_du_menu', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_de_publication', models.DateTimeField()),
                ('nom', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=80)),
                ('sujet', models.CharField(max_length=100)),
                ('contenu', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=5)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menuitems', to='website.menu')),
            ],
        ),
    ]
