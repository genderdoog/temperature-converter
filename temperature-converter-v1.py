"""
Temperature converter in python using tkinter

Created by: Matthew C
Created on: 10/6/25

Version 1: set up the frames and make the buttons work
"""

from tkinter import * 

class Program:
    
    def __init__(self):
        '''Set up the GUI'''
        # Main window setup
        self.root = Tk()
        self.root.title("Temperature Converter")
        
        # Container for frames
        self.container = Frame(self.root)
        self.container.grid(row=0,column=0)
        
        # Dictionary to hold frames
        self.frames = {}
        
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_cFrame"] = self.create_to_cFrame()
        self.frames["to_fFrame"] = self.create_to_fFrame()
        
        # Show initial frame by calling function show_frame
        self.show_frame("MainFrame")
        
    def show_frame(self, name):
        '''display the required frame from the dictionary'''
        frame = self.frames[name] 
        frame.tkraise()
        
    def run(self):
        '''run the program'''
        self.root.mainloop()
        
    def create_main_frame(self):
        '''Create main menu'''
        # Create a frame for widgets of main menu
        frame = Frame(self.container)
        frame.grid(row=0,column=0)
        
        # Heading
        title = Label(frame, text="Temperature Converter")
        title.grid(row=0,column=0, columnspan=2)
        
        # Buttons
        # To change screen to centigrade
        button_toC = Button(frame, text="to Centigrade", 
                            command=lambda: self.show_frame("to_cFrame"))
        button_toC.grid(row = 1, column = 0)
        
        # To change screen to centigrade
        button_toF = Button(frame, text="to Fahrenheit")
        button_toF.grid(row = 1, column = 1)
        
        # Return frame to show to user
        return frame
        
    def create_to_cFrame(self):
        frame = Frame(self.container)
        frame.grid(row = 0, column = 0)
        
        # Heading
        title = Label(frame, text="convert to C")
        title.grid(row = 0, column = 0)
        
        return frame
    
    def create_to_fFrame(self):
        pass
    
# Main program
if __name__ == "__main__":
    app = Program()
    app.run()