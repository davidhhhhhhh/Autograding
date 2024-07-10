from ideaToText import Decision

class InitialPositionHelloWorld(Decision):
    def registerChoices(self):
        self.addChoice('initialPointLocation', {
            '{OnCanvasPositions}': 3,
            '{OffCanvasPositions}': 1
        })

    def render(self):
        return self.getChoice('initialPointLocation')

class OnCanvasPositions(Decision):
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

class OffCanvasPositions(Decision):
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