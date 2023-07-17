import tkinter
from tkinter import messagebox as mb 
from tkinter import filedialog as fd
from export_to_xls import export
from import_to_tbl import import_data
import customtkinter
import os


# function to open a .tbl file  
def openTblFile():  
    try:
        file_name = fd.askopenfilename(
            title = "Select a .tbl file", 
            filetypes = [("Table Files", ".tbl")]
            )
        
        temp_file_name = file_name.split("/")        
        if file_name:
            tbl_file_label.configure(text=temp_file_name[-1], text_color=("green"))
            file_path.initialize(file_name)
    except:
        pass
    
# function to open a .xls file  
def openXlsFile():  
    try:
        file_name = fd.askopenfilename(
            title = "Select a .xlsx file", 
            filetypes = [("Table Files", ".xlsx")]
            )
        
        temp_file_name = file_name.split("/")       
        if file_name:
            xls_file_label.configure(text=temp_file_name[-1], text_color=("green"))
            file_path.initialize(file_name)
    except:
        pass
      
# Function to export .tbl file to .xls
def export_to_xls():
    try:
      status =  export(file_path.get())
      temp_file_name = file_path.get().split("/")
      if status == "done":
            tbl_file_label.configure(text=(f"{temp_file_name[-1]} Converted to .XLS"), text_color=("green"))
      else:
          raise ValueError
    except ValueError:
        tbl_file_label.configure(text=(f"Something went Wrong try again!"), text_color=("red"))
        
        
# Function to export .xls file to .tbl
def import_to_tbl():
    try:
      status =  import_data(file_path.get())
      temp_file_name = file_path.get().split("/")
      if status == "done":
            xls_file_label.configure(text=(f"{temp_file_name[-1]} Converted to .TBL"), text_color=("green"))
      else:
          raise ValueError
    except ValueError:
        xls_file_label.configure(text=(f"Something went Wrong try again!"), text_color=("red"))

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Hero-Online | Table Converter")


# Header Convert TBL to XLS
font = customtkinter.CTkFont(size=20)
title = customtkinter.CTkLabel(app, text="Convert .TBL to .XLSX", font = font)
title.pack(pady=20)

# .tbl File input
file_path = tkinter.StringVar()
file = customtkinter.CTkButton(app, command=openTblFile, text="Select your .tbl file")
file.pack()

# File Label
tbl_file_label = customtkinter.CTkLabel(app, text="⚠️ No file selected!", text_color=("red", "red"))
tbl_file_label.pack()

# Convert to XLS button
convert_to_xls = customtkinter.CTkButton(app, text="Convert", command=export_to_xls, fg_color=("green"), hover_color=("olive"))
convert_to_xls.pack(pady=20)

# Divisor line
line = customtkinter.CTkLabel(app, text="________________________________________________________________________________________")
line.pack()

# Header XLS to TBL
font = customtkinter.CTkFont(size=20)
title = customtkinter.CTkLabel(app, text="Convert .XLSX to .TBL", font = font)
title.pack(pady=20)

# .xls File input
file_path = tkinter.StringVar()
file = customtkinter.CTkButton(app, command=openXlsFile, text="Select your .xls file")
file.pack()

# File Label
xls_file_label = customtkinter.CTkLabel(app, text="⚠️ No file selected!", text_color=("red", "red"))
xls_file_label.pack()

# Convert to XLS button
convert_to_tbl = customtkinter.CTkButton(app, text="Convert", command=import_to_tbl, fg_color=("green"), hover_color=("olive"))
convert_to_tbl.pack(pady=20)



def main():     
# Run app
    app.mainloop()
    
    
if __name__ == "__main__":
    main()