// Create offset bricks for even and odd rows
            import acm.graphics.*;
            import java.awt.Color;
            import java.awt.Graphics;
            import java.awt.image.BufferedImage;
            import java.io.File;
            import java.text.SimpleDateFormat;
            import java.util.Date;
            import javax.imageio.ImageIO;
    
            public class DrawStructure36{
                private static final int INNER_CANVAS_WIDTH = 600;
                private static final int INNER_CANVAS_HEIGHT = 400;
                private static final int OUTER_CANVAS_WIDTH = 800;
                private static final int OUTER_CANVAS_HEIGHT = 600;
    
                public static void main(String[] args) {
                    // Create an off-screen GCanvas
                    GCanvas canvas = new GCanvas();
                    canvas.setSize(OUTER_CANVAS_WIDTH, OUTER_CANVAS_HEIGHT);
    
                    // Initialize structure parameters
                    int NUM_COLUMNS = 53;
int NUM_ROWS = 120;
int BRICK_WIDTH = 30;
int BRICK_HEIGHT = 10;
    
                    // Draw rows of bricks covering the entire screen without offset
                    for (int row = 0; row < NUM_ROWS; row++) {
                        for (int col = 0; col < NUM_COLUMNS; col++) {
                            // 100 means the offset between outer and inner canvas
                            int x =   0 + col * BRICK_WIDTH + (row % 2 == 0 ? 0: BRICK_WIDTH / 2);
                            int y = 500 - row * BRICK_HEIGHT; 
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
                    String filename = "brick_wall_" + timestamp + ".png";
    
                    try {
                        // Write the buffered image to a file
                        ImageIO.write(image, "png", new File(filename));
                        System.out.println("Image saved as " + filename);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }            
            }