import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

emails = ["upwork8000@gmail.com","tafreewalaroast@gmail.com"]

def Send_Mails(fromEmail, toEmail, subject, html_content):
    msg = MIMEMultipart()
    msg["From"] = fromEmail
    msg["To"] = toEmail
    msg["Subject"] = subject
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Template</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
        }
        .container {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        .header {
            text-align: center;
            padding-bottom: 20px;
        }
        .header h1 {
            color: #333333;
            font-size: 24px;
        }
        .content {
            padding: 20px 0;
            border-top: 1px solid #e0e0e0;
            border-bottom: 1px solid #e0e0e0;
        }
        .content p {
            margin: 0 0 15px;
            color: #666666;
        }
        .content ul {
            padding: 0 0 0 20px;
            margin: 10px 0;
        }
        .content ul li {
            list-style-type: disc;
            margin-bottom: 5px;
            color: #666666;
        }
        .footer {
            text-align: center;
            padding-top: 20px;
            color: #999999;
            font-size: 14px;
        }
        .footer a {
            color: #999999;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Boost Your Business with Cutting-Edge Web Development and Python Solutions</h1>
        </div>
        <div class="content">
            <p>Dear """ + toEmail + """,</p>
            <p>My name is Abdul Rafay, a passionate Web Developer and Python Programmer. I specialize in creating innovative web solutions that help businesses grow and thrive in the digital world.</p>
            <p>My expertise includes:</p>
            <ul>
                <li>Custom Web Development</li>
                <li>Python Programming</li>
                <li>Responsive Design</li>
                <li>SEO Optimization</li>
                <li>And much more...</li>
            </ul>
            <p>I invite you to explore my portfolio to see some of the projects I've worked on:</p>
            <p><a href="https://portfolio-web-mu-azure.vercel.app/">Portfolio: https://portfolio-web-mu-azure.vercel.app/</a></p>
            <p>You can also connect with me on LinkedIn to stay updated with my latest projects and professional insights:</p>
            <p><a href="https://www.linkedin.com/in/abdulrafaykhan-dev/">LinkedIn Profile: https://www.linkedin.com/in/abdulrafaykhan-dev/</a></p>
            <p>If you have any questions or would like to discuss how I can help your business, please feel free to reach out to me.</p>
            <p>Best regards,<br>Abdul Rafay</p>
        </div>
        <div class="footer">
            <p>Company Inc, 7-11 Commercial Ct, Belfast BT1 2NB<br>
            Don't like these emails? <a href="#">Unsubscribe</a>.</p>
            <p>Powered by <a href="#">HTMLemail.io</a></p>
        </div>
    </div>
</body>
</html>
"""
    # Attach HTML content
    msg.attach(MIMEText(html_content, 'html'))

    try:
        # Connect to SMTP server
        mail_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        mail_server.ehlo()
        
        # Login to SMTP server
        mail_server.login(fromEmail, os.getenv("EMAIL_PASSWORD"))
        
        # Send email message
        mail_server.send_message(msg)
        
        # Quit SMTP server
        mail_server.quit()
        
        print(f"Mail sent to {toEmail} successfully")
    except Exception as e:
        print(f"Error occurred while sending email to {toEmail}: {e}")

# Load sender's email from environment variables
fromEmail = os.getenv("FROM_EMAIL")

# Email subject
subject = "Boost Your Business with Cutting-Edge Web Development and Python Solutions by Abdul Rafay"

# HTML Content


# Send emails to each recipient
for email in emails:
    Send_Mails(fromEmail, email, subject, html_content=None)

print("All Emails Sent Successfully")
