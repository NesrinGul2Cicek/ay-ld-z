from matplotlib.path import Path
from shapely.geometry import Point, Polygon

class NoFlyZone:
    def __init__(self, id, coordinates, active_time):
        self.id = id
        self.coordinates = coordinates
        self.active_time = active_time
        self.polygon = Polygon(coordinates)