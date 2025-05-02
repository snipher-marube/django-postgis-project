from django.contrib.gis.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    point = models.PointField()  # Using PostGIS Point field for geospatial data

    def __str__(self):
        return self.name
