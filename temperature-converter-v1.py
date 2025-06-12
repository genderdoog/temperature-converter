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
        frame.grid(row = 0, column = 0, sticky="NESW")
        
        # Heading
        title = Label(frame, text="Temperature Converter")
        title.grid(row = 0, column = 0, columnspan=2)
        
        # Buttons
        # To change screen to centigrade
        button_toC = Button(frame, text="to Centigrade", 
                            command=lambda: self.show_frame("to_cFrame"))
        button_toC.grid(row = 1, column = 0)
        
        # To change screen to centigrade
        button_toF = Button(frame, text="to Fahrenheit",
                            command=lambda: self.show_frame("to_fFrame"))
        button_toF.grid(row = 1, column = 1)
        
        # Return frame to show to user
        return frame
        
    def create_to_cFrame(self):
        '''Create converting fahrenheit to celsius window'''
        # Set up frame
        frame = Frame(self.container)
        frame.grid(row = 0, column = 0, sticky="NSEW") # We use sticky so that it fills up the whole window
        
        # Initialise the result label
        self.to_Cresult = IntVar()
        self.to_Cresult.set("Result will appear here (celsius result)") # Set it to nothing when program first starts         
        
        # Heading
        self.title = Label(frame, text="convert to C")
        self.title.grid(row = 0, column = 0, columnspan = 3, sticky="NESW")
        
        # User input box
        self.entry_box = Entry(frame)
        self.entry_box.grid(row = 1, column = 0, columnspan = 3, sticky="NESW")
        
        # Buttons
        # Calculate button
        self.calculate_button = Button(frame, text = "Calculate", command = self.convert_toC)
        self.calculate_button.grid(row = 2, column = 0)
        
        # Back button (return to main menu)
        self.back_button = Button(frame, text = "Back", command=lambda: self.show_frame("MainFrame"))
        self.back_button.grid(row = 2, column = 1)
        
        # Reset button
        self.reset_button = Button(frame, text = "Reset", command = self.reset_entry)
        self.reset_button.grid(row = 2, column = 2)
        
        # Result label
        self.result_label = Label(frame, textvariable = self.to_Cresult)
        self.result_label.grid(row = 3, column = 0, columnspan=3, sticky="NESW")
        
        return frame
    
    def create_to_fFrame(self):
        '''Create converting celsius to fahrenheit window'''
        # Set up frame
        frame = Frame(self.container)
        frame.grid(row = 0, column = 0, sticky="NSEW") # We use sticky so that it fills up the whole window
        
        # Initialise the result label
        self.to_Fresult = IntVar()
        self.to_Fresult.set("Result will appear here (fahrenheit)") # Set it to nothing when program first starts         
        
        # Heading
        self.title = Label(frame, text="convert to F")
        self.title.grid(row = 0, column = 0, columnspan = 3, sticky="NESW")
        
        # User input box
        self.entry_box = Entry(frame)
        self.entry_box.grid(row = 1, column = 0, columnspan = 3, sticky="NESW")
        
        # Buttons
        # Calculate button
        self.calculate_button = Button(frame, text = "Calculate", command = self.convert_toF)
        self.calculate_button.grid(row = 2, column = 0)
        
        # Back button (return to main menu)
        self.back_button = Button(frame, text = "Back", command=lambda: self.show_frame("MainFrame"))
        self.back_button.grid(row = 2, column = 1)
        
        # Reset button
        self.reset_button = Button(frame, text = "Reset", command = self.reset_entry)
        self.reset_button.grid(row = 2, column = 2)
        
        # Result label
        self.result_label = Label(frame, textvariable = self.to_Fresult)
        self.result_label.grid(row = 3, column = 0, columnspan=3, sticky="NESW")        
    
        return frame
    
    
    def convert_toC(self):
        '''Converts temperature from fahrenheit to celsius'''
        self.fahrenheit = int(self.entry_box.get()) # Get user input
        result = (self.fahrenheit - 32) * (5/9) # Calculate result
        
        self.to_Cresult.set(result) # Change the output label to answer
        
        
    def convert_toF(self):
        '''Converts temperature from celsius to fahrenheit'''
        self.celsius = int(self.entry_box.get()) # Get user input
        result = (self.celsius * (9/5)) + 32 # Calculate result
        
        self.to_Fresult.set(result) # Change the output label to answer
        
        
    def reset_entry(self):
        '''Clear entry boxes and output label'''
        self.entry_box.delete(0, END) # Clears user input
        self.to_Cresult.set("") # Resets to blank input
        self.to_Fresult.set("")
        
        
# Main program
if __name__ == "__main__":
    app = Program()
    app.run()