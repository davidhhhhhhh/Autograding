import acm.graphics.*;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.imageio.ImageIO;

public class DrawStructure149{
    private static final int INNER_CANVAS_WIDTH = 600;
    private static final int INNER_CANVAS_HEIGHT = 400;
    private static final int OUTER_CANVAS_WIDTH = 800;
    private static final int OUTER_CANVAS_HEIGHT = 600;

    public static void main(String[] args) {
        // Create an off-screen GCanvas
        GCanvas canvas = new GCanvas();
        canvas.setSize(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);

        // Determine the shape and initialize parameters
        int START_X = 750;
int START_Y = 50;
int NUM_ROWS = 16;
int NUM_BRICKS_BASE = 16;
int BRICK_WIDTH = 30;
int BRICK_HEIGHT = 10;
int BRICK_SEP = 0;
int ROW_SEP = 5;
boolean isUpsideDown = false;
boolean isRightTriangle = true;
String input = "16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1";
        
        // Convert String to int array 
        String[] stringArray = input.split(",");
        int[] NUM_BRICKS = new int[stringArray.length];
        for (int i = 0; i < stringArray.length; i++) {
            NUM_BRICKS[i] = Integer.parseInt(stringArray[i].trim());
        }

        // Draw rows of bricks
        for (int row = 0; row < NUM_ROWS; row++) {
            int numBricks = NUM_BRICKS[row];
            for (int i = 0; i < numBricks; i++) {
                int x = START_X + i * (BRICK_WIDTH + BRICK_SEP);
                int y = START_Y + row * (BRICK_HEIGHT + ROW_SEP);
                GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

                // Determine if the brick is filled
                brick.setFilled(false);
                brick.setColor(Color.BLACK);

                canvas.add(brick);
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
                    String filename = "right_triangle_" + timestamp + ".png";
    
                    try {
                        // Write the buffered image to a file
                        ImageIO.write(image, "png", new File(filename));
                        System.out.println("Image saved as " + filename);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }            
            }