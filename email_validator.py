# Email Validator
# Create a class called EmailValidator. Upon initialization it should receive:
# •	min_length (of the username; example: in "peter@gmail.com" "peter" is the username)
# •	mails (list of the valid mails; example: "gmail", "abv")
# •	domains (list of valid domains; example: "com", "net")
# Create three methods that should not be accessed outside the class:
# •	is_name_valid(name) - returns whether the name is greater than or equal to the min_length (True/False)
# •	is_mail_valid(mail) - returns whether the mail is in the possible mails list (True/False)
# •	is_domain_valid(domain) - returns whether the domain is in the possible domains list (True/False)
# Create one public method:
# •	validate(email) - using the three methods returns whether the email is valid (True/False)


class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def is_name_valid(self, name):
        return len(name) >= self.min_length

    def is_mail_valid(self, mail):
        return mail in self.mails

    def is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        name, mail_domain = email.split("@")
        mail, domain = mail_domain.split(".")
        return self.is_name_valid(name) and self.is_mail_valid(mail) and self.is_domain_valid(domain)