from ideaToText import Decision

class OffsetExtra(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''import acm.graphics.*;
import acm.program.*;
import java.awt.Color;

public class DrawOffsetPyramidStructure extends GraphicsProgram {{
    public void run() {{
        // Set canvas size
        {SetCanvasSizePyramid}

        // Initialize structure parameters
        {InitializeStructureParametersPyramid}

        // Optionally add centering assist lines
        {AddCenteringAssistLines}

        // Draw a pyramid
        for (int i = 0; i < BRICKS_IN_BASE; i++) {{
            // Calculate row variables
            int nBricks = BRICKS_IN_BASE - i;
            int rowWidth = nBricks * BRICK_WIDTH;
            double rowY = OFFSET_Y + getHeight() - (i + 1) * BRICK_HEIGHT;
            double rowX = OFFSET_X + (getWidth() - rowWidth) / 2.0;

            // Draw a single row
            for (int j = 0; j < nBricks; j++) {{
                // Add a single brick
                double x = rowX + j * BRICK_WIDTH;
                GRect brick = new GRect(x, rowY, BRICK_WIDTH, BRICK_HEIGHT);

                // Determine if the brick is filled
                {SetBrickFilled}

                brick.setColor({BrickColorPyramidExtra});
                add(brick);
            }}
        }}
    }}

    public static void main(String[] args) {{
        // Start the GraphicsProgram
        new DrawOffsetPyramidStructure().start(args);
    }}
}}''': 1
        })

    def render(self):
        return self.getChoice('codeStructure')


class BrickColorPyramidExtra(Decision):
    def registerChoices(self):
        self.addChoice('brickColor', {
            'Color.GRAY': 1,
            'Color.BLUE': 1,
            'Color.GREEN': 1,
            'Color.YELLOW': 1,
            'Color.ORANGE': 1,
            'Color.MAGENTA': 1
        })

    def render(self):
        return self.getChoice('brickColor')
