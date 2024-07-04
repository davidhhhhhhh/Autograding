from ideaToText import Decision

class Hello_world(Decision):
    def registerChoices(self):
        self.addChoice('codeStructure',{
            '''import acm.graphics.*;
import acm.program.*;

public class DrawRectangle extends GraphicsProgram {
    public void run() {
        // Set canvas size
        {Set_Canvas_Hello_World}
        // Create a rectangle with the specified position 
        {Initial_Position_Hello_World}
        // Specify size of the rectangle 
        {Draw_Block_Hello_World}
        // Add color, optional 
        {Add_Color_Hello_World}
       
        // Add the rectangle to the canvas
        add(rect);
    }
   
    public static void main(String[] args) {
        // Start the GraphicsProgram
        new DrawRectangle().start(args);
    }
}''': 1
        })

    def render(self):
    	# if the string you return has a Decision name
    	# in brackets, the sampler will auto expand itß
        return self.getChoice('codeStructure')