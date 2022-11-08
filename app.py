import csv
import os

csvFilename = 'data_contact.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=== Data Contact ===")
    print("[1] View Contact")
    print("[2] Create Contact")
    print("[3] Edit Contact")
    print("[4] Delete Contact")
    print("[5] Search Contact")
    print("[0] Exit")
    print("===================")
    selected_menu = input("Menu No => ")

    if(selected_menu == "1"):
        show_contact()
    elif(selected_menu == "2"):
        create_contact()
    elif(selected_menu == "3"):
        edit_contact()
    elif(selected_menu == "4"):
        delete_contact()
    elif(selected_menu == "5"):
        search_contact()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Menu is wrong!!!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Press Enter to return")
    show_menu()

def show_contact():
    clear_screen()
    contacts = []
    with open(csvFilename, mode="r") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=",")
        for row in csvReader:
            contacts.append(row)

    if (len(contacts) > 0):

        print("ID \t NAME \t PHONE")
        print("-" * 34)
        for data in contacts:
            print(f"{data['ID']} \t {data['NAME']} \t {data['PHONE']}")
    else:
      print("Data Not Found")

    back_to_menu()

def create_contact():
    clear_screen()
    with open(csvFilename, mode='a') as csvFile:
        fieldNames = ['ID', 'NAME', 'PHONE']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)

        id = input("ID : ")
        name = input("Full Name : ")
        phone = input("Phone Number : ")

        writer.writerow({'ID' : id, 'NAME': name, 'PHONE': phone})
        print("Succes")

    back_to_menu()
def edit_contact():
    clear_screen()
    contacts = []

    with open(csvFilename, mode="r") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            contacts.append(row)

    print("ID \t NAME \t PHONE")
    print("-"*34)

    for data in contacts:
        print(f"{data['ID']} \t {data['NAME']} \t {data['PHONE']}")

    print("-"*12)
    id = input("ID : ")
    name = input("Name Edit : ")
    phone = input("Phone Edit : ")

    #search data contact and change data
    indeks = 0
    for data in contacts:
        if(data['ID'] == id):
            contacts[indeks]['NAME'] = name
            contacts[indeks]['PHONE'] = phone
        indeks = indeks + 1

    #Input New Data to CSV File
    with open(csvFilename, mode="w") as csvFile:
        fieldNames = ['ID', 'NAME', 'PHONE']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
        writer.writeheader()
        for newData in contacts:
            writer.writerow({'ID': newData['ID'],'NAME': newData['NAME'] ,'PHONE': newData['PHONE'] })

    back_to_menu()

def delete_contact():
    clear_screen()
    contacts = []

    with open(csvFilename, mode="r") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            contacts.append(row)

    print("ID \t FULL NAME \t PHONE")
    print("-"*32)

    for data in contacts:
        print(f"{data['ID']} \t {data['NAME']} \t {data['PHONE']}")

    print("-"*12)
    id = input("Delete ID :")

    #search data contact and delete
    indeks = 0
    for data in contacts:
        if (data['ID'] == id):
            contacts.remove(contacts[indeks])
        indeks = indeks + 1

    #Change data contact in file CSV
    with open(csvFilename, mode="w") as csvFile:
        fieldNames = ['ID', 'NAME', 'PHONE']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
        writer.writeheader()
        for newData in contacts:
            writer.writerow({'ID': newData['ID'], 'NAME': newData['NAME'], 'PHONE': newData['PHONE']})

    print("Data Delete!!")
    back_to_menu()

def search_contact():
    clear_screen()
    contacts = []

    with open(csvFilename, mode="r") as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            contacts.append(row)

    id = input("Search By ID > ")

    data_found = []

    #search data contact
    indeks = 0
    for data in contacts:
        if(data['ID'] == id):
            data_found = contacts[indeks]

        indeks = indeks + 1

    if len(data_found) > 0:
        print("DATA FOUND : ")
        print(f"Name: {data_found['NAME']}")
        print(f"Phone: {data_found['PHONE']}")
    else:
        print("Data Not Found")
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()

