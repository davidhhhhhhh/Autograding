from ideaToText import Decision

class TwoRows(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''import acm.graphics.*;
import acm.program.*;
import java.awt.Color;

public class DrawTwoRows extends GraphicsProgram {{
    public void run() {{
        // Set canvas size
        {SetCanvasSizeTwoRows}

        // Initialize brick parameters for first row
        {InitializeBrickParametersTwoRowsFirstRow}

        // Draw first row of bricks
        for (int i = 0; i < NUM_BRICKS_FIRST_ROW; i++) {{
            int x = START_X_FIRST_ROW + i * (BRICK_WIDTH_FIRST_ROW + BRICK_SEP_FIRST_ROW);
            int y = START_Y_FIRST_ROW;
            GRect brick = new GRect(x, y, BRICK_WIDTH_FIRST_ROW, BRICK_HEIGHT_FIRST_ROW);

            // Add a rogue brick condition for the first row
            if (i == ROGUE_BRICK_INDEX_FIRST_ROW) {{
                brick.setFilled(true);
                brick.setColor(Color.RED);
            }} else {{
                brick.setColor({BrickColorTwoRowsFirstRow});
            }}

            add(brick);
        }}

        // Initialize brick parameters for second row
        {InitializeBrickParametersTwoRowsSecondRow}

        // Draw second row of bricks
        for (int i = 0; i < NUM_BRICKS_SECOND_ROW; i++) {{
            int x = START_X_SECOND_ROW + i * (BRICK_WIDTH_SECOND_ROW + BRICK_SEP_SECOND_ROW);
            int y = START_Y_SECOND_ROW;
            GRect brick = new GRect(x, y, BRICK_WIDTH_SECOND_ROW, BRICK_HEIGHT_SECOND_ROW);

            // Add a rogue brick condition for the second row
            if (i == ROGUE_BRICK_INDEX_SECOND_ROW) {{
                brick.setFilled(true);
                brick.setColor(Color.RED);
            }} else {{
                brick.setColor({BrickColorTwoRowsSecondRow});
            }}

            add(brick);
        }}
    }}

    public static void main(String[] args) {{
        // Start the GraphicsProgram
        new DrawTwoRows().start(args);
    }}
}}''': 1
        })

    def render(self):
        return self.getChoice('codeStructure')


class SetCanvasSizeTwoRows(Decision):
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


class InitializeBrickParametersTwoRowsFirstRow(Decision):
    def registerChoices(self):
        self.addChoice('numBricksFirstRow', {
            'int NUM_BRICKS_FIRST_ROW = 3;': 2,
            'int NUM_BRICKS_FIRST_ROW = 4;': 1,
            'int NUM_BRICKS_FIRST_ROW = 5;': 2,
            'int NUM_BRICKS_FIRST_ROW = 6;': 3,
            'int NUM_BRICKS_FIRST_ROW = 7;': 4,
            'int NUM_BRICKS_FIRST_ROW = 8;': 5
        })
        self.addChoice('brickWidthFirstRow', {
            '40': 2,
            '30': 1,
            '20': 1
        })
        self.addChoice('brickHeightFirstRow', {
            '20': 2,
            '30': 1,
            '40': 1
        })
        self.addChoice('brickSeparationFirstRow', {
            'int BRICK_SEP_FIRST_ROW = 5;': 1,
            'int BRICK_SEP_FIRST_ROW = 0;': 5,
            'int BRICK_SEP_FIRST_ROW = 10;': 1
        })
        self.addChoice('rogueBrickIndexFirstRow', {
            'int ROGUE_BRICK_INDEX_FIRST_ROW = -1;': 3,  # No rogue brick
            'int ROGUE_BRICK_INDEX_FIRST_ROW = 1;': 1,  # Rogue brick at position 1
            'int ROGUE_BRICK_INDEX_FIRST_ROW = 2;': 1  # Rogue brick at position 2
        })
        self.addChoice('startXFirstRow', {
            'int START_X_FIRST_ROW = 50;': 2,
            'int START_X_FIRST_ROW = 100;': 1,
            'int START_X_FIRST_ROW = -100;': 1,
            'int START_X_FIRST_ROW = -50;': 1
        })
        self.addChoice('startYFirstRow', {
            'int START_Y_FIRST_ROW = 50;': 2,
            'int START_Y_FIRST_ROW = 100;': 1,
            'int START_Y_FIRST_ROW = 150;': 1,
            'int START_Y_FIRST_ROW = -50;': 2,
            'int START_Y_FIRST_ROW = -100;': 1,
            'int START_Y_FIRST_ROW = -150;': 1
        })

    def render(self):
        return '\n'.join([
            self.getChoice('numBricksFirstRow'),
            'int BRICK_WIDTH_FIRST_ROW = {};'.format(self.getChoice('brickWidthFirstRow')),
            'int BRICK_HEIGHT_FIRST_ROW = {};'.format(self.getChoice('brickHeightFirstRow')),
            self.getChoice('brickSeparationFirstRow'),
            self.getChoice('rogueBrickIndexFirstRow'),
            self.getChoice('startXFirstRow'),
            self.getChoice('startYFirstRow')
        ])


class InitializeBrickParametersTwoRowsSecondRow(Decision):
    def registerChoices(self):
        self.addChoice('numBricksSecondRow', {
            'int NUM_BRICKS_SECOND_ROW = 3;': 2,
            'int NUM_BRICKS_SECOND_ROW = 4;': 1,
            'int NUM_BRICKS_SECOND_ROW = 5;': 2,
            'int NUM_BRICKS_SECOND_ROW = 6;': 3,
            'int NUM_BRICKS_SECOND_ROW = 7;': 4,
            'int NUM_BRICKS_SECOND_ROW = 8;': 5
        })
        self.addChoice('brickWidthSecondRow', {
            '40': 2,
            '30': 1,
            '20': 1
        })
        self.addChoice('brickHeightSecondRow', {
            '20': 2,
            '30': 1,
            '40': 1
        })
        self.addChoice('brickSeparationSecondRow', {
            'int BRICK_SEP_SECOND_ROW = 5;': 1,
            'int BRICK_SEP_SECOND_ROW = 0;': 5,
            'int BRICK_SEP_SECOND_ROW = 10;': 1
        })
        self.addChoice('rogueBrickIndexSecondRow', {
            'int ROGUE_BRICK_INDEX_SECOND_ROW = -1;': 3,  # No rogue brick
            'int ROGUE_BRICK_INDEX_SECOND_ROW = 1;': 1,  # Rogue brick at position 1
            'int ROGUE_BRICK_INDEX_SECOND_ROW = 2;': 1  # Rogue brick at position 2
        })
        self.addChoice('startXSecondRow', {
            'int START_X_SECOND_ROW = START_X_FIRST_ROW;': 2,
            'int START_X_SECOND_ROW = START_X_FIRST_ROW + 100;': 1,
            'int START_X_SECOND_ROW = START_X_FIRST_ROW + 50;': 1
        })
        self.addChoice('startYSecondRow', {
            'int START_Y_SECOND_ROW = START_Y_FIRST_ROW + BRICK_HEIGHT_FIRST_ROW;': 5,
            'int START_Y_SECOND_ROW = START_Y_FIRST_ROW + 150;': 1,
            'int START_Y_SECOND_ROW = START_Y_FIRST_ROW + 200;': 1,
            'int START_Y_SECOND_ROW = START_Y_FIRST_ROW + 250;': 1
        })

    def render(self):
        return '\n'.join([
            self.getChoice('numBricksSecondRow'),
            'int BRICK_WIDTH_SECOND_ROW = {};'.format(self.getChoice('brickWidthSecondRow')),
            'int BRICK_HEIGHT_SECOND_ROW = {};'.format(self.getChoice('brickHeightSecondRow')),
            self.getChoice('brickSeparationSecondRow'),
            self.getChoice('rogueBrickIndexSecondRow'),
            self.getChoice('startXSecondRow'),
            self.getChoice('startYSecondRow')
        ])


class BrickColorTwoRowsFirstRow(Decision):
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


class BrickColorTwoRowsSecondRow(Decision):
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
