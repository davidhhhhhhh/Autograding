from ideaToText import Decision


class HorizontalLoop(Decision):
    def registerChoices(self):
        self.addChoice('HLoopExistence', {
            'HLoopExist': 20,
            'HelloWorld': 1,
            'Diagonal': 1
        })

    def render(self):
        choice_mapping = {'HLoopExist': '''// Determine # of bricks 
                {NumBricksInHLoop}
                
               // Determine starting point 
                {StartingPoint}
                
               // Determine the number of rows
                {TotalRows}
                
               // Create a horizontal loop
                {NumRowsInVLoop}''',

                          'HelloWorld': '''// No horizontal loop, hello world
                //
                GRect brick = new GRect(5 + random.nextInt(700), 5 + random.nextInt(500), brick_width, brick_height);
                {SetColorFilled}
                canvas.add(brick);''',

                          'Diagonal': '''// No horizontal loop but vertical loop
                // Determine starting point 
                {StartingPointVec}
                
                int xOffset = random.nextInt(60);
                int nRows = 4 + random.nextInt(20);
                for (int i = 0; i < nRows; i++) {{
                    double x = start_X + i * xOffset;
                    double y = start_Y - i * brick_height;
                    // Draw a bricks
                    GRect brick = new GRect(x, y, brick_width, brick_height);
                    {SetColorFilled}
                    canvas.add(brick);
                }}'''}
        choice = self.getChoice('HLoopExistence')
        output = choice_mapping[choice]
        return output


class NumBricksInHLoop(Decision):
    def registerChoices(self):
        self.addChoice('NumBaseBricks', {
            'RightNumBaseBricks': 40,

            'FalseNumBaseBricks': 2,
        })

    def render(self):
        choice_mapping = {'RightNumBaseBricks': '''// Suitable # bricks in base row
                //
                int num_bricks_base = 7 + random.nextInt(12);
                int BRICKS_IN_BASE = num_bricks_base;''',

                          'FalseNumBaseBricks': '''// Too many bricks in base row
                //
                int num_bricks_base = 21 + random.nextInt(12);
                int BRICKS_IN_BASE = num_bricks_base;'''}

        choice = self.getChoice('NumBaseBricks')
        output = choice_mapping[choice]
        return output


class StartingPoint(Decision):
    def registerChoices(self):
        self.addChoice('StartingPoint', {
            'RightStartPoint': 10,

            'FalseStartPoint': 1,
        })

    def render(self):
        choice_mapping = {'RightStartPoint': '''// Correct Starting Point
                int baseRowWidth = num_bricks_base * brick_width;
                double start_Y = 500 - brick_height;
                double start_X = (canvas.getWidth() - baseRowWidth) / 2.0;''',

                          'FalseStartPoint': '''// Random Starting Point
                //
                double start_Y = random.nextInt(600);
                double start_X = random.nextInt(800);'''}

        choice = self.getChoice('StartingPoint')
        output = choice_mapping[choice]
        return output


class TotalRows(Decision):
    def registerChoices(self):
        self.addChoice('NumRows', {
            'RightNumRows': 10,

            'TwoRows': 2,

            'OtherLessRows': 2
        })

    def render(self):
        choice_mapping = {'RightNumRows': '''// Correct number of rows
                int nRows = num_bricks_base;
               ''',

                          'TwoRows': '''// Incorrect number of rows, two rows
                int nRows = 2;''',

                          'OtherLessRows': '''// Incorrect number of rows, less than a pyramid
                //
                int nRows = num_bricks_base - (1 + random.nextInt(3));'''
                          }

        choice = self.getChoice('NumRows')
        output = choice_mapping[choice]
        return output


class StartingPointVec(Decision):
        def registerChoices(self):
            self.addChoice('StartingPointVec', {
                'FalseStartPoint': 1,
            })

        def render(self):
            choice_mapping = {'FalseStartPoint': '''// Random Starting Point
                    double start_Y = random.nextInt(600);
                    double start_X = random.nextInt(800);'''}

            choice = self.getChoice('StartingPointVec')
            output = choice_mapping[choice]
            return output

