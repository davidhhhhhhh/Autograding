from ideaToText import Decision

class Draw_Block_Hello_World(Decision):
    def registerChoices(self):
        self.addChoice('rectangleOrientation', {
            '{Standing_Rectangle}': 1,
            '{Lying_Down_Rectangle}': 1
        })

    def render(self):
        return self.expand('rectangleOrientation')

class Standing_Rectangle(Decision):
    def registerChoices(self):
        self.addChoice('standingRectangleSize', {
            'GRect rect = new GRect(x, y, 50, 100);': 3,
            'GRect rect = new GRect(x, y, 75, 150);': 2,
            'GRect rect = new GRect(x, y, 100, 200);': 1,
        })

    def render(self):
        return self.getChoice('standingRectangleSize')

class Lying_Down_Rectangle(Decision):
    def registerChoices(self):
        self.addChoice('lyingDownRectangleSize', {
            'GRect rect = new GRect(x, y, 100, 50);': 3,
            'GRect rect = new GRect(x, y, 150, 75);': 2,
            'GRect rect = new GRect(x, y, 200, 100);': 1,
        })

    def render(self):
        return self.getChoice('lyingDownRectangleSize')