# Generated by Django 4.2.7 on 2023-12-06 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pessoa_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acompanhamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_ligacao', models.DateField(db_index=True)),
                ('resultado_acompanhamento', models.CharField(max_length=100)),
                ('dat_inc', models.DateTimeField(auto_now_add=True)),
                ('dat_exc', models.DateTimeField(blank=True, null=True)),
                ('dat_aut', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=100)),
                ('sobrenome', models.CharField(db_index=True, max_length=100)),
                ('idade', models.IntegerField()),
                ('telefone', models.CharField(db_index=True, max_length=15)),
                ('escolha_acompanhamento', models.CharField(max_length=100)),
                ('dat_inc', models.DateTimeField(auto_now_add=True)),
                ('dat_exc', models.DateTimeField(blank=True, null=True)),
                ('dat_aut', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnderecoDosCadastros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
                ('cep', models.CharField(max_length=9)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(db_index=True, max_length=100)),
                ('estado', models.CharField(db_index=True, max_length=2)),
                ('dat_inc', models.DateTimeField(auto_now_add=True)),
                ('dat_exc', models.DateTimeField(blank=True, null=True)),
                ('dat_aut', models.DateTimeField(blank=True, null=True)),
                ('cadastro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enderecos', to='core.cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='Integracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_integracao', models.DateField(db_index=True)),
                ('resultado', models.CharField(max_length=100)),
                ('notas', models.TextField()),
                ('dat_inc', models.DateTimeField(auto_now_add=True)),
                ('dat_exc', models.DateTimeField(blank=True, null=True)),
                ('dat_aut', models.DateTimeField(blank=True, null=True)),
                ('cadastro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='integracoes', to='core.cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='Movimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco_evento', models.CharField(max_length=255)),
                ('data_evento', models.DateField(db_index=True)),
                ('observacoes', models.TextField()),
                ('dat_inc', models.DateTimeField(auto_now_add=True)),
                ('dat_exc', models.DateTimeField(blank=True, null=True)),
                ('dat_aut', models.DateTimeField(blank=True, null=True)),
                ('cadastro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimentos', to='core.cadastro')),
            ],
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
        migrations.AddField(
            model_name='acompanhamento',
            name='cadastro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acompanhamentos', to='core.cadastro'),
        ),
    ]
