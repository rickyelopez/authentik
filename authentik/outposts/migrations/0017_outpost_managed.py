# Generated by Django 3.2.4 on 2021-06-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_outposts", "0016_alter_outpost_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="outpost",
            name="managed",
            field=models.TextField(
                default=None,
                help_text="Objects which are managed by authentik. These objects are created and updated automatically. This is flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.",
                null=True,
                unique=True,
                verbose_name="Managed by authentik",
            ),
        ),
    ]
