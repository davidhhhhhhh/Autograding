from ideaToText import Decision


class NumRowsInVLoop(Decision):
    def registerChoices(self):
        self.addChoice('VLoopExistence', {
            'SingleRow': 1,

            'MultipleRows': 10
        })

    def render(self):
        choice_mapping = {'SingleRow': '''// Only one single row, no vertical loop
               for (int i = 0; i < num_bricks_base; i++) {{
                   // Single Row, no over lap 
                   {BrickSingleRowSpacing}
                   
                   // Draw a bricks
                   GRect brick = new GRect(x, start_Y, brick_width, brick_height);
                   {SetColorFilled}
                   canvas.add(brick);
               }}''',

                          'MultipleRows': '''// Vertical loop exist
               for (int i = 0; i < nRows; i++) {{
                    // Determine # of Bricks per row
                    {NumBricksPerRow}
                    
                    // Determine rowY value
                    {BrickYSpacing}                  
                    
                    // Determine horizontal offset
                    {RowOffset}
                    
                    // Draw a single row
                    for (int j = 0; j < nBricks; j++) {{
                        // Determine horizontal offset
                        {BrickMultiRowSpacing}
                        GRect brick = new GRect(x, rowY, brick_width, brick_height);
                        {SetColorFilled}
                        canvas.add(brick);
                    }}
                }}'''}

        choice = self.getChoice('VLoopExistence')
        output = choice_mapping[choice]
        return output


class NumBricksPerRow(Decision):
    def registerChoices(self):
        self.addChoice('NumBrickPerRow', {
            'RightNumBricksPerRow': 10,

            'ConstantNumBricksPerRow': 1,

            'RamLessBricksPerRow': 1,

            'RamMoreBricksPerRow': 1,
        })

    def render(self):
        choice_mapping = {'RightNumBricksPerRow': '''// Correct nBricks per row
                int nBricks = num_bricks_base - i;''',

                          'ConstantNumBricksPerRow': '''// Constant nBricks per row
                int nBricks = num_bricks_base;''',

                          'RamLessBricksPerRow': '''// Random less nBricks per row
                //
                int nBricks = num_bricks_base - random.nextInt(num_bricks_base) + 1;''',

                          'RamMoreBricksPerRow': '''// Random more nBricks per row
                //
                int nBricks = num_bricks_base + random.nextInt(num_bricks_base) + 1;'''
                          }

        choice = self.getChoice('NumBrickPerRow')
        output = choice_mapping[choice]
        return output

