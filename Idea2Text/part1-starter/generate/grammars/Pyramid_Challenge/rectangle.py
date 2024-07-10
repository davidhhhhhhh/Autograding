from ideaToText import Decision

class Rectangle(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''import acm.graphics.*;
import acm.program.*;
import java.awt.Color;

public class DrawRectangleStructure extends GraphicsProgram {{
    public void run() {{
        // Set canvas size
        {SetCanvasSizeRectangle}

        // Initialize brick parameters for rows
        {InitializeBrickParametersRectangleRows}

        // Draw rows of bricks
        for (int row = 0; row < NUM_ROWS; row++) {{
            for (int i = 0; i < NUM_BRICKS_PER_ROW; i++) {{
                int x = START_X + i * (BRICK_WIDTH + BRICK_SEP);
                int y = START_Y + row * (BRICK_HEIGHT + ROW_SEP);
                GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

                // Add a rogue row/diagonal condition
                if ((row == ROGUE_ROW_INDEX && isRogueRow) || (i == ROGUE_DIAGONAL_INDEX && isRogueDiagonal)) {{
                    brick.setFilled(true);
                    brick.setColor(Color.RED);
                }} else {{
                    brick.setFilled(true);
                    brick.setColor({BrickColorRectangle});
                }}

                add(brick);
            }}
        }}
    }}

    public static void main(String[] args) {{
        // Start the GraphicsProgram
        new DrawRectangleStructure().start(args);
    }}
}}''': 1
        })

    def render(self):
        return self.getChoice('codeStructure')


class SetCanvasSizeRectangle(Decision):
    def registerChoices(self):
        self.addChoice('canvasWidth', {
            '400': 2,
            '600': 1
        })
        self.addChoice('canvasHeight', {
            '260': 3,
            '400': 1,
            '600': 1
        })

    def render(self):
        return 'setSize({}, {});'.format(self.getChoice('canvasWidth'), self.getChoice('canvasHeight'))


class InitializeBrickParametersRectangleRows(Decision):
    def registerChoices(self):
        self.addChoice('numRows', {
            'int NUM_ROWS = 3;': 2,
            'int NUM_ROWS = 4;': 1,
            'int NUM_ROWS = 5;': 2,
            'int NUM_ROWS = 6;': 3,
            'int NUM_ROWS = 7;': 4,
            'int NUM_ROWS = 8;': 5
        })
        self.addChoice('numBricksPerRow', {
            'int NUM_BRICKS_PER_ROW = 3;': 1,
            'int NUM_BRICKS_PER_ROW = 4;': 2,
            'int NUM_BRICKS_PER_ROW = 5;': 3,
            'int NUM_BRICKS_PER_ROW = 6;': 4,
            'int NUM_BRICKS_PER_ROW = 7;': 5
        })
        self.addChoice('brickWidth', {
            '40': 2,
            '30': 1,
            '20': 1
        })
        self.addChoice('brickHeight', {
            '20': 2,
            '30': 1,
            '40': 1
        })
        self.addChoice('brickSeparation', {
            'int BRICK_SEP = 5;': 1,
            'int BRICK_SEP = 0;': 5,
            'int BRICK_SEP = 10;': 1
        })
        self.addChoice('rowSeparation', {
            'int ROW_SEP = 5;': 1,
            'int ROW_SEP = 0;': 5,
            'int ROW_SEP = 10;': 1
        })
        self.addChoice('rogueRowIndex', {
            'int ROGUE_ROW_INDEX = -1;': 3,  # No rogue row
            'int ROGUE_ROW_INDEX = 1;': 1,  # Rogue row at position 1
            'int ROGUE_ROW_INDEX = 2;': 1  # Rogue row at position 2
        })
        self.addChoice('rogueDiagonalIndex', {
            'int ROGUE_DIAGONAL_INDEX = -1;': 3,  # No rogue diagonal
            'int ROGUE_DIAGONAL_INDEX = 1;': 1,  # Rogue diagonal at position 1
            'int ROGUE_DIAGONAL_INDEX = 2;': 1  # Rogue diagonal at position 2
        })
        self.addChoice('startX', {
            'int START_X = 50;': 1,
            'int START_X = 100;': 1,
            'int START_X = -50;': 1  # Potentially out of canvas
        })
        self.addChoice('startY', {
            'int START_Y = 50;': 1,
            'int START_Y = 100;': 1,
            'int START_Y = -50;': 1  # Potentially out of canvas
        })
        self.addChoice('isRogueRow', {
            'boolean isRogueRow = true;': 1,
            'boolean isRogueRow = false;': 2
        })
        self.addChoice('isRogueDiagonal', {
            'boolean isRogueDiagonal = true;': 1,
            'boolean isRogueDiagonal = false;': 2
        })

    def render(self):
        initialization = '\n'.join([
            '{};'.format(self.getChoice('numRows')),
            '{};'.format(self.getChoice('numBricksPerRow')),
            'int BRICK_WIDTH = {};'.format(self.getChoice('brickWidth')),
            'int BRICK_HEIGHT = {};'.format(self.getChoice('brickHeight')),
            self.getChoice('brickSeparation'),
            self.getChoice('rowSeparation'),
            self.getChoice('rogueRowIndex'),
            self.getChoice('rogueDiagonalIndex'),
            self.getChoice('startX'),
            self.getChoice('startY'),
            self.getChoice('isRogueRow'),
            self.getChoice('isRogueDiagonal')
        ])
        return initialization


class BrickColorRectangle(Decision):
    def registerChoices(self):
        self.addChoice('brickColor', {
            'Color.GRAY': 2,
            'Color.BLUE': 1,
            'Color.GREEN': 1,
            'Color.YELLOW': 1,
            'Color.ORANGE': 1,
            'Color.MAGENTA': 1,
            'Color.BLACK': 5
        })

    def render(self):
        return self.getChoice('brickColor')