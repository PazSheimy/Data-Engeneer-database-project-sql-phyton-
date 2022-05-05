import sqlite3
import tkinter as tk
from sqlite3 import Error
from tkinter import *
from tkinter import messagebox


# Create connection to database - done
def create_connection(database_file):
    conn = None
    try:
        conn = sqlite3.connect(database_file)
        print("Connection established")
        return conn
    except Error as e:
        print(e)

    return conn


# Create table - done
def create_table(conn, sql_table_create):
    try:
        c = conn.cursor()
        c.execute(sql_table_create)
        conn.commit()
    except Error as e:
        print(e)


# Creates View from 'internships' table that displays companies offering internships
def create_view_companies():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("View: Companies Available")
    # Sets window size
    top.geometry("500x400")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)

    # Creates connection to database
    conn = create_connection('internship.db')
    # Creates cursor
    c = conn.cursor()

    c.execute("SELECT company_name FROM available_companies ")
    rows = c.fetchall()
    results = ""

    for row in rows:
        results += str(row) + "\n"

    conn.commit()

    tk.Label(top, text="The following companies have internships available: ").grid(row=1, column=1)
    tk.Label(top, text=results).grid(row=2)

    main_menu_btn = Button(top, text="Main Menu", command=lambda: return_to_main_menu(top))
    main_menu_btn.grid(row=3, column=1)


# Creates application query window
def application_query_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Application Query")
    # Sets window size
    top.geometry("400x400")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)

    # Creates connection to database
    conn = create_connection('internship.db')
    # Creates cursor
    c = conn.cursor()

    c.execute("SELECT * FROM application")

    rows = c.fetchall()
    results = ""

    for row in rows:
        results += str(row) + "\n"

    conn.commit()

    tk.Label(top, text="Application search results: ").grid(row=1, column=0)
    tk.Label(top, text=results).grid(row=2, column=0)

    main_menu_btn = Button(top, text="Main Menu", command=lambda: return_to_main_menu(top))
    main_menu_btn.grid(row=3, column=0)


# Creates internship query window
def internship_query_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Internship Query")
    # Sets window size
    top.geometry("400x400")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)

    # Creates connection to database
    conn = create_connection('internship.db')
    # Creates cursor
    c = conn.cursor()

    c.execute("SELECT * FROM internships")

    rows = c.fetchall()
    results = ""

    for row in rows:
        results += str(row) + "\n"

    conn.commit()

    tk.Label(top, text="Internship search results: ").grid(row=1, column=0)
    tk.Label(top, text=results).grid(row=2, column=0)

    main_menu_btn = Button(top, text="Main Menu", command=lambda: return_to_main_menu(top))
    main_menu_btn.grid(row=3, column=0)


# Creates new window for 'Application'
def create_application_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Create Application")
    # Sets window size
    top.geometry("400x400")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)

    # Creates connection to database
    conn = create_connection('internship.db')
    # Creates cursor
    c = conn.cursor()

    # Creates display text
    tk.Label(top, text="Please fill in the boxes below:").grid(row=0)
    tk.Label(top, text="Application ID: ").grid(row=1)
    tk.Label(top, text="Internship ID: ").grid(row=2)
    tk.Label(top, text="Applicant Name: ").grid(row=3)
    tk.Label(top, text="Status: ").grid(row=4)
    tk.Label(top, text="Dates: ").grid(row=5)

    # Creates input boxes. '.grid()' function must go on a separate line in order for user data to be saved properly
    box_app_id = Entry(top)
    box_app_id.grid(row=1, column=1)
    box_internship_id = Entry(top)
    box_internship_id.grid(row=2, column=1)
    box_applicant_name = Entry(top)
    box_applicant_name.grid(row=3, column=1)
    box_status = Entry(top)
    box_status.grid(row=4, column=1)
    box_dates = Entry(top)
    box_dates.grid(row=5, column=1)

    submit_button = Button(top, text="Submit Application", command=lambda: confirmation_application_input(box_app_id,
                                                                                                    box_internship_id,
                                                                                                    box_applicant_name,
                                                                                                    box_status,
                                                                                                    box_dates))
    submit_button.grid(row=6, column=1)
    main_menu_btn = Button(top, text="Main Menu", command=lambda: return_to_main_menu(top))
    main_menu_btn.grid(row=6, column=2)


# Creates new window for creating internships
def create_new_internship_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Create New Internship")
    # Sets window size
    top.geometry("400x400")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)

    # Creates connection to database
    conn = create_connection('internship.db')
    # Creates cursor
    c = conn.cursor()

    # Creates display text
    tk.Label(top, text="Please fill in the boxes below:").grid(row=0)
    tk.Label(top, text="Company Name: ").grid(row=1)
    tk.Label(top, text="Internship ID: ").grid(row=2)
    tk.Label(top, text="Application Term: ").grid(row=3)
    tk.Label(top, text="Internship Term: ").grid(row=4)
    tk. Label(top, text="Description: ").grid(row=5)
    tk.Label(top, text="Experience Review: ").grid(row=6)

    # Creates input boxes. '.grid()' function must go on a separate line in order for user data to be saved properly
    box_company_name = Entry(top)
    box_company_name.grid(row=1, column=1)
    box_id = Entry(top)
    box_id.grid(row=2, column=1)
    box_app_term = Entry(top)
    box_app_term.grid(row=3, column=1)
    box_internship_term = Entry(top)
    box_internship_term.grid(row=4, column=1)
    box_description = Entry(top)
    box_description.grid(row=5, column=1)
    box_review = Entry(top)
    box_review.grid(row=6, column=1)

    submit_button = Button(top, text="Save record", command=lambda: confirmation_internship_input(box_company_name,
                                                                                                  box_id,
                                                                                                  box_app_term,
                                                                                                  box_internship_term,
                                                                                                  box_description,
                                                                                                  box_review))
    submit_button.grid(row=7, column=1)
    main_menu_btn = Button(top, text="Main Menu", command=lambda: return_to_main_menu(top))
    main_menu_btn.grid(row=7, column=2)


# Creates a new window for Company registration
def create_company_registration_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Company Registration")
    # Sets window size
    top.geometry("400x400")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)

    # Creates display text
    tk.Label(top, text="Please fill in the boxes below:").grid(row=0)
    tk.Label(top, text="Company ID: ").grid(row=1)
    tk.Label(top, text="Company Name: ").grid(row=2)
    tk.Label(top, text="Location: ").grid(row=3)
    tk.Label(top, text="Internship ID: ").grid(row=4)
    tk.Label(top, text="Description: ").grid(row=5)
    tk.Label(top, text="Positions Available: ").grid(row=6)

    # Creates input boxes. '.grid()' function must go on a separate line in order for user data to be saved properly
    box_company_id = Entry(top)
    box_company_id.grid(row=1, column=1)
    box_name = Entry(top)
    box_name.grid(row=2, column=1)
    box_location = Entry(top)
    box_location.grid(row=3, column=1)
    box_internship_id = Entry(top)
    box_internship_id.grid(row=4, column=1)
    box_description = Entry(top)
    box_description.grid(row=5, column=1)
    box_positions = Entry(top)
    box_positions.grid(row=6, column=1)

    submit_button = Button(top, text="Save record", command=lambda: confirmation_company_input(box_company_id, box_name,
                                                                                               box_location,
                                                                                               box_internship_id,
                                                                                               box_description,
                                                                                               box_positions))
    submit_button.grid(row=7, column=1)
    main_menu_btn = Button(top, text="Main Menu", command=lambda: return_to_main_menu(top))
    main_menu_btn.grid(row=7, column=2)


# Creates a new window for Student registration
def create_student_registration_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Student Registration")
    # Sets window size
    top.geometry("400x400")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)

    # Creates display text
    tk.Label(top, text="Please fill in the boxes below:").grid(row=0)
    tk.Label(top, text="First Name: ").grid(row=1)
    tk.Label(top, text="Last Name: ").grid(row=2)
    tk.Label(top, text="Address: ").grid(row=3)
    tk.Label(top, text="Phone: ").grid(row=4)
    tk.Label(top, text="E-mail: ").grid(row=5)

    # Creates input boxes. '.grid()' function must go on a separate line in order for user data to be saved properly
    box_first = Entry(top)
    box_first.grid(row=1, column=1)
    box_last = Entry(top)
    box_last.grid(row=2, column=1)
    box_address = Entry(top)
    box_address.grid(row=3, column=1)
    box_phone = Entry(top)
    box_phone.grid(row=4, column=1)
    box_email = Entry(top)
    box_email.grid(row=5, column=1)

    submit_button = Button(top, text="Save record", command=lambda: confirmation_student_input(box_first, box_last,
                                                                                               box_address,
                                                                                               box_phone, box_email))
    submit_button.grid(row=6, column=1)
    main_menu_btn = Button(top, text="Main Menu", command=lambda: return_to_main_menu(top))
    main_menu_btn.grid(row=6, column=2)


# Confirms user data collected from 'Application' window is correct and then enters it into database
def confirmation_application_input(application_id, internship_id, applicant, status, dates):
    message = tk.messagebox.askquestion("Confirm submission", "Is all of your information correct?", icon="question")
    if message == "yes":
        try:
            # need connection for cursor to work
            conn = create_connection('internship.db')
            c = conn.cursor()
            c.execute('''INSERT INTO application VALUES (?, ?, ?, ?, ?)''', (application_id.get(), internship_id.get(),
                                                                             applicant.get(), status.get(),
                                                                             dates.get()))
            conn.commit()
            print("Application successfully created!")
        except Error as e:
            print(e)
    else:
        tk.messagebox.showinfo("Return", "Returning to the previous screen...")


