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
            'int x = 150; int y = 450;': 3,
            'int x = 100; int y = 500;': 2,
            'int x = 150; int y = 350;': 2,
            'int x = 200; int y = 350;': 1,
            'int x = 175; int y = 275;': 1,
            'int x = 300; int y = 300;': 1,
        })

    def render(self):
        return self.getChoice('onCanvasPosition')

class OffCanvasPositions(Decision):
    def registerChoices(self):
        self.addChoice('offCanvasPosition', {
            'int x = 50; int y = 50;': 1,
            'int x = 75; int y = 100;': 1,
            'int x = 60; int y = 550;': 1,
            'int x = 25; int y = 550;': 1,
            'int x = 700; int y = 575;': 1,
            'int x = 750; int y = 520;': 1,
        })

    def render(self):
        return self.getChoice('offCanvasPosition')