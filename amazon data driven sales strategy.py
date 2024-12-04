

#python to mysql project

# Importing the Libraries
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to connect to the database
def database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='ismailpriya',
        database='person'
    )

# Function to add a user
def add_user():
    name = e1.get()
    age = e2.get()

    print("\n")
    print("employee_name :", name)
    print("employee_age :", age)

    # Clear the entry fields
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

    # SQL database interaction
    try:
        d = database()
        mycursor = d.cursor()
        sql = "INSERT INTO detials (name, age) VALUES (%s, %s)"
        values = (name, age)
        mycursor.execute(sql, values)
        d.commit()

        # Close the cursor and connection
        mycursor.close()
        d.close()
                        
        # Success Message
        messagebox.showinfo(title="Success", message="Data submitted successfully!")

    except mysql.connector.Error as error:
        messagebox.showerror(title="Database Error", message=str(error))

# Creating the main application window
root = tk.Tk()

# Setting the title
root.title("Mini_Project-1")

# Creating a frame
frame = tk.Frame(root)
frame.pack()

# Creating a LabelFrame
L = tk.LabelFrame(frame, text="Database of Employee")
L.grid(row=0, column=0, padx=5, pady=5)

# Creating Widgets under L
L1 = tk.Label(L, text="employee_name: ")
L1.grid(row=0, column=0)
e1 = tk.Entry(L)
e1.grid(row=0, column=1)

L2 = tk.Label(L, text="employee_age: ")
L2.grid(row=1, column=0)
e2 = tk.Entry(L)
e2.grid(row=1, column=1)

# Adding a button to submit the form
submit_btn = tk.Button(frame, text="Submit", command=add_user)
submit_btn.grid(row=1, column=0, pady=10)

# Starting the Tkinter main loop
root.mainloop()
