import smtplib


class EmailHandler:
    """A class to handle sending emails"""

    def __init__(self, email, password) -> None:
        self.__email = email
        self.__password = password

    def send_email(self, form):
        """Sends email to self"""
        msg = (
            f"Name: {form.name.data}\n"
            f"{f'Company Name: {form.company.data}' if form.company.data else ''}"
            f"Email: {form.email.data}\n"
            f"{f'Message: {form.message.data}' if form.message.data else ''}"
        )
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.__email, password=self.__password)
            connection.sendmail(
                self.__email,
                self.__email,
                msg=f"Subject: You have a new message in your website!\n\n{msg}",
            )
