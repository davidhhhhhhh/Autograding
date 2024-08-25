from ideaToText import Decision


class NumRowsInVLoop(Decision):
    def registerChoices(self):
        self.addChoice('VLoopExistence', {
            '''// Only one single row, no vertical loop
               for (int i = 0; i < num_bricks_base; i++) {{
                   // Single Row, no over lap 
                   {BrickSingleRowSpacing}
                   
                   // Draw a bricks
                   GRect brick = new GRect(x, start_Y, brick_width, brick_height);
                   canvas.add(brick);
               }}''': 1,

            '''// Vertical loop exist
               for (int i = 0; i < num_bricks_base; i++) {{
                    // Determine # of Bricks per row
                    {NumBricksPerRow}
                    
                    // Determine Number of Rows
                    {TotalRows}
                    
                    // Determine rowY value
                    {BrickYSpacing}                  
                    
                    // Determine horizontal offset
                    {RowOffset}
                    
                    // Draw a single row
                    for (int j = 0; j < nRows; j++) {{
                        // Determine horizontal offset
                        {BrickMultiRowSpacing}
                        GRect brick = new GRect(x, rowY, brick_width, brick_height);
                        canvas.add(brick);
                    }}
                }}''': 10
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('VLoopExistence')


class NumBricksPerRow(Decision):
    def registerChoices(self):
        self.addChoice('NumBrickPerRow', {
            '''// Correct nBricks per row
                int nBricks = num_bricks_base - i;''': 10,

            '''// Constant nBricks per row
                int nBricks = num_bricks_base;''': 1,

            '''// Random nBricks per row
                int nBricks = num_bricks_base - 2 * i;''': 1,
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('NumBrickPerRow')


class TotalRows(Decision):
    def registerChoices(self):
        self.addChoice('NumRows', {
            '''// Correct number of rows
                int nRows = nBricks;
               ''': 5,

            '''// Incorrect number of rows
                int nRows = 4;''': 1,
        })

    def render(self):
        # if the string you return has a Decision name
        # in brackets, the sampler will auto expand itß
        return self.getChoice('NumRows')

