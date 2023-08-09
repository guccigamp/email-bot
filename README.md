# Email Marketing Tool


The Email Marketing Tool is a powerful solution designed to simplify the process of sending bulk emails. It enables you to send personalized emails to a large number of recipients within seconds. By providing an HTML email template with pre-defined content and an email list, the tool replaces the specified attributes in the template with customer information, such as the recipient's name, company name, and more. The customized emails are then sent to the respective recipients' email addresses.

## Features

- **Efficient Email Sending**: The tool automates the process of sending emails, allowing you to reach a large number of recipients in a matter of seconds.
- **Personalization**: Each email is personalized by replacing attributes in the email template with customer information, creating a tailored experience for each recipient.
- **HTML Email Templates**: The tool supports HTML email templates, allowing you to create visually appealing and professional-looking emails.
- **Quick and Easy Setup**: With a few simple steps, you can set up the tool and start sending emails right away.

## Prerequisites

Before using the Email Marketing Tool, ensure that you have the following:

- Python (version 3.7 or above) installed on your machine.
- Access to an SMTP server to send emails. You will need the SMTP server address, port number, and login credentials.

## Installation

Clone the repository:

   ```bash
   git clone https://github.com/guccigamp/email-bot.git
   ```
   Installing the required libraries:

   ```bash
   pip3 install -r requirements.txt
   ```
## Usage
1. Prepare your email template:

Customize the email content as desired, making sure to use placeholders for the attributes you want to replace. In my case, you can use {founder_name} as a placeholder for the recipient's name.

2. Prepare your email list:

Open the email_list.xlsx file in a spreadsheet application or text editor.
Add the necessary customer information, including the email address, recipient's name, company name, and any other relevant attributes. Ensure that the column headers correspond to the placeholders used in the email template.

3. Configure the tool:

Open the config.py file in a text editor.
Provide the required SMTP server details, including the server address, port number, and login credentials. Make sure to update the FROM_EMAIL field with the email address you want to use as the sender.

4. Execute the tool:
   
   ```bash
   python email_bot.py
    ```
5. Sit back and relax!

The tool will process the email list and send personalized emails to each recipient. The console will display the progress and any encountered errors.

## Customization
Adding Additional Attributes: If you want to include more attributes in your email template and email list, follow these steps:

Update the email template, adding the desired placeholders for the new attributes.
Add new columns to the email list Excel file, using appropriate headers for the new attributes.
Modifying the Email Sending Logic: If you wish to customize the email-sending logic, you can modify the send_email() function in the email_bot.py file. Refer to the smtplib documentation for more information on sending emails using Python's SMTP library.

## License
This project is licensed under the MIT License.

## Acknowledgements
The Email Marketing Tool project was inspired by the need for a simple and efficient solution to automate email marketing campaigns. Special thanks to the developers who contributed to this project.

## Contact
For any inquiries or questions, please contact the project maintainer at shahaagam04@gmail.com.


