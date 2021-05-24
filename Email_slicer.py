"""
Collect an email address from the user and then find out if the user has a custom
domain name or a popular domain name. For example:
Input: mary.jane@gmail.com
Output: Hey Mary, I see your email is registered with Google. That's cool!.
Input: peter.pan@myfantasy.com
Output: Hey Peter, looks like you've got your own custom setup at MyFantasy. Impressive!.
This is a convenient python project that has a lot of use in the future. The program helps
get you the username and domain name from an email address.
"""
#I'm trying to take the email provider from a dictionary containing providers and domains
email_providers=["Outlook", "Apple", "AOL Mail", "ProtonMail", "Google", "Yahoo", "Hotmail"]
email_domains=["@outlook.com", "@icloud.com", "@aol.com", "@protonmail.com", "@gmail.com", "@yahoo.com", "@hotmail"]
dictio=dict(zip(email_providers, email_domains))

email=input("Please type your email address > ")

#first I need to find the index for '@'
#then slice the string by that index
atindex=email.find('@')
domain=email[atindex:]
username=email[:atindex]
#now I need to try to split a first name from the username
if "_" in username:
    fname=username.find('_')
elif "." in username:
    fname=username.find('.')

if fname:
    first_name = username[:fname]
    first_namet=first_name.title()

for k, v in dictio.items():
    if v==domain:
        dom=k

if domain in email_domains:
    print(f"Hey {first_namet}, looks like your email is registered with {dom}. That's cool!")
else:
    print(f"Hey {first_namet}, looks like you've got your own custom setup at {email[atindex+1:].title()}. Impressive!")

