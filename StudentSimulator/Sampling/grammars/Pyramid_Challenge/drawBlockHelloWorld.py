from StudentSimulator.ideaToText import Decision

class DrawBlockHelloWorld(Decision):
    def registerChoices(self):
        self.addChoice('rectangleOrientation', {
            '{StandingRectangle}': 1,
            '{LyingDownRectangle}': 10
        })

    def render(self):
        return self.getChoice('rectangleOrientation')

class StandingRectangle(Decision):
    def registerChoices(self):
        self.addChoice('standingRectangleSize', {
            'GRect rect = new GRect(x, y, 10, 30);': 20,
            'GRect rect = new GRect(x, y, 40, 20);': 1,
            'GRect rect = new GRect(x, y, 100, 200);': 1,
        })

    def render(self):
        return self.getChoice('standingRectangleSize')

class LyingDownRectangle(Decision):
    def registerChoices(self):
        self.addChoice('lyingDownRectangleSize', {
            'GRect rect = new GRect(x, y, 30, 10);': 20,
            'GRect rect = new GRect(x, y, 40, 20);': 1,
            'GRect rect = new GRect(x, y, 30, 20);': 1,
        })

    def render(self):
        return self.getChoice('lyingDownRectangleSize')