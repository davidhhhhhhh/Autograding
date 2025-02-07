from StudentSimulator.ideaToText import Decision


class TwoRows(Decision):
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

            canvas.add(brick);
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

            canvas.add(brick);
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
                    String filename = "two_rows_" + timestamp + ".png";
    
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


class InitializeBrickParametersTwoRowsFirstRow(Decision):
    def registerChoices(self):
        self.addChoice('numBricksFirstRow', {
            'int NUM_BRICKS_FIRST_ROW = 3;': 2,
            'int NUM_BRICKS_FIRST_ROW = 4;': 1,
            'int NUM_BRICKS_FIRST_ROW = 5;': 2,
            'int NUM_BRICKS_FIRST_ROW = 6;': 3,
            'int NUM_BRICKS_FIRST_ROW = 7;': 4,
            'int NUM_BRICKS_FIRST_ROW = 8;': 5,
            'int NUM_BRICKS_FIRST_ROW = 15;': 5
        })
        self.addChoice('brickWidthFirstRow', {
            '40': 1,
            '30': 20,
            '20': 1
        })
        self.addChoice('brickHeightFirstRow', {
            '10': 20,
            '30': 1,
            '40': 1
        })
        self.addChoice('brickSeparationFirstRow', {
            'int BRICK_SEP_FIRST_ROW = 5;': 1,
            'int BRICK_SEP_FIRST_ROW = 0;': 20,
            'int BRICK_SEP_FIRST_ROW = 10;': 1
        })
        self.addChoice('rogueBrickIndexFirstRow', {
            'int ROGUE_BRICK_INDEX_FIRST_ROW = -1;': 20,  # No rogue brick
            'int ROGUE_BRICK_INDEX_FIRST_ROW = 1;': 1,  # Rogue brick at position 1
            'int ROGUE_BRICK_INDEX_FIRST_ROW = 2;': 1  # Rogue brick at position 2
        })
        self.addChoice('startXFirstRow', {
            'int START_X_FIRST_ROW = 150;': 2,
            'int START_X_FIRST_ROW = 200;': 1,
            'int START_X_FIRST_ROW = 300;': 1,
            'int START_X_FIRST_ROW = 650;': 1,
            'int START_X_FIRST_ROW = 0;': 1,
            'int START_X_FIRST_ROW = 50;': 1
        })
        self.addChoice('startYFirstRow', {
            'int START_Y_FIRST_ROW = 450;': 1,
            'int START_Y_FIRST_ROW = 500;': 20,
            'int START_Y_FIRST_ROW = 350;': 1,
            'int START_Y_FIRST_ROW = 250;': 1,
            'int START_Y_FIRST_ROW = 550;': 1,
            'int START_Y_FIRST_ROW = 150;': 1
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
            '40': 1,
            '30': 20,
            '20': 1
        })
        self.addChoice('brickHeightSecondRow', {
            '10': 20,
            '30': 1,
            '40': 1
        })
        self.addChoice('brickSeparationSecondRow', {
            'int BRICK_SEP_SECOND_ROW = 5;': 1,
            'int BRICK_SEP_SECOND_ROW = 0;': 20,
            'int BRICK_SEP_SECOND_ROW = 10;': 1
        })
        self.addChoice('rogueBrickIndexSecondRow', {
            'int ROGUE_BRICK_INDEX_SECOND_ROW = -1;': 20,  # No rogue brick
            'int ROGUE_BRICK_INDEX_SECOND_ROW = 1;': 1,  # Rogue brick at position 1
            'int ROGUE_BRICK_INDEX_SECOND_ROW = 2;': 1  # Rogue brick at position 2
        })
        self.addChoice('startXSecondRow', {
            'int START_X_SECOND_ROW = START_X_FIRST_ROW;': 1,
            'int START_X_SECOND_ROW = START_X_FIRST_ROW + 100;': 1,
            'int START_X_SECOND_ROW = START_X_FIRST_ROW + 50;': 1
        })
        self.addChoice('startYSecondRow', {
            'int START_Y_SECOND_ROW = START_Y_FIRST_ROW - BRICK_HEIGHT_FIRST_ROW;': 16,
            'int START_Y_SECOND_ROW = START_Y_FIRST_ROW + 150;': 1,
            'int START_Y_SECOND_ROW = START_Y_FIRST_ROW + 200;': 1,
            'int START_Y_SECOND_ROW = START_Y_FIRST_ROW + 250;': 1,
            'int START_Y_SECOND_ROW = START_Y_FIRST_ROW + BRICK_HEIGHT_FIRST_ROW;': 5,
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
            'Color.RED': 1,
            'Color.ORANGE': 1,
            'Color.MAGENTA': 1,
            'Color.BLACK': 60
        })

    def render(self):
        return self.getChoice('brickColor')


class BrickColorTwoRowsSecondRow(Decision):
    def registerChoices(self):
        self.addChoice('brickColor', {
            'Color.GRAY': 1,
            'Color.BLUE': 1,
            'Color.GREEN': 1,
            'Color.YELLOW': 1,
            'Color.ORANGE': 1,
            'Color.MAGENTA': 1,
            'Color.BLACK': 60
        })

    def render(self):
        return self.getChoice('brickColor')
