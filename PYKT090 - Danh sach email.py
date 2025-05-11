with open("CONTACT.in", "r") as file:
    emails = file.read().splitlines()

arr_mails = sorted(set(email.lower() for email in emails))

for email in arr_mails:
    print(email)