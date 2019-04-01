"""
    Author      : Sathish Kumar(sathishkumarb1139@gmail.com)
    Version     : 1.0
    Description : Data Serializer & Deserializer for Models which makes it simple
"""

from rest_framework import serializers
from smartsport.models import Series, Tournament


class SeriesSerializer(serializers.ModelSerializer):

    """ API Serializer for Series Model """
    id = serializers.IntegerField(read_only=False)
    class Meta:
        model = Series
        fields = ('id', 'name', 'date_start', 'date_end')

class TournamentSerializer(serializers.ModelSerializer):

    """ API Serializer for Tournament Model """
    series = SeriesSerializer(many=True, read_only=False, partial=True)
    id = serializers.IntegerField(read_only=False)
    class Meta:
        model = Tournament
        fields = ('id', 'series', 'city', 'country','name', 'date_start', 'date_end')

    def update(self, instance, validated_data):
        series = validated_data.pop('series', [])
        instance = super().update(instance, validated_data)
        for series_data in series:
            seris = Series.objects.get(pk=series_data.get('id'))
            seris.name = series_data.get('name')
            seris.date_start = series_data.get('date_start')
            seris.date_end = series_data.get('date_end')
            seris.save()
            instance.series.add(seris)
            instance.save()
        return instance
