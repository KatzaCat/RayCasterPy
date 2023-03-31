
class Level:
    def __init__(self, file, size_x, size_y):
        self.file = file
        
        self.level = self.init_level()
        self.size_x = size_x
        self.size_y = size_y

    def init_level(self):
        rv = []
        with open(self.file, "r") as file:
            rv = file.read()
            rv = rv.replace(" ", "")
            rv = rv.replace("\n", "")

        return rv