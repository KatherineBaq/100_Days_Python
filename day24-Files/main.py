#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

path_starting_letter = "Input/Letters/starting_letter.txt"
path_names = "Input/Names/invited_names.txt"
path_send_letters = "Output/ReadyToSend/"


with open(path_names) as file:
    names = file.readlines()

for name in names:
    with open(path_starting_letter) as file_sl:
        contents = file_sl.read()
        name_clean = name.strip('\n')
        new_contents = contents.replace("[name]", name_clean)
        print(new_contents)
        with open(f"{path_send_letters}letter_for_{name_clean}", mode="w") as file_send:
            file_send.write(new_contents)

# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew Text")
#
# with open("my_new_file.txt", mode="w") as file:
#     file.write("New file!!")
