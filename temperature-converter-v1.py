"""
Temperature converter in python using tkinter

Created by: Matthew C
Created on: 10/6/25

Version 1: set up the frames and make the buttons work
"""

from tkinter import * 

# Font for buttons
FONT1 = "Arial 10 bold"

# Font for heading in main menu
FONT2 = "Arial 17 bold"

# Padding for buttons
PADDING = 10

class Program:
    
    def __init__(self):
        '''Set up the GUI'''
        # Main window setup
        self.root = Tk()
        self.root.title("Temperature Converter")
        
        # Initialise the celsius result label
        self.to_Cresult = IntVar()
        self.to_Cresult.set("Result will appear here")        
        
        # Initialise the fahrenheit result label
        self.to_Fresult = IntVar()
        self.to_Fresult.set("Result will appear here")           
        
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
        
        # Used in conjunction with sticky to make it fill the window
        frame.columnconfigure([0,1], minsize=150)
        frame.rowconfigure([0,1], minsize=50)
        
        # Heading
        title = Label(frame, text="Temperature Converter", font=FONT2)
        title.grid(row = 0, column = 0, columnspan=2)
        
        # Buttons
        # To change screen to centigrade
        button_toC = Button(frame, text="to Centigrade", bg="yellow", font=FONT1,
                            command=lambda: self.show_frame("to_cFrame"))
        button_toC.grid(row = 1, column = 0, sticky="NESW", padx=PADDING, pady=PADDING)
        
        # To change screen to centigrade
        button_toF = Button(frame, text="to Fahrenheit", bg="#FFB3B3", font=FONT1,
                            command=lambda: self.show_frame("to_fFrame"))
        button_toF.grid(row = 1, column = 1, sticky="NESW", padx=PADDING, pady=PADDING)
        
        # Return frame to show to user
        return frame
        
    def create_to_cFrame(self):
        '''Create converting fahrenheit to celsius window'''
        # Set up frame
        frame = Frame(self.container)
        frame.grid(row = 0, column = 0, sticky="NSEW") # We use sticky so that it fills up the whole window
        
        # Make all the buttons the same size
        frame.columnconfigure([0,1,2], minsize=100)
        
        # Configure height of entrybox
        frame.rowconfigure([1], minsize=25)
        
        # configure height of buttons
        frame.rowconfigure([2], minsize=33)
        
        # Heading
        self.title = Label(frame, text="Enter the temperature in Fahrenheit")
        self.title.grid(row = 0, column = 0, columnspan = 3, sticky="NESW")
        
        # User input box
        self.toC_entry_box = Entry(frame, justify=CENTER)
        self.toC_entry_box.grid(row = 1, column = 0, columnspan = 3, sticky="NESW")
        
        # Buttons
        # Calculate button
        self.calculate_button = Button(frame, text = "Calculate", command = self.convert_toC)
        self.calculate_button.grid(row = 2, column = 0, sticky="NESW")
        
        # Back button (return to main menu)
        self.back_button = Button(frame, text = "Back", command=lambda: self.show_frame("MainFrame"))
        self.back_button.grid(row = 2, column = 1, sticky="NESW")
        
        # Reset button
        self.reset_button = Button(frame, text = "Reset", command=lambda: self.reset_entry("celsius"))
        self.reset_button.grid(row = 2, column = 2, sticky="NESW")
        
        # Result label
        self.result_label = Label(frame, font=FONT1, textvariable = self.to_Cresult)
        self.result_label.grid(row = 3, column = 0, columnspan=3, sticky="NESW")
        
        return frame
    
    def create_to_fFrame(self):
        '''Create converting celsius to fahrenheit window'''
        # Set up frame
        frame = Frame(self.container)
        frame.grid(row = 0, column = 0, sticky="NSEW") # We use sticky so that it fills up the whole window
        
        # Make all the buttons the same size
        frame.columnconfigure([0,1,2], minsize=100)
        
        # Configure height of entrybox
        frame.rowconfigure([1], minsize=25)
        
        # configure height of buttons
        frame.rowconfigure([2], minsize=33)
        
        # Heading
        self.title = Label(frame, text="Enter the temperature in Centigrade")
        self.title.grid(row = 0, column = 0, columnspan = 3, sticky="NESW")
        
        # User input box
        self.entry_box = Entry(frame, justify=CENTER)
        self.entry_box.grid(row = 1, column = 0, columnspan = 3, sticky="NESW")
        
        # Buttons
        # Calculate button
        self.calculate_button = Button(frame, text = "Calculate", command = self.convert_toF)
        self.calculate_button.grid(row = 2, column = 0, sticky="NESW")
        
        # Back button (return to main menu)
        self.back_button = Button(frame, text = "Back", command=lambda: self.show_frame("MainFrame"))
        self.back_button.grid(row = 2, column = 1, sticky="NESW")
        
        # Reset button
        self.reset_button = Button(frame, text = "Reset", command=lambda: self.reset_entry("fahrenheit"))
        self.reset_button.grid(row = 2, column = 2, sticky="NESW")
        
        # Result label
        self.result_label = Label(frame, font=FONT1, textvariable = self.to_Fresult)
        self.result_label.grid(row = 3, column = 0, columnspan=3, sticky="NESW")        
    
        return frame
    
    
    def convert_toC(self):
        '''Converts temperature from fahrenheit to celsius'''
        try:
            self.fahrenheit = float(self.toC_entry_box.get()) # Get user input
            result = (self.fahrenheit - 32) * (5/9) # Calculate result
        
            self.to_Cresult.set(f"{result} C") # Change the output label to answer
        
        except ValueError:
            self.to_Fresult.set("ERROR: Enter only numbers") # Inform user if input is not valid
            
            
    def convert_toF(self):
        '''Converts temperature from celsius to fahrenheit'''
        try:
            self.celsius = float(self.entry_box.get()) # Get user input
            result = ((self.celsius) * (9/5)) + 32 # Calculate result
            
            self.to_Fresult.set(f"{result} F") # Change the output label to answer
        
        except ValueError:
            self.to_Fresult.set("ERROR: Enter only numbers") # Inform user if input is not valid
        
        
    def reset_entry(self, which_entry_box):
        '''Clear entry boxes and output label based on which reset button is pressed'''
        # If we want to clear fahrenheit calculation
        if which_entry_box == "fahrenheit":
            self.entry_box.delete(0, END) # Clears user input
            self.to_Fresult.set("")
        
        # If we want to clear celsius calculation
        elif which_entry_box == "celsius":
            self.toC_entry_box.delete(0, END)
            self.to_Cresult.set("") # Resets to blank input
        
        
# Main program
if __name__ == "__main__":
    app = Program()
    app.run()