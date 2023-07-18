import tkinter as tk
from tkinter import filedialog
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas
import json

with open(file="/Users/aagamshah/Documents/Email Bot/config.json", mode="r") as f:
    data = json.load(f)


# <--------------------------------Mail Merge----------------------------->
class Mail_Merge:
    def __init__(self, email_template, directory):
        # Making a separate Dataframe "mail_directory" containing only Founder Names and Company Email Addrs
        data = pandas.read_excel(io=directory)
        self.mail_directory = {
            "company name": data["Company Name"],
            "founder name": data["Founder Name"],
            "email_id": data["Email"]
        }
        self.mail_directory = pandas.DataFrame(self.mail_directory)

        # Reads the mail template
        with open(file=email_template, mode="r") as self.template:
            self.letter_lines = self.template.readlines()
        self.founder_name_loc = []
        self.company_name_loc = []

    def swap(self):

        for index, contact in self.mail_directory.iterrows():
            founder_name = str(contact["founder name"])
            company_name = str(contact["company name"])
            for x in range(len(self.letter_lines)):
                # swaps the [Founder Name] with name
                if "[Founder Name]" in self.letter_lines[x]:
                    self.letter_lines[x] = self.letter_lines[x].replace("[Founder Name]", founder_name)
                    self.founder_name_loc.append(x)
                # swaps the [Company Name] with name
                if "[Company Name]" in self.letter_lines[x]:
                    self.letter_lines[x] = self.letter_lines[x].replace("[Company Name]", company_name)
                    self.company_name_loc.append(x)

            # creates and writes the mail designated to each name
            new_letter = open(file=f"ReadyToSend/{founder_name}.html", mode="w")
            for line in self.letter_lines:
                new_letter.write(line)

            # swaps the name with [Founder Name]
            for x in self.founder_name_loc:
                self.letter_lines[x] = self.letter_lines[x].replace(founder_name, "[Founder Name]")
            # swaps the name with [Company Name]
            for x in self.company_name_loc:
                self.letter_lines[x] = self.letter_lines[x].replace(company_name, "[Company Name]")


# <--------------------------------Mail Send----------------------------->
class Mail_Send:
    def __init__(self, email, db, subject):
        self.html = None
        self.message = None
        self.to_email = None
        self.merger = Mail_Merge(email_template=email, directory=db)
        self.merger.swap()
        # <--------------------Sender's Credentials---------------------------->
        self.my_email = data["email"]
        self.my_password = data["app_password"]
        self.host = data["host"]
        self.port = data["port"]
        self.local_hostname = data["local_hostname"]
        self.subject = subject

    def mail_sending(self):
        for index, contact in self.merger.mail_directory.iterrows():
            self.to_email = contact["email_id"]
            self.message = MIMEMultipart('alternative')
            self.message['Subject'] = self.subject
            self.message['From'] = self.my_email
            self.message['To'] = self.to_email

            # Create the body of the message (an HTML version).
            with open(file=f'''ReadyToSend/{contact["founder name"]}.html''') as self.content:
                self.message.attach(MIMEText(self.content.read(), 'html'))

            with SMTP(host="smtp.gmail.com", port=587, local_hostname="localhost") as self.connection:
                self.connection.starttls()
                self.connection.login(user=self.my_email, password=self.my_password)
                self.connection.sendmail(from_addr=self.my_email, to_addrs=self.to_email, msg=self.message.as_string())
            print(f"Email Sent to {contact['founder name']}!")


# <--------------------------------User Interface----------------------------->
class EmailSenderGUI:
    def __init__(self, master):
        self.master = master
        master.title("Email Sender")

        # Create labels and buttons
        self.excel_label = tk.Label(master, text="Select Excel File:")
        self.excel_label.grid(row=0, column=0)
        self.excel_button = tk.Button(master, text="Browse", command=self.browse_excel)
        self.excel_button.grid(row=0, column=1)

        self.template_label = tk.Label(master, text="Select HTML Email Template:")
        self.template_label.grid(row=1, column=0)
        self.template_button = tk.Button(master, text="Browse", command=self.browse_template)
        self.template_button.grid(row=1, column=1)

        self.subject_label = tk.Label(master, text="Email Subject:")
        self.subject_label.grid(row=2, column=0)
        self.subject_entry = tk.Entry(master)
        self.subject_entry.grid(row=2, column=1)

        self.send_button = tk.Button(master, text="Send Emails", command=self.send_emails)
        self.send_button.grid(row=3, column=1)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.grid(row=4, column=1)

        # Initialize variables
        self.excel_path = None
        self.template_path = None
        self.subject = None

    def browse_excel(self):
        self.excel_path = filedialog.askopenfilename(filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))
        print("Selected Excel file:", self.excel_path)

    def browse_template(self):
        self.template_path = filedialog.askopenfilename(filetypes=(("HTML files", "*.html"), ("All files", "*.*")))
        print("Selected HTML email template file:", self.template_path)

    def send_emails(self):
        # Get the email subject from the entry widget
        self.subject = self.subject_entry.get()
        print("Email subject:", self.subject)

        # Execute the Python script
        print("Sending emails")
        ms = Mail_Send(email=self.template_path, db=self.excel_path, subject=self.subject)
        ms.mail_sending()

        # Show popup message
        popup = tk.Toplevel()
        popup.title("Email Sent!")
        popup_label = tk.Label(popup, text="All Emails are sent")
        popup_label.pack()
        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack()


# <-----------------------------Execution----------------------------->
root = tk.Tk()
my_gui = EmailSenderGUI(root)
root.mainloop()
