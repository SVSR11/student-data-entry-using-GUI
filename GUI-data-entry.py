import tkinter as tk
import csv
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style
from ttkbootstrap.constants import *

fields=['name','class_','section','english','hindi','math','science','sst']
#function to save student info into a csv file
def save_student():                                                                                                                        
    name = entry_name.get()
    class_ = entry_class.get()
    section = entry_section.get()
    marks_english = entry_english.get() or 'NA'
    marks_hindi = entry_hindi.get() or 'NA'
    marks_maths = entry_maths.get() or 'NA'
    marks_science = entry_science.get() or 'NA'
    marks_sst = entry_sst.get() or 'NA'
    if name=='' and class_=='' and section=='':
        messagebox.showinfo("Information", "Name,class and section can not be empty.")
    else:
        with open('student_info.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, class_, section, marks_english, marks_hindi, marks_maths, marks_science, marks_sst])
    
#funtion to clear all data in all the fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_class.delete(0, tk.END)
    entry_section.delete(0, tk.END)
    entry_english.delete(0, tk.END)
    entry_hindi.delete(0, tk.END)
    entry_maths.delete(0, tk.END)
    entry_science.delete(0, tk.END)
    entry_sst.delete(0, tk.END)




def view_students():
    students_window = tk.Toplevel(window)
    students_window.title("Student List")
    
    # Create treeview
    tree = ttk.Treeview(students_window)
    tree['columns'] = ('Name', 'Class')
    
    tree.heading('#0', text='ID',anchor='center')
    tree.heading('Name', text='Name',anchor='center')
    tree.heading('Class', text='Class',anchor='center')
    
    with open('student_info.csv', 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            tree.insert(parent='', index='end', iid=i, text=str(i+1), values=(row[0], row[1]))
        
    tree.bind('<Double-1>', lambda event: view_marks(tree.item(tree.selection())['values'][0]))
    tree.pack()

def view_marks(student_name):
    marks_window = tk.Toplevel(window)
    marks_window.title("Marks Details")
    
    # Create labels
    label_subjects = tk.Label(marks_window, text="Subjects")
    label_subjects.grid(row=0, column=0, padx=5, pady=5)
    label_marks = tk.Label(marks_window, text="Marks")
    label_marks.grid(row=0, column=1, padx=5, pady=5)
    
    subjects = ['English', 'Hindi', 'Maths', 'Science', 'SST']
    
    with open('student_info.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == student_name:
                for i, subject in enumerate(subjects):
                    label_subject = tk.Label(marks_window, text=subject)
                    label_subject.grid(row=i+1, column=0, padx=5, pady=5)
                    label_mark = tk.Label(marks_window, text=row[i+3])
                    label_mark.grid(row=i+1, column=1, padx=5, pady=5)



def select_all(event):
    event.widget.select_range(0, tk.END)
    
                              
# Create the main window
window = tk.Tk()
window.title("Student Information")
window_width = 500
window_height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
#.configure(bg="#4eedcb")

style = Style(theme="solar")
style.configure("TButton", padding=10, font=("Arial", 12))



# Create labels
label_name = tk.Label(window, text="Name:")
label_name.grid(row=0, column=0, padx=5, pady=5)
label_class = tk.Label(window, text="Class:")
label_class.grid(row=1, column=0, padx=5, pady=5)
label_section = tk.Label(window, text="Section:")
label_section.grid(row=2, column=0, padx=5, pady=5)
label_english = tk.Label(window, text="English:")
label_english.grid(row=3, column=0, padx=5, pady=5)
label_hindi = tk.Label(window, text="Hindi:")
label_hindi.grid(row=4, column=0, padx=5, pady=5)
label_maths = tk.Label(window, text="Maths:")
label_maths.grid(row=5, column=0, padx=5, pady=5)
label_science = tk.Label(window, text="Science:")
label_science.grid(row=6, column=0, padx=5, pady=5)
label_sst = tk.Label(window, text="SST:")
label_sst.grid(row=7, column=0, padx=5, pady=5)

# Create entry fields
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1, padx=5, pady=5)
entry_name.bind("<FocusIn>", select_all)
entry_class = tk.Entry(window)
entry_class.grid(row=1, column=1, padx=5, pady=5)
entry_class.bind("<FocusIn>", select_all)
entry_section = tk.Entry(window)
entry_section.grid(row=2, column=1, padx=5, pady=5)
entry_section.bind("<FocusIn>", select_all)
entry_english = tk.Entry(window)
entry_english.grid(row=3, column=1, padx=5, pady=5)
entry_english.bind("<FocusIn>", select_all)
entry_hindi = tk.Entry(window)
entry_hindi.grid(row=4, column=1, padx=5, pady=5)
entry_hindi.bind("<FocusIn>", select_all)
entry_maths = tk.Entry(window)
entry_maths.grid(row=5, column=1, padx=5, pady=5)
entry_maths.bind("<FocusIn>", select_all)
entry_science = tk.Entry(window)
entry_science.grid(row=6, column=1, padx=5, pady=5)
entry_science.bind("<FocusIn>", select_all)
entry_sst = tk.Entry(window)
entry_sst.grid(row=7, column=1, padx=5, pady=5)
entry_sst.bind("<FocusIn>", select_all)

# Create buttons
button_save = ttk.Button(window, text="Save",bootstyle=('PRIMARY', OUTLINE) , command=save_student)
button_save.grid(row=8, column=0, padx=5, pady=5)
button_view = ttk.Button(window, text="View Students",bootstyle=('PRIMARY', OUTLINE), command=view_students)
button_view.grid(row=8, column=1, padx=5, pady=5)
button_clear = ttk.Button(window, text="clear",bootstyle=('PRIMARY', OUTLINE), command=clear_fields)
button_clear.grid(row=8, column=2, padx=5, pady=5)

# Start the main loop
window.mainloop()