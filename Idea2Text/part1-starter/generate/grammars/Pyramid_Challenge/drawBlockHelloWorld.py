from ideaToText import Decision

class DrawBlockHelloWorld(Decision):
    def registerChoices(self):
        self.addChoice('rectangleOrientation', {
            '{StandingRectangle}': 1,
            '{LyingDownRectangle}': 1
        })

    def render(self):
        return self.getChoice('rectangleOrientation')

class StandingRectangle(Decision):
    def registerChoices(self):
        self.addChoice('standingRectangleSize', {
            'GRect rect = new GRect(x, y, 50, 100);': 3,
            'GRect rect = new GRect(x, y, 75, 150);': 2,
            'GRect rect = new GRect(x, y, 100, 200);': 1,
        })

    def render(self):
        return self.getChoice('standingRectangleSize')

class LyingDownRectangle(Decision):
    def registerChoices(self):
        self.addChoice('lyingDownRectangleSize', {
            'GRect rect = new GRect(x, y, 100, 50);': 3,
            'GRect rect = new GRect(x, y, 150, 75);': 2,
            'GRect rect = new GRect(x, y, 200, 100);': 1,
        })

    def render(self):
        return self.getChoice('lyingDownRectangleSize')