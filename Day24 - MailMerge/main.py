#read the letter file
with open("./Input/Letters/Letter_template.txt") as letter:
    content = letter.read()

#read the name file as list ...readlines() used for converts as list
with open("./Input/Names/Invited_Names_List.txt") as name_data:
    names_list = name_data.readlines() 


#prepare the letters for each person in the invited names list
for name in names_list:
    stripped_name = name.strip() #--strip method used remove the extra spaces on the name
    replaced_content = content.replace("[Name]", stripped_name)
    with open(f"./Output/Letter_to_{stripped_name}.txt", "w") as Output_letter:
        Output_letter.write(replaced_content)




