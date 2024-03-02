# Generated by Django 3.2 on 2024-03-01 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.user'),
        ),
    ]