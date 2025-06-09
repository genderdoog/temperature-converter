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
        self.root.title("Temperature converter")
        
        # Container for frames
        self.container = Frame(self.root)
        
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
        pass
        
    def create_to_cFrame(self):
        pass
    
    def create_to_fFrame(self):
        pass
    
# Main program
if __name__ == "__main__":
    app = Program()
    app.run()