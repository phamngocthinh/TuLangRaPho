# Generated by Django 3.1.2 on 2020-11-24 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, db_column='create_time', null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='update_time', null=True)),
                ('create_user', models.IntegerField(blank=True, db_column='create_user', null=True)),
                ('update_user', models.IntegerField(blank=True, db_column='update_user', null=True)),
                ('delete_flag', models.IntegerField(blank=True, db_column='delete_flag', default=0)),
                ('image_path', models.CharField(db_column='image_path', max_length=100)),
            ],
            options={
                'db_table': 'blogs',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('create_time', models.DateTimeField(blank=True, db_column='create_time', null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='update_time', null=True)),
                ('create_user', models.IntegerField(blank=True, db_column='create_user', null=True)),
                ('update_user', models.IntegerField(blank=True, db_column='update_user', null=True)),
                ('delete_flag', models.IntegerField(blank=True, db_column='delete_flag', default=0)),
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('category_name', models.CharField(blank=True, db_column='category_name', max_length=250)),
                ('description', models.CharField(blank=True, db_column='description', max_length=200)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, db_column='create_time', null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='update_time', null=True)),
                ('create_user', models.IntegerField(blank=True, db_column='create_user', null=True)),
                ('update_user', models.IntegerField(blank=True, db_column='update_user', null=True)),
                ('delete_flag', models.IntegerField(blank=True, db_column='delete_flag', default=0)),
                ('image_path', models.CharField(blank=True, db_column='image_path', max_length=150)),
                ('category_id', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, db_column='create_time', null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='update_time', null=True)),
                ('create_user', models.IntegerField(blank=True, db_column='create_user', null=True)),
                ('update_user', models.IntegerField(blank=True, db_column='update_user', null=True)),
                ('delete_flag', models.IntegerField(blank=True, db_column='delete_flag', default=0)),
            ],
            options={
                'db_table': 'product_types',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='name', max_length=100, null=True)),
                ('enable', models.IntegerField(blank=True, db_column='enable', default=1, null=True)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, db_column='create_time', null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='update_time', null=True)),
                ('create_user', models.IntegerField(blank=True, db_column='create_user', null=True)),
                ('update_user', models.IntegerField(blank=True, db_column='update_user', null=True)),
                ('delete_flag', models.IntegerField(blank=True, db_column='delete_flag', default=0)),
                ('name', models.CharField(blank=True, db_column='name', max_length=100, null=True)),
                ('user_name', models.CharField(blank=True, db_column='user_name', max_length=50, null=True)),
                ('password', models.CharField(blank=True, db_column='password', max_length=50, null=True)),
                ('enable', models.IntegerField(blank=True, db_column='enable', default=1, null=True)),
                ('role_id', models.ForeignKey(db_column='role_id', on_delete=django.db.models.deletion.CASCADE, to='home.role')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='ProductTypeTranslate',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, db_column='create_time', null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='update_time', null=True)),
                ('create_user', models.IntegerField(blank=True, db_column='create_user', null=True)),
                ('update_user', models.IntegerField(blank=True, db_column='update_user', null=True)),
                ('delete_flag', models.IntegerField(blank=True, db_column='delete_flag', default=0)),
                ('lang_code', models.CharField(blank=True, db_column='lang_code', max_length=10)),
                ('type_name', models.CharField(blank=True, db_column='type_name', max_length=100)),
                ('description', models.CharField(blank=True, db_column='description', max_length=200)),
                ('type_id', models.ForeignKey(db_column='type_id', on_delete=django.db.models.deletion.CASCADE, to='home.producttype')),
            ],
            options={
                'db_table': 'product_type_translates',
            },
        ),
        migrations.CreateModel(
            name='ProductTranslate',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, db_column='create_time', null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='update_time', null=True)),
                ('create_user', models.IntegerField(blank=True, db_column='create_user', null=True)),
                ('update_user', models.IntegerField(blank=True, db_column='update_user', null=True)),
                ('delete_flag', models.IntegerField(blank=True, db_column='delete_flag', default=0)),
                ('lang_code', models.CharField(db_column='lang_code', default='', max_length=10)),
                ('product_name', models.CharField(blank=True, db_column='product_name', max_length=100)),
                ('description', models.CharField(blank=True, db_column='description', max_length=200)),
                ('product_id', models.ForeignKey(db_column='product_id', default=None, on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
            options={
                'db_table': 'product_translates',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_type_id',
            field=models.ForeignKey(blank=True, db_column='product_type_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='home.producttype'),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, db_column='create_time', null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='update_time', null=True)),
                ('create_user', models.IntegerField(blank=True, db_column='create_user', null=True)),
                ('update_user', models.IntegerField(blank=True, db_column='update_user', null=True)),
                ('delete_flag', models.IntegerField(blank=True, db_column='delete_flag', default=0)),
                ('discount', models.FloatField(blank=True, db_column='discount', null=True)),
                ('effected_start_date', models.DateTimeField(db_column='effected_start_date')),
                ('effected_end_date', models.DateTimeField(db_column='effected_end_date')),
                ('activation', models.IntegerField(db_column='activation', default=1)),
                ('product_id', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
            options={
                'db_table': 'discount',
            },
        ),
        migrations.CreateModel(
            name='CategoryTranslate',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, db_column='create_time', null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='update_time', null=True)),
                ('create_user', models.IntegerField(blank=True, db_column='create_user', null=True)),
                ('update_user', models.IntegerField(blank=True, db_column='update_user', null=True)),
                ('delete_flag', models.IntegerField(blank=True, db_column='delete_flag', default=0)),
                ('lang_code', models.CharField(db_column='lang_code', max_length=10)),
                ('category_name', models.CharField(blank=True, db_column='category_name', max_length=100)),
                ('description', models.CharField(blank=True, db_column='description', max_length=200)),
                ('category_id', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
            options={
                'db_table': 'category_translates',
            },
        ),
        migrations.CreateModel(
            name='BlogTranslate',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(blank=True, db_column='create_time', null=True)),
                ('update_time', models.DateTimeField(blank=True, db_column='update_time', null=True)),
                ('create_user', models.IntegerField(blank=True, db_column='create_user', null=True)),
                ('update_user', models.IntegerField(blank=True, db_column='update_user', null=True)),
                ('delete_flag', models.IntegerField(blank=True, db_column='delete_flag', default=0)),
                ('lang_code', models.CharField(db_column='lang_code', max_length=10)),
                ('title', models.CharField(db_column='title', max_length=100)),
                ('content', models.TextField(blank=True, db_column='content')),
                ('blog_id', models.ForeignKey(db_column='blog_id', on_delete=django.db.models.deletion.CASCADE, to='home.blog')),
            ],
            options={
                'db_table': 'blog_translates',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='product_id',
            field=models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='home.product'),
        ),
    ]
