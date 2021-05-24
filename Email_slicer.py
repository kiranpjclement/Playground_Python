"""
Collect an email address from the user and then find out if the user has a custom
domain name or a popular domain name. For example:
Input: mary.jane@gmail.com
Output: Hey Mary, I see your email is registered with Google. That's cool!.
Input: peter.pan@myfantasy.com
Output: Hey Peter, looks like you've got your own custom setup at MyFantasy. Impressive!.
This is a convenient python project that has a lot of use in the future. The program helps
get you the username and domain name from an email address.
If you want to push this further, you can customize the application and send
a message to the host with this information.
"""
#I'm trying to take the email provider from a dictionary containing providers and domains
email_providers=[]
email_domains=[]

email=input("Please type your email address > ")
#print(email)

#first I need to find the index for '@'
#then slice the string by that index
atindex=email.find('@')
#print(atindex)
domain=email[atindex+1:]
#print(domain)
username=email[:atindex]
#print(username)
#now I need to try to split a first name from the username
if "_" in username:
    fname=username.find('_')
elif "." in username:
    fname=username.find('.')

if fname:
    first_name = username[:fname]
    print(first_name)

print(f"Hey {first_name}, looks like your email is registered with {domain}. That's cool!")
print(f"Hey {first_name}, looks like you've got your own custom setup at {domain}. Impressive!")
