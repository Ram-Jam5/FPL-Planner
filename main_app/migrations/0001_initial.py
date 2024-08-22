# Generated by Django 5.1 on 2024-08-22 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('goalkeeper', models.CharField(choices=[('Martinez', ' Emiliano Martinez'), ('Henderson', 'Dean Henderson'), ('Pope', 'Nick Pope'), ('Raya', 'David Raya Martin'), ('Ederson', 'Ederson Santana de Moraes')], default='Martinez', max_length=50)),
                ('defender1', models.CharField(choices=[('Pedro Porro', 'Pedro Porro'), ('Alexander-Arnold', 'Trent Alexander-Arnold'), ('Gvardiol', 'Josko Gvardiol'), ('Martinez', 'Lissandro Martinez'), ('Saliba', 'William Salbia'), ('Virgil', 'Virgil Van Dijk'), ('Dunk', 'Lewis Dunk'), ('Konsa', 'Ezri Konsa Ngoyo'), ('Maguire', 'Harry Maguire'), ('Romero', 'Chrisitan Romero')], default='Pedro Porro', max_length=50)),
                ('defender2', models.CharField(choices=[('Pedro Porro', 'Pedro Porro'), ('Alexander-Arnold', 'Trent Alexander-Arnold'), ('Gvardiol', 'Josko Gvardiol'), ('Martinez', 'Lissandro Martinez'), ('Saliba', 'William Salbia'), ('Virgil', 'Virgil Van Dijk'), ('Dunk', 'Lewis Dunk'), ('Konsa', 'Ezri Konsa Ngoyo'), ('Maguire', 'Harry Maguire'), ('Romero', 'Chrisitan Romero')], default='Alexander-Arnold', max_length=50)),
                ('defender3', models.CharField(choices=[('Pedro Porro', 'Pedro Porro'), ('Alexander-Arnold', 'Trent Alexander-Arnold'), ('Gvardiol', 'Josko Gvardiol'), ('Martinez', 'Lissandro Martinez'), ('Saliba', 'William Salbia'), ('Virgil', 'Virgil Van Dijk'), ('Dunk', 'Lewis Dunk'), ('Konsa', 'Ezri Konsa Ngoyo'), ('Maguire', 'Harry Maguire'), ('Romero', 'Chrisitan Romero')], default='Gvardiol', max_length=50)),
                ('defender4', models.CharField(choices=[('Pedro Porro', 'Pedro Porro'), ('Alexander-Arnold', 'Trent Alexander-Arnold'), ('Gvardiol', 'Josko Gvardiol'), ('Martinez', 'Lissandro Martinez'), ('Saliba', 'William Salbia'), ('Virgil', 'Virgil Van Dijk'), ('Dunk', 'Lewis Dunk'), ('Konsa', 'Ezri Konsa Ngoyo'), ('Maguire', 'Harry Maguire'), ('Romero', 'Chrisitan Romero')], default='Martinez', max_length=50)),
                ('midfielder1', models.CharField(choices=[('De Bruyne', 'Kevin De Bruyne'), ('Gordon', 'Anthony Gordon'), ('Jota', 'Diogo Jota'), ('Maddison', 'James Maddison'), ('Bernardo', 'Bernardo Silva'), ('Garnacho', 'Alejandro Garnacho'), ('Rice', 'Declan Rice'), ('Salah', 'Mohammed Salah'), ('Saka', 'Bukayo Saka')], default='De Bruyne', max_length=50)),
                ('midfielder2', models.CharField(choices=[('De Bruyne', 'Kevin De Bruyne'), ('Gordon', 'Anthony Gordon'), ('Jota', 'Diogo Jota'), ('Maddison', 'James Maddison'), ('Bernardo', 'Bernardo Silva'), ('Garnacho', 'Alejandro Garnacho'), ('Rice', 'Declan Rice'), ('Salah', 'Mohammed Salah'), ('Saka', 'Bukayo Saka')], default='Gordon', max_length=50)),
                ('midfielder3', models.CharField(choices=[('De Bruyne', 'Kevin De Bruyne'), ('Gordon', 'Anthony Gordon'), ('Jota', 'Diogo Jota'), ('Maddison', 'James Maddison'), ('Bernardo', 'Bernardo Silva'), ('Garnacho', 'Alejandro Garnacho'), ('Rice', 'Declan Rice'), ('Salah', 'Mohammed Salah'), ('Saka', 'Bukayo Saka')], default='Jota', max_length=50)),
                ('forward1', models.CharField(choices=[('Haaland', 'Erling Haaland'), ('Isak', 'Alexander Isak'), ('Watkins', 'Ollie Watkins'), ('Wood', 'Chris Wood'), ('Vardy', 'Jamie Vardy'), ('Solanke', 'Dominic Solanke'), ('Toney', 'Ivan Toney')], default='Haaland', max_length=50)),
                ('forward2', models.CharField(choices=[('Haaland', 'Erling Haaland'), ('Isak', 'Alexander Isak'), ('Watkins', 'Ollie Watkins'), ('Wood', 'Chris Wood'), ('Vardy', 'Jamie Vardy'), ('Solanke', 'Dominic Solanke'), ('Toney', 'Ivan Toney')], default='Isak', max_length=50)),
                ('forward3', models.CharField(choices=[('Haaland', 'Erling Haaland'), ('Isak', 'Alexander Isak'), ('Watkins', 'Ollie Watkins'), ('Wood', 'Chris Wood'), ('Vardy', 'Jamie Vardy'), ('Solanke', 'Dominic Solanke'), ('Toney', 'Ivan Toney')], default='Watkins', max_length=50)),
            ],
        ),
    ]