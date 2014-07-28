import webbrowser

class Track():
    def __init__(self, t, d, i, v):
        self.title = t
        self.desc = d
        self.image = i
        self.video = v

    def showtrailer(self):
        webbrowser.open(self.video)

    def showposter(self):
        webbrowser.open(self.image)
