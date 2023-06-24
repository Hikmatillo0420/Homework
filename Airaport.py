class Airport:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.planes = []
    def add_plane(self, plane):
        self.planes.append(plane)
    def remove_plane(self, plane):
        self.planes.remove(plane)
        # new value
        # skjfksjdfsf
        # hjdjskdhfkjsdhfjskdf