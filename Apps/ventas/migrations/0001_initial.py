# Generated by Django 4.1.1 on 2022-10-28 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administracion', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=100, unique=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('producto', models.ManyToManyField(to='administracion.producto')),
            ],
        ),
        migrations.CreateModel(
            name='CartProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.producto')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='producto',
            field=models.ManyToManyField(through='ventas.CartProducts', to='administracion.producto'),
        ),
    ]