#Functions with Outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
       return "you didn't provid valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return (f"{formatted_f_name} {formatted_l_name}")
    # print("THIS GOT PRINTED") #this won't be printed because return tells computer its end of Function


formatted_string = format_name(input("whats your first name?"), input("whats your last name"))
print(formatted_string)