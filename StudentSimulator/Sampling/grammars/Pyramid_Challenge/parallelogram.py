from StudentSimulator.ideaToText import Decision

class Parallelogram(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''import acm.graphics.*;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.imageio.ImageIO;

public class DrawStructure{{
    private static final int INNER_CANVAS_WIDTH = 600;
    private static final int INNER_CANVAS_HEIGHT = 400;
    private static final int OUTER_CANVAS_WIDTH = 800;
    private static final int OUTER_CANVAS_HEIGHT = 600;

    public static void main(String[] args) {{
        // Create an off-screen GCanvas
        GCanvas canvas = new GCanvas();
        canvas.setSize(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);

        // Initialize brick parameters for rows
        {InitializeBrickParametersParallelogram}

        // Draw rows of bricks with horizontal offset
        for (int row = 0; row < NUM_ROWS; row++) {{
            int initialX = START_X + row * OFFSET;
            for (int i = 0; i < NUM_BRICKS_PER_ROW; i++) {{
                int x = initialX + i * (BRICK_WIDTH + BRICK_SEP);
                int y = START_Y + row * (BRICK_HEIGHT + ROW_SEP);
                GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

                // Determine if the brick is filled
                {SetBrickFilled}

                // Add a rogue row/diagonal condition
                if ((row == ROGUE_ROW_INDEX && isRogueRow) || (i == ROGUE_DIAGONAL_INDEX && isRogueDiagonal)) {{
                    {SetRogueBrickFilled}
                    brick.setColor(Color.RED);
                }} else {{
                    brick.setColor({BrickColorParallelogram});
                }}

                canvas.add(brick);
            }}
        }}
        // Draw the inner canvas boundary
        GRect innerCanvasBoundary = new GRect((OUTER_CANVAS_WIDTH - INNER_CANVAS_WIDTH) / 2,
                                               (OUTER_CANVAS_HEIGHT - INNER_CANVAS_HEIGHT) / 2,
                                               INNER_CANVAS_WIDTH, INNER_CANVAS_HEIGHT);
        innerCanvasBoundary.setColor(Color.BLACK);
        canvas.add(innerCanvasBoundary);
        
        // Save the canvas as an image
        saveCanvasAsImage(canvas);
    }}
    private static void saveCanvasAsImage(GCanvas canvas) {{
                    BufferedImage image = new BufferedImage(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT, BufferedImage.TYPE_INT_RGB);
                    Graphics g = image.getGraphics();
                    g.setColor(Color.WHITE);
                    g.fillRect(0, 0, OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);
    
                    // Draw the current canvas content to the buffered image
                    canvas.paint(g);
    
                    // Generate a unique filename using a timestamp
                    String timestamp = new SimpleDateFormat("yyyyMMddHHmmss").format(new Date());
                    String filename = "parallelogram_" + timestamp + ".png";
    
                    try {{
                        // Write the buffered image to a file
                        ImageIO.write(image, "png", new File(filename));
                        System.out.println("Image saved as " + filename);
                    }} catch (Exception e) {{
                        e.printStackTrace();
                    }}
                }}            
            }}''': 1
        })

    def render(self):
        return self.getChoice('codeStructure')


class InitializeBrickParametersParallelogram(Decision):
    def registerChoices(self):
        self.addChoice('numRows', {
            'int NUM_ROWS = 3;': 1,
            'int NUM_ROWS = 4;': 2,
            'int NUM_ROWS = 5;': 3,
            'int NUM_ROWS = 6;': 4,
            'int NUM_ROWS = 7;': 5
        })
        self.addChoice('numBricksPerRow', {
            'int NUM_BRICKS_PER_ROW = 3;': 1,
            'int NUM_BRICKS_PER_ROW = 4;': 1,
            'int NUM_BRICKS_PER_ROW = 5;': 2,
            'int NUM_BRICKS_PER_ROW = 6;': 3,
            'int NUM_BRICKS_PER_ROW = 7;': 4,
            'int NUM_BRICKS_PER_ROW = 8;': 5,
        })
        self.addChoice('offset', {
            'int OFFSET = 20;': 2,
            'int OFFSET = -20;': 1
        })
        self.addChoice('brickWidth', {
            '40': 1,
            '30': 10,
            '20': 1
        })
        self.addChoice('brickHeight', {
            '10': 10,
            '30': 1,
            '40': 1
        })
        self.addChoice('brickSeparation', {
            'int BRICK_SEP = 5;': 1,
            'int BRICK_SEP = 0;': 20,
            'int BRICK_SEP = 10;': 1
        })
        self.addChoice('rowSeparation', {
            'int ROW_SEP = 5;': 1,
            'int ROW_SEP = 0;': 20,
            'int ROW_SEP = 10;': 1
        })
        self.addChoice('rogueRowIndex', {
            'int ROGUE_ROW_INDEX = -1;': 20,  # No rogue row
            'int ROGUE_ROW_INDEX = 1;': 1,  # Rogue row at position 1
            'int ROGUE_ROW_INDEX = 2;': 1  # Rogue row at position 2
        })
        self.addChoice('rogueDiagonalIndex', {
            'int ROGUE_DIAGONAL_INDEX = -1;': 20,  # No rogue diagonal
            'int ROGUE_DIAGONAL_INDEX = 1;': 1,  # Rogue diagonal at position 1
            'int ROGUE_DIAGONAL_INDEX = 2;': 1  # Rogue diagonal at position 2
        })
        self.addChoice('startX', {
            'int START_X = 150;': 1,
            'int START_X = 200;': 1,
            'int START_X = 550;': 1,
            'int START_X = 50;': 1  # Potentially out of canvas
        })
        self.addChoice('startY', {
            'int START_Y = 500;': 1,
            'int START_Y = 400;': 1,
            'int START_Y = 50;': 1,
            'int START_Y = 550;': 1  # Potentially out of canvas
        })
        self.addChoice('isRogueRow', {
            'boolean isRogueRow = true;': 1,
            'boolean isRogueRow = false;': 10
        })
        self.addChoice('isRogueDiagonal', {
            'boolean isRogueDiagonal = true;': 1,
            'boolean isRogueDiagonal = false;': 10
        })

    def render(self):
        return '\n'.join([
            '{};'.format(self.getChoice('numRows')),
            '{};'.format(self.getChoice('numBricksPerRow')),
            '{};'.format(self.getChoice('offset')),
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


class BrickColorParallelogram(Decision):
    def registerChoices(self):
        self.addChoice('brickColor', {
            'Color.GRAY': 1,
            'Color.BLUE': 1,
            'Color.GREEN': 1,
            'Color.RED': 1,
            'Color.ORANGE': 1,
            'Color.MAGENTA': 1,
            'Color.BLACK': 60
        })

    def render(self):
        return self.getChoice('brickColor')