# Generated by Django 4.2.5 on 2023-11-21 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("uploader", "0001_initial"),
        ("usuario", "0004_remove_usuario_foto"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuario",
            name="foto",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="uploader.image",
            ),
        ),
    ]
