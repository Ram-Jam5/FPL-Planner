from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
GOALKEEPERS = (
    ('Martinez', ' Emiliano Martinez'),
    ('Henderson', 'Dean Henderson'),
    ('Pope', 'Nick Pope'),
    ('Raya', 'David Raya Martin'),
    ('Ederson', 'Ederson Santana de Moraes')
    )

DEFENDERS = (
    ('Pedro Porro', 'Pedro Porro'),
    ('Alexander-Arnold', 'Trent Alexander-Arnold'),
    ('Gvardiol', 'Josko Gvardiol'),
    ('Martinez', 'Lissandro Martinez'),
    ('Saliba', 'William Salbia'),
    ('Virgil', 'Virgil Van Dijk'),
    ('Dunk', 'Lewis Dunk'),
    ('Konsa', 'Ezri Konsa Ngoyo'),
    ('Maguire', 'Harry Maguire'),
    ('Romero', 'Chrisitan Romero'),
)

MIDFIELDERS = (
    ('De Bruyne', 'Kevin De Bruyne'),
    ('Gordon', 'Anthony Gordon'),
    ('Jota', 'Diogo Jota'),
    ('Maddison', 'James Maddison'),
    ('Bernardo', 'Bernardo Silva'),
    ('Garnacho', 'Alejandro Garnacho'),
    ('Rice', 'Declan Rice'),
    ('Salah', 'Mohammed Salah'),
    ('Saka', 'Bukayo Saka'),
)

FORWARDS = (
    ('Haaland', 'Erling Haaland'),
    ('Isak', 'Alexander Isak'),
    ('Watkins', 'Ollie Watkins'),
    ('Wood', 'Chris Wood'),
    ('Vardy', 'Jamie Vardy'),
    ('Solanke', 'Dominic Solanke'),
    ('Toney', 'Ivan Toney'),
)


class Team(models.Model):
    name = models.CharField(max_length=100)
    goalkeeper = models.CharField(
        max_length=50,
        choices=GOALKEEPERS,
        default=GOALKEEPERS[0][0]
    )
    defender1 = models.CharField(
        max_length=50,
        choices=DEFENDERS,
        default=DEFENDERS[0][0],
    )
    defender2 = models.CharField(
        max_length=50,
        choices=DEFENDERS,
        default=DEFENDERS[1][0],
    )
    defender3 = models.CharField(
        max_length=50,
        choices=DEFENDERS,
        default=DEFENDERS[2][0],
    )
    defender4 = models.CharField(
        max_length=50,
        choices=DEFENDERS,
        default=DEFENDERS[3][0]
    )
    midfielder1 = models.CharField(
        max_length=50,
        choices=MIDFIELDERS,
        default=MIDFIELDERS[0][0]
    )
    midfielder2 = models.CharField(
        max_length=50,
        choices=MIDFIELDERS,
        default=MIDFIELDERS[1][0]
    )
    midfielder3 = models.CharField(
        max_length=50,
        choices=MIDFIELDERS,
        default=MIDFIELDERS[2][0]
    )
    forward1 = models.CharField(
        max_length=50,
        choices=FORWARDS,
        default=FORWARDS[0][0]
    )
    forward2 = models.CharField(
        max_length=50,
        choices=FORWARDS,
        default=FORWARDS[1][0]
    )
    forward3 = models.CharField(
        max_length=50,
        choices=FORWARDS,
        default=FORWARDS[2][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("teams-detail", kwargs={"teams_id": self.id})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    