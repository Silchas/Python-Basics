import re

string = "Please contact info@carlcare.com for assistance. Phone: (123) 456-7890 or (111) 222-3333"
replacement = "If previous email does not work use care@carlcare.com"


def extract_phone_numbers(string):
    phone_numbers = re.findall(r'\(\d{3}\) \d{3}-\d{4}', string)
    return phone_numbers

phone_numbers = extract_phone_numbers(string)
print(phone_numbers)

def extract_email_addresses(string):
    email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', string)
    return email_addresses

email_addresses = extract_email_addresses(string)
print(email_addresses)

def replace_email_addresses(string, replacement):
    new_string = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', replacement, string)
    return new_string

new_string = replace_email_addresses(string, replacement)
print(new_string)



