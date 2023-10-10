
from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image

PRIORITY_CHOICES = (
    ('1', 'Highest'),
    ('2', 'High'),
    ('3', 'Medium'),
    ('4', 'Low'),
    ('5', 'Lowest'),
)

STATUS_CHOICES = (
    ('1', 'Pending'),
    ('2', 'Proposed'),
    ('3', 'Interview'),
    ('4', 'Results won'),
    ('5', 'Results lost'),
    ('6', 'No resource'),
)

LEVEL_CHOICES = (
    ('1', 'Junior'),
    ('2', 'Senior'),
)

class Request(models.Model): #creation d'une requete
    title = models.CharField(max_length=100)
    reference_number = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    deadline = models.DateField()
    budget = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    priority = models.CharField(default='3', max_length=10, choices=PRIORITY_CHOICES)
    faction = models.CharField(max_length=100)
    consultant = models.CharField(max_length=100) #consultant assigné à la mission
    main_skills = models.CharField(max_length=100)  #skills du consultant (exemple : Java)
    consultant_level = models.CharField(default='1', max_length=10, choices=LEVEL_CHOICES)
    status = models.CharField(default='1', max_length=10, choices=STATUS_CHOICES)
    attachment = models.FileField(upload_to='public', null=True)
    date_requested = models.DateTimeField(default=timezone.now)
    #author = models.ForeignKey(User, on_delete=models.CASCADE) #reférence à une autre classe (clé étrangère)
    #on_delete=models.CASCADE --> signifie que lors de la suppression d'un User, tous ses Requests seront supprimés aussi

    def save(self, *args, **kwargs):  # method that runs after our model is saved --> méthode qui existe déjà mais on va la réécrire afin d'ajouter des fonctionnalités
        super(Request, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('request-detail', kwargs={'pk' : self.pk}) #redirige vers la page "Request-detail" et enregistre la clé primaire du nouveau Request