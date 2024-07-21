import acm.graphics.*;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.imageio.ImageIO;
import java.util.Random;

public class DrawStructure402{
    private static final int INNER_CANVAS_WIDTH = 600;
    private static final int INNER_CANVAS_HEIGHT = 400;
    private static final int OUTER_CANVAS_WIDTH = 800;
    private static final int OUTER_CANVAS_HEIGHT = 600;

    public static void main(String[] args) {
        // Create an off-screen GCanvas
        GCanvas canvas = new GCanvas();
        canvas.setSize(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);

        // Initialize structure parameters
        int START_X = 150;
int START_Y = 50;
int NUM_ROWS = 5;
int BRICK_WIDTH = 30;
int BRICK_HEIGHT = 10;
int BRICK_SEP = 0;
int ROW_SEP = 0;
int HORIZONTAL_OFFSET = 20;
int HOLE_PROBABILITY = 3;
boolean isUpsideDown = false;
String input = "1, 2, 3, 4, 5";
        
        // Convert String to int array 
        String[] stringArray = input.split(",");
        int[] NUM_BRICKS = new int[stringArray.length];
        for (int i = 0; i < stringArray.length; i++) {
            NUM_BRICKS[i] = Integer.parseInt(stringArray[i].trim());
        }

        Random rand = new Random();

        // Draw rows of bricks with horizontal offset
        for (int row = 0; row < NUM_ROWS; row++) {
            int initialX = START_X + row * HORIZONTAL_OFFSET;
            for (int i = 0; i < NUM_BRICKS[row]; i++) {
                int x = initialX + i * (BRICK_WIDTH + BRICK_SEP);
                int y = START_Y + row * (BRICK_HEIGHT + ROW_SEP);

                // Randomly decide if there is a hole (missing brick)
                boolean hasHole = (rand.nextInt(10) < HOLE_PROBABILITY);

                if (!hasHole) {
                    GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

                    // Determine if the brick is filled
                    brick.setFilled(false);
                    brick.setColor(Color.BLACK);

                    canvas.add(brick);
                }
            }
        }
        // Draw the inner canvas boundary
        GRect innerCanvasBoundary = new GRect((OUTER_CANVAS_WIDTH - INNER_CANVAS_WIDTH) / 2,
                                               (OUTER_CANVAS_HEIGHT - INNER_CANVAS_HEIGHT) / 2,
                                               INNER_CANVAS_WIDTH, INNER_CANVAS_HEIGHT);
        innerCanvasBoundary.setColor(Color.BLACK);
        canvas.add(innerCanvasBoundary);
        
        // Save the canvas as an image
        saveCanvasAsImage(canvas);
    }
    private static void saveCanvasAsImage(GCanvas canvas) {
                    BufferedImage image = new BufferedImage(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT, BufferedImage.TYPE_INT_RGB);
                    Graphics g = image.getGraphics();
                    g.setColor(Color.WHITE);
                    g.fillRect(0, 0, OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);
    
                    // Draw the current canvas content to the buffered image
                    canvas.paint(g);
    
                    // Generate a unique filename using a timestamp
                    String timestamp = new SimpleDateFormat("yyyyMMddHHmmss").format(new Date());
                    String filename = "pyramid_like_" + timestamp + ".png";
    
                    try {
                        // Write the buffered image to a file
                        ImageIO.write(image, "png", new File(filename));
                        System.out.println("Image saved as " + filename);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }            
            }