# Generated by Django 4.0.5 on 2022-06-09 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CommentsApp', '0003_alter_comment_deleted_at_alter_comment_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upvote',
            name='poster_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='CommentsApp.poster'),
        ),
    ]
