from ideaToText import Decision


class HorizontalLoop(Decision):
    def registerChoices(self):
        self.addChoice('HLoopExistence', {
            '{HLoopExist}': 10,
            '{HLoopNotExist}': 1
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('HLoopExistence')


class HLoopNotExist(Decision):
    def registerChoices(self):
        self.addChoice('hello_world', {
            '''// No horizontal loop, hello world
                GRect brick = new GRect(300, 300, brick_width, brick_height);
                canvas.add(brick);''': 1
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('hello_world')


class HLoopExist(Decision):
    def registerChoices(self):
        self.addChoice('HLoopExist', {
            '''// Determine # of bricks 
                {NumBricksInHLoop}
                
               // Determine starting point 
                {StartingPoint}
                
               // Create a horizontal loop
                {NumRowsInVLoop}''': 1
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('HLoopExist')


class NumBricksInHLoop(Decision):
    def registerChoices(self):
        self.addChoice('NumBaseBricks', {
            '''// Suitable # bricks in base row
                int num_bricks_base = 7;
                int BRICKS_IN_BASE = num_bricks_base;''': 20,

            '''// Too many bricks in base row
                int num_bricks_base = 25;
                int BRICKS_IN_BASE = num_bricks_base;''': 1,
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('NumBaseBricks')


class StartingPoint(Decision):
    def registerChoices(self):
        self.addChoice('StartingPoint', {
            '''// Correct Starting Point
                int baseRowWidth = num_bricks_base * brick_width;
                double start_Y = 500 - brick_height;
                double start_X = (canvas.getWidth() - baseRowWidth) / 2.0;''': 10,

            '''// Random Starting Point
                double start_Y = 300;
                double start_X = 400;''': 1,
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('StartingPoint')