# Confirms user data collected from 'Company Registration' window is correct and then enters it into database
def confirmation_company_input(company_id, name, location, internship_id, description, positions):
    message = tk.messagebox.askquestion("Confirm submission", "Is all of your information correct?", icon="question")
    if message == "yes":
        try:
            # need connection for cursor to work
            conn = create_connection('internship.db')
            c = conn.cursor()
            c.execute('''INSERT INTO company VALUES (?, ?, ?, ?, ?, ?)''', (company_id.get(), name.get(),
                                                                            location.get(), internship_id.get(),
                                                                            description.get(),
                                                                            positions.get()))
            conn.commit()
            print("Company registration successful!")
        except Error as e:
            print(e)
    else:
        tk.messagebox.showinfo("Return", "Returning to the previous screen...")


# Confirms user data collected from 'Internships' window is correct and then enters it into database
def confirmation_internship_input(name, id_num, app_term, intern_term, description, review):
    message = tk.messagebox.askquestion("Confirm submission", "Is all of your information correct?", icon="question")
    if message == "yes":
        try:
            # need connection for cursor to work
            conn = create_connection('internship.db')
            c = conn.cursor()
            c.execute('''INSERT INTO internships VALUES (?, ?, ?, ?, ?, ?)''', (name.get(), id_num.get(),
                                                                                app_term.get(), intern_term.get(),
                                                                                description.get(), review.get()))
            conn.commit()
            print("Internship successfully created!")
        except Error as e:
            print(e)
    else:
        tk.messagebox.showinfo("Return", "Returning to the previous screen...")


# Confirms user data collected from 'Student Registration' window is correct and then enters it into database
def confirmation_student_input(first, last, address, telephone, email):
    message = tk.messagebox.askquestion("Confirm submission", "Is all of your information correct?", icon="question")
    if message == "yes":
        try:
            # need connection for cursor to work
            conn = create_connection('internship.db')
            c = conn.cursor()
            c.execute('''INSERT INTO registered_users VALUES (?, ?, ?, ?, ?)''', (last.get(), first.get(),
                                                                                  address.get(),
                                                                                  telephone.get(),
                                                                                  email.get()))
            conn.commit()
            print("Student registration successful!")
        except Error as e:
            print(e)
    else:
        tk.messagebox.showinfo("Return", "Returning to the previous screen...")


# Return to 'Main Menu' prompt. Closes current window if 'yes' is clicked
def return_to_main_menu(current_window):
    message = tk.messagebox.askquestion("Please confirm", "Return to Main Menu?", icon="question")
    if message == "yes":
        current_window.destroy()
    else:
        tk.messagebox.showinfo("Return", "Returning to the previous screen...")


def main():
    # creates database file or connects to database if the file already exists
    conn = create_connection('internship.db')

    # Creates a cursor to execute SQL commands
    c = conn.cursor()

    # Creates main window
    root = Tk()
    root.title("Main Window")

    tk.Label(root, text="Welcome to the internship database. Please choose an option below:").pack()
    # Creation of Main Menu buttons
    tk.Button(root, text="Student Registration", command=create_student_registration_window).pack()
    tk.Button(root, text="Company Registration", command=create_company_registration_window).pack()
    tk.Button(root, text="Create Application", command=create_application_window).pack()
    tk.Button(root, text="Create Internship", command=create_new_internship_window).pack()
    tk.Button(root, text="View: Companies", command=create_view_companies).pack()
    tk.Button(root, text="Query Applications", command=application_query_window).pack()
    tk.Button(root, text="Query Internships", command=internship_query_window).pack()

    # Creation of SQL tables
    sql_create_registered_users_table = '''CREATE TABLE IF NOT EXISTS registered_users (
                    lastname text NOT NULL,
                    firstname text NOT NULL,
                    address text,
                    phone_number text,
                    email text NOT NULL UNIQUE
                    )'''

    # TODO change data type back to Integer for id
    sql_create_internships_table = '''CREATE TABLE IF NOT EXISTS internships (
                        company_name text,
                        internship_id text,
                        application_term text,
                        internship_term text,
                        description text,
                        experience_review text
                        )'''

    # TODO change data type back to Integer for id and positions
    sql_create_company_table = '''CREATE TABLE IF NOT EXISTS company (
                            company_id  text,
                            company_name text,
                            location text,
                            internship_id text,
                            internship_description text,
                            num_of_positions text,
                            primary key (company_id),
                            foreign key (internship_id) references internships
                            )'''

    sql_create_application_table = '''CREATE TABLE IF NOT EXISTS application (
                           application_id integer,
                           internship_id integer,
                           applicant_name text,
                           status text,
                           dates text,
                           primary key (application_id, applicant_name),
                           foreign key (internship_id) references internships
                           )'''

    # Creating of VIEWS
    c.execute('''CREATE VIEW IF NOT EXISTS available_companies AS SELECT company_name, internship_id, 
    application_term, internship_term, description, experience_review FROM internships''')

    if conn is not None:
        # Create 'registered_users' table
        create_table(conn, sql_create_registered_users_table)

        # Create 'internships' table
        create_table(conn, sql_create_internships_table)

        # Create 'company' table
        create_table(conn, sql_create_company_table)

        # Create 'application' table
        create_table(conn, sql_create_application_table)

    else:
        print("Error! Cannot establish connection to database.")

    root.mainloop()


if __name__ == '__main__':
    main()