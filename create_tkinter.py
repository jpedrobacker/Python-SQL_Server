import pyodbc
import os
from dotenv import load_dotenv
import customtkinter

load_dotenv()

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = os.getenv('server_name')

# Main code to create a tkinter window
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("200x300")
app.title('CREATE-CONNECT MS DATABASE')

# Main code to create a box to type the DataBase
entry_database = customtkinter.CTkEntry(app, placeholder_text="Database name")
entry_database.place(relx=0.1, rely=0.1)

# Main code to connect to a data base in SQL server
def	connect_db():
	try:
		connection = pyodbc.connect(f'DRIVER={{{DRIVER_NAME}}};' + f'SERVER={SERVER_NAME};'
								+ f'DATABASE={entry_database.get()};' + 'Trusted_Connection=True')
		info_label.configure(text="Connection Successful!")
	except pyodbc.Error as ex:
		info_label.configure(text="Error to connect!")

# Main code to create a data base in SQL server
def create_db():
	try:
		connection = pyodbc.connect(f'DRIVER={{{DRIVER_NAME}}};' + f'SERVER={SERVER_NAME};'
								+ 'DATABASE=master;' + 'Trusted_Connection=True')
		connection.autocommit = True
		connection.execute(f'create database {entry_database.get()}')
		info_label.configure(text="DataBase Created!")
	except pyodbc.Error as ex:
		info_label.configure(text="Error to create!")

# Buttons to connect and create
connect_button = customtkinter.CTkButton(app, text="Connect", command=connect_db, fg_color="blue")
create_button = customtkinter.CTkButton(app, text="Create", command=create_db, fg_color="green")
connect_button.place(relx=0.1, rely=0.2)
create_button.place(relx=0.1, rely=0.3)

info_label = customtkinter.CTkLabel(app, text="")
info_label.place(relx=0.1, rely=0.4)

app.mainloop()
