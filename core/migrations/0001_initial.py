# Generated by Django 4.1.3 on 2022-11-30 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mercado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('rua', models.CharField(max_length=150)),
                ('bairro', models.CharField(max_length=150)),
                ('cidade', models.CharField(max_length=150)),
                ('avaliacao', models.CharField(blank=True, max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('categoria', models.CharField(blank=True, max_length=50, null=True)),
                ('quantidade', models.IntegerField(null=True)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('mercado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='produtos', to='core.mercado')),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=100)),
                ('capa', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image')),
                ('produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.produto')),
            ],
        ),
    ]