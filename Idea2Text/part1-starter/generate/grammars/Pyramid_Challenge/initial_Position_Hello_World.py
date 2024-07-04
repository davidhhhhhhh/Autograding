from ideaToText import Decision

class Initial_Position_Hello_World(Decision):
    def registerChoices(self):
        self.addChoice('initialPointLocation', {
            '{On_Canvas_Positions}': 3,
            '{Off_Canvas_Positions}': 1
        })

    def render(self):
        return self.expand('initialPointLocation')

class On_Canvas_Positions(Decision):
    def registerChoices(self):
        self.addChoice('onCanvasPosition', {
            'int x = 50; int y = 50;': 3,
            'int x = 100; int y = 100;': 2,
            'int x = 150; int y = 150;': 2,
            'int x = 200; int y = 50;': 1,
            'int x = 75; int y = 75;': 1,
            'int x = 300; int y = 100;': 1,
        })

    def render(self):
        return self.getChoice('onCanvasPosition')

class Off_Canvas_Positions(Decision):
    def registerChoices(self):
        self.addChoice('offCanvasPosition', {
            'int x = -50; int y = -50;': 1,
            'int x = -100; int y = -100;': 1,
            'int x = -150; int y = -150;': 1,
            'int x = -200; int y = -50;': 1,
            'int x = -75; int y = -75;': 1,
            'int x = -300; int y = -100;': 1,
        })

    def render(self):
        return self.getChoice('offCanvasPosition')