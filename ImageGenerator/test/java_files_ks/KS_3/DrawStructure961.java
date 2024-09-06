import acm.graphics.*;
import java.awt.Color;
import java.util.Random;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.imageio.ImageIO;

public class DrawStructure961{
    private static final int INNER_CANVAS_WIDTH = 600;
    private static final int INNER_CANVAS_HEIGHT = 400;
    private static final int OUTER_CANVAS_WIDTH = 800;
    private static final int OUTER_CANVAS_HEIGHT = 600;

    public static void main(String[] args) {
        // Create an off-screen GCanvas
        GCanvas canvas = new GCanvas();
        canvas.setSize(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);
        
        // Initiate new random
        Random random = new Random();

        // Initialize brick size
        int brick_width = 30;
               int brick_height = 10;
               int BRICK_WIDTH = brick_width;
               int BRICK_HEIGHT = brick_height;

        // Horizontal Loop
        // Determine # of bricks 
                // Suitable # bricks in base row
                //
                int num_bricks_base = 7 + random.nextInt(12);
                int BRICKS_IN_BASE = num_bricks_base;
                
               // Determine starting point 
                // Correct Starting Point
                int baseRowWidth = num_bricks_base * brick_width;
                double start_Y = 500 - brick_height;
                double start_X = (canvas.getWidth() - baseRowWidth) / 2.0;
                
               // Determine the number of rows
                // Correct number of rows
                int nRows = num_bricks_base;
               
                
               // Create a horizontal loop
                // Vertical loop exist
               for (int i = 0; i < nRows; i++) {
                    // Determine # of Bricks per row
                    // Correct nBricks per row
                int nBricks = num_bricks_base - i;
                    
                    // Determine rowY value
                    // Correct brick space in Y direction
                double rowY = start_Y - i * BRICK_HEIGHT;                   
                    
                    // Determine horizontal offset
                     // Constant value of offset, correct direction
                //
                double rowX = start_X + i * random.nextInt(30);
               
               
                    
                    // Draw a single row
                    for (int j = 0; j < nBricks; j++) {
                        // Determine horizontal offset
                        // Correct brick space
                double x = rowX + j * BRICK_WIDTH; 
                        GRect brick = new GRect(x, rowY, brick_width, brick_height);
                        // Black Color, Not filled
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
                    String filename = "image_" + timestamp + ".png";

                    try {
                        // Write the buffered image to a file
                        ImageIO.write(image, "png", new File(filename));
                        System.out.println("Image saved as " + filename);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }            
            }