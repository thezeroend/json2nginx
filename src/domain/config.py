class Route:
    def __init__(self, path, modifier=None, directives=None):
        self.path = path
        self.modifier = modifier
        self.directives = directives if directives else []
