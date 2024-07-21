import acm.graphics.*;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.imageio.ImageIO;

public class DrawStructure72{
    private static final int INNER_CANVAS_WIDTH = 600;
    private static final int INNER_CANVAS_HEIGHT = 400;
    private static final int OUTER_CANVAS_WIDTH = 800;
    private static final int OUTER_CANVAS_HEIGHT = 600;

    public static void main(String[] args) {
        // Create an off-screen GCanvas
        GCanvas canvas = new GCanvas();
        canvas.setSize(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);

        // Initialize brick parameters
        int NUM_BRICKS = 5;
int BRICK_WIDTH = 30;
int BRICK_HEIGHT = 10;
int BRICK_SEP = 0;
int ROGUE_BRICK_INDEX = -1;
int START_X = 300 + 100;
int START_Y = 100 + 350;
boolean isDiagonal = true;
boolean isUpRight = true;

        // Draw bricks
        for (int i = 0; i < NUM_BRICKS; i++) {
            int x = START_X;
            int y = START_Y;
            if (isDiagonal) {
                if (isUpRight) {
                    x += i * (BRICK_WIDTH + BRICK_SEP);
                    y -= i * (BRICK_HEIGHT + BRICK_SEP);
                } else {
                    x -= i * (BRICK_WIDTH + BRICK_SEP);
                    y -= i * (BRICK_HEIGHT + BRICK_SEP);
                }
            } else {
                y += i * (BRICK_HEIGHT + BRICK_SEP);
            }
            GRect brick = new GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT);

            // Add a rogue brick condition
            if (i == ROGUE_BRICK_INDEX) {
                brick.setFilled(true);
                brick.setColor(Color.RED);
            } else {
                brick.setFilled(true);
                brick.setColor(Color.BLACK);
            }

            canvas.add(brick);
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
                    String filename = "diagonal_" + timestamp + ".png";
    
                    try {
                        // Write the buffered image to a file
                        ImageIO.write(image, "png", new File(filename));
                        System.out.println("Image saved as " + filename);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }            
            }