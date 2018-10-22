"""10.2写入文件"""

'''10-3 访客'''

name = input("Please enter your name: ")

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(name.title())
    print("Your name " + name.title() + "hu has been entered！")

'''10-4 访客名单'''

prompt = "\nPlease enter your name: "
prompt += "\n（Enter 'quit' to end the program.）"

while True:
    name = input(prompt)

    if name == 'quit':
        break
    else:
        print("Hello, " + name + "!")
    filename = 'guest_book.txt'

    with open(filename, 'a') as file_object:
        file_object.write(name + " has been login.\n")

'''10-5关于编程的调查'''

prompt = "\nWhy do you like programming？"
prompt += "\n(Enter 'Q' to quit)"

while True:
    reasons = input(prompt)

    if reasons == 'Q':
        break
    else:
        print("Ok, I will record this reason.")

    filename = 'guest_reasons.txt'
    with open(filename, 'a') as file_object:
        file_object.write(reasons + "\n")