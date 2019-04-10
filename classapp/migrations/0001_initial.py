# Generated by Django 2.1.4 on 2018-12-06 05:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Adviser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoardParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.Board')),
            ],
        ),
        migrations.CreateModel(
            name='Chatmember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Chatrecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('secret', models.BooleanField(default=False)),
                ('password', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.Board')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Groupmember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('contents', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('view_count', models.IntegerField(default=0)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.Board')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='writer_p',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.Professor'),
        ),
        migrations.AddField(
            model_name='post',
            name='writer_s',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.Student'),
        ),
        migrations.AddField(
            model_name='groupmember',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.Student'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='writer_p',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.Professor'),
        ),
        migrations.AddField(
            model_name='comment',
            name='writer_s',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.Student'),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='manager_p',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.Professor'),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='manager_s',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.Student'),
        ),
        migrations.AddField(
            model_name='chatrecord',
            name='chatroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.Chatroom'),
        ),
        migrations.AddField(
            model_name='chatrecord',
            name='member_p',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.Professor'),
        ),
        migrations.AddField(
            model_name='chatrecord',
            name='member_s',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.Student'),
        ),
        migrations.AddField(
            model_name='chatmember',
            name='chatroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.Chatroom'),
        ),
        migrations.AddField(
            model_name='chatmember',
            name='member_p',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.Professor'),
        ),
        migrations.AddField(
            model_name='chatmember',
            name='member_s',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.Student'),
        ),
        migrations.AddField(
            model_name='boardparticipant',
            name='professor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.Professor'),
        ),
        migrations.AddField(
            model_name='boardparticipant',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.Student'),
        ),
        migrations.AddField(
            model_name='board',
            name='group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classapp.Group'),
        ),
        migrations.AddField(
            model_name='adviser',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.Professor'),
        ),
        migrations.AddField(
            model_name='adviser',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='groupmember',
            unique_together={('group', 'student')},
        ),
        migrations.AlterUniqueTogether(
            name='adviser',
            unique_together={('professor', 'student')},
        ),
    ]
