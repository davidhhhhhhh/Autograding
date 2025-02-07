from StudentSimulator.ideaToText import Decision

class BrickWall(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure', {
            '''// create aligned bricks in canvas 
import acm.graphics.*;
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

        // Initialize structure parameters
        {InitializeStructureParametersBrickWall}

        // Draw rows of bricks covering the entire screen without offset
        for (int row = 0; row < NUM_ROWS; row++) {{
            for (int col = 0; col < NUM_COLUMNS; col++) {{
                // 100 means the offset between outer and inner canvas
                int x = 100 + col * BRICK_WIDTH; 
                int y = 100 + row * BRICK_HEIGHT;
                GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

                // Determine if the brick is filled
                {SetBrickFilledWall}

                brick.setColor({BrickColorBrickWall});
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
        String filename = "pyramid_structure_" + timestamp + ".png";

        try {{
            // Write the buffered image to a file
            ImageIO.write(image, "png", new File(filename));
            System.out.println("Image saved as " + filename);
        }} catch (Exception e) {{
            e.printStackTrace();
        }}
    }}            
}}''': 1,
            '''// Create offset bricks for even and odd rows
            import acm.graphics.*;
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
    
                    // Initialize structure parameters
                    {InitializeStructureParametersBrickWallWholeScreen}
    
                    // Draw rows of bricks covering the entire screen without offset
                    for (int row = 0; row < NUM_ROWS; row++) {{
                        for (int col = 0; col < NUM_COLUMNS; col++) {{
                            // 100 means the offset between outer and inner canvas
                            {WallXFullScreen}
                            {WallYFullScreen} 
                            GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);
    
                            // Determine if the brick is filled
                            {SetBrickFilledWall}
    
                            brick.setColor({BrickColorBrickWall});
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
                    String filename = "brick_wall_" + timestamp + ".png";
    
                    try {{
                        // Write the buffered image to a file
                        ImageIO.write(image, "png", new File(filename));
                        System.out.println("Image saved as " + filename);
                    }} catch (Exception e) {{
                        e.printStackTrace();
                    }}
                }}            
            }}''': 3
        })

    def render(self):
        return self.getChoice('codeStructure')


class InitializeStructureParametersBrickWall(Decision):
    def registerChoices(self):
        self.addChoice('brickWidth', {
            '30': 7,
            '60': 1,
            '80': 1,
            '100': 1
        })
        self.addChoice('brickHeight', {
            '20': 1,
            '10': 7,
            '40': 1,
            '50': 1
        })

    def render(self):
        brickWidth = int(self.getChoice('brickWidth'))
        brickHeight = int(self.getChoice('brickHeight'))

        canvasWidth = 600
        canvasHeight = 400

        numColumns = canvasWidth // brickWidth
        numRows = canvasHeight // brickHeight

        return '\n'.join([
            'int NUM_COLUMNS = {};'.format(numColumns),
            'int NUM_ROWS = {};'.format(numRows),
            'int BRICK_WIDTH = {};'.format(brickWidth),
            'int BRICK_HEIGHT = {};'.format(brickHeight)
        ])

class BrickColorBrickWall(Decision):
    def registerChoices(self):
        self.addChoice('brickColor', {
            'Color.GRAY': 1,
            'Color.BLUE': 1,
            'Color.RED': 1,
            'Color.ORANGE': 1,
            'Color.MAGENTA': 1,
            'Color.BLACK': 50
        })

    def render(self):
        return self.getChoice('brickColor')


class SetBrickFilledWall(Decision):
    def registerChoices(self):
        self.addChoice('brickFilled', {
            'brick.setFilled(false);': 10,
            'brick.setFilled(true);': 1
        })

    def render(self):
        return self.getChoice('brickFilled')


class InitializeStructureParametersBrickWallWholeScreen(Decision):
    def registerChoices(self):
        self.addChoice('brickWidth', {
            '30': 30,
            '60': 1,
            '80': 1,
            '120': 1
        })
        self.addChoice('brickHeight', {
            '20': 1,
            '10': 30,
            '40': 1,
            '30': 1
        })

    def render(self):
        brickWidth = int(self.getChoice('brickWidth'))
        brickHeight = int(self.getChoice('brickHeight'))

        canvasWidth = 800
        canvasHeight = 600

        numColumns = 2 * canvasWidth // brickWidth
        numRows = 2 * canvasHeight // brickHeight

        return '\n'.join([
            'int NUM_COLUMNS = {};'.format(numColumns),
            'int NUM_ROWS = {};'.format(numRows),
            'int BRICK_WIDTH = {};'.format(brickWidth),
            'int BRICK_HEIGHT = {};'.format(brickHeight)
        ])


class WallXFullScreen(Decision):
    def registerChoices(self):
        self.addChoice('offsetX', {
            'int x = - 100 + col * BRICK_WIDTH + (row % 2 == 0 ? 0: BRICK_WIDTH / 2);': 2,
            'int x = - 90 + col * BRICK_WIDTH + (row % 2 == 0 ? 0: BRICK_WIDTH / 2);': 1,
            'int x = - 50 + col * BRICK_WIDTH + (row % 2 == 0 ? 0: BRICK_WIDTH / 2);': 1,
            'int x = - 30 + col * BRICK_WIDTH + (row % 2 == 0 ? 0: BRICK_WIDTH / 2);': 1,
            'int x =   100 + col * BRICK_WIDTH + (row % 2 == 0 ? 0: BRICK_WIDTH / 2);': 1,
            'int x =   0 + col * BRICK_WIDTH + (row % 2 == 0 ? 0: BRICK_WIDTH / 2);': 1,

        })

    def render(self):
        return self.getChoice('offsetX')


class WallYFullScreen(Decision):
    def registerChoices(self):
        self.addChoice('offsetY', {
            'int y = 500 - row * BRICK_HEIGHT;': 3,
            'int y = 500 - (row + 1) * BRICK_HEIGHT;': 1,
            'int y = 600 - (row + 1) * BRICK_HEIGHT;': 1,
            'int y = 600 - row * BRICK_HEIGHT;': 1,
        })

    def render(self):
        return self.getChoice('offsetY')
