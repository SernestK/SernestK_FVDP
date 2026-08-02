import json
import csv

I_fiction = {"Name":"I",
             "Opening Date":"1/3/2026",
             "Type":"Short Story",
             "Chapter":1,
             "Collected View Date":"1/8/2026",
             "View":50}

II_fiction = {"Name":"II",
             "Opening Date":"1/4/2026",
             "Type":"Short Story",
             "Chapter":1,
             "Collected View Date":"1/8/2026",
             "View":60}

III_fiction = {"Name":"III",
             "Opening Date":"1/5/2026",
             "Type":"Short Story",
             "Chapter":1,
             "Collected View Date":"1/8/2026",
             "View":55}

IV_fiction = {"Name":"IV",
             "Opening Date":"1/6/2026",
             "Type":"Long Story",
             "Chapter":20,
             "Collected View Date":"1/8/2026",
             "View":100}

V_fiction = {"Name":"V",
             "Opening Date":"1/7/2026",
             "Type":"Short Story",
             "Chapter":1,
             "Collected View Date":"1/8/2026",
             "View":40}

VI_fiction = {"Name":"VI",
             "Opening Date":"1/8/2026",
             "Type":"Short Story",
             "Chapter":1,
             "Collected View Date":"1/8/2026",
             "View":0}

my_fiction = {"I_fiction":I_fiction,
              "II_fiction":II_fiction,
              "III_fiction":III_fiction,
              "IV_fiction":IV_fiction,
              "V_fiction":V_fiction,
              "VI_fiction":VI_fiction}

print("This is the fiction data program.")
print("You can search Fiction data including Name, Opening Date, Type, etc.")
print("--------------------------------------------------------------------")
print("MENU \n If you want JSON File,select 1. \n If you want CSV File,select 2. \n Do not want any file,select 3. \n You want to see fiction data,select 4. \n You want to stop the program,select 5.")
key_fiction = my_fiction.keys()
selected_file_number = int(input("Enter the number : "))
print("--------------------------------------------------------------------")
while selected_file_number != 5:
    if selected_file_number == 1:
        json_export_file_name = input("Enter the name for JSON Export File : ")
        with open(f'./{json_export_file_name}.json','w') as json_export_file:
            json.dump(my_fiction,json_export_file)
        print("--------------------------------------------------------------------")
        print("MENU \n If you want JSON File,select 1. \n If you want CSV File,select 2. \n Do not want any file,select 3. \n You want to see fiction data,select 4. \n You want to stop the program,select 5.")
        selected_file_number = int(input("Enter the number : "))
    elif selected_file_number == 2:
        csv_export_file_name = input("Enter the name for CSV Export File : ")
        with open(f'./{csv_export_file_name}.csv',mode='w',newline='') as csv_export_file:
            file_csv = csv.writer(csv_export_file)
            file_csv.writerow(I_fiction.keys())
            for i in my_fiction.keys():
                file_csv.writerow(my_fiction[i].values())
        print("--------------------------------------------------------------------")
        print("MENU \n If you want JSON File,select 1. \n If you want CSV File,select 2. \n Do not want any file,select 3. \n You want to see fiction data,select 4. \n You want to stop the program,select 5.")
        selected_file_number = int(input("Enter the number : "))
    elif selected_file_number == 3:
        print("You do not want any file.")
        print("--------------------------------------------------------------------")
        print("MENU \n If you want JSON File,select 1. \n If you want CSV File,select 2. \n Do not want any file,select 3. \n You want to see fiction data,select 4. \n You want to stop the program,select 5.")
        selected_file_number = int(input("Enter the number : "))
    elif selected_file_number == 4:
        selected_fiction = input("Enter the fiction : ")
        key_fiction = my_fiction.keys()
        if selected_fiction in key_fiction:
            print("---------------------------------------")
            name_data = my_fiction[selected_fiction]["Name"]
            print("Fiction Name : ",name_data)
            openingdate_data = my_fiction[selected_fiction]["Opening Date"]
            print("Opening Date : ",openingdate_data)
            type_data = my_fiction[selected_fiction]["Type"]
            print("Fiction Type : ",type_data)
            chapter_data = my_fiction[selected_fiction]["Chapter"]
            print("Amount of Chapter(s) : ",chapter_data)
            collectedviewdate_data = my_fiction[selected_fiction]["Collected View Date"]
            print("Collected View Date : ",collectedviewdate_data)
            view_data = my_fiction[selected_fiction]["View"]
            print("Fiction View : ",view_data,"View(s)")
            print("---------------------------------------")
            print("--------------------------------------------------------------------")
            print("MENU \n If you want JSON File,select 1. \n If you want CSV File,select 2. \n Do not want any file,select 3. \n You want to see fiction data,select 4. \n You want to stop the program,select 5.")
            selected_file_number = int(input("Enter the number : "))
        else: 
            print("At the moment,The Fiction that you search is not in the author fiction list.")
            for i in key_fiction:
                print(i)
            print("--------------------------------------------------------------------")
            print("MENU \n If you want JSON File,select 1. \n If you want CSV File,select 2. \n Do not want any file,select 3. \n You want to see fiction data,select 4. \n You want to stop the program,select 5.")
            selected_file_number = int(input("Enter the number : "))
    else:
        print("This program have only 5 numbers to operation (1,2,3,4,5)")
        print("MENU \n If you want JSON File,select 1. \n If you want CSV File,select 2. \n Do not want any file,select 3. \n You want to see fiction data,select 4. \n You want to stop the program,select 5.")
        selected_file_number = int(input("Enter the number : "))



