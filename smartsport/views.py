"""
    Author      : Sathish Kumar(sathishkumarb1139@gmail.com)
    Version     : 1.0
    Description : File contains the View Set (Returns the API Results)
"""

from rest_framework import viewsets
from smartsport.models import Series, Tournament
from smartsport.serializers import TournamentSerializer, SeriesSerializer
from rest_framework.permissions import IsAuthenticated


class SeriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Series to be viewed or edited.
    """
    permission_classes = [IsAuthenticated] # User Should atleast provide his/her username and password
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tournaments to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]  # User Should atleast provide his/her username and password
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
