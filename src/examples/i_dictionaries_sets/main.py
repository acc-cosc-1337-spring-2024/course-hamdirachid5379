import dictionaries

def display_menu():
    
    print('Inventory Menu:')
    print('1: Add or Update ')
    print('2: Delete ')
    print('3: Exit')
def run_menu():
    widgets = {}
    choice = -1

    while (choice != 3):
        display_menu()
        choice = input('Enter your choice: ')

def handle_menu_option(choice, widgets):

        if choice == '1':
            widget_name = input('Enter your widget: ')
            quantity = int(input('Enter the quantity: '))
            widgets[widget_name] = quantity
            print('Item Added or Updated')

        elif choice == '2':
            widget_name = input('Enter widget to delete: ')
            if widget_name in widgets:
             del widgets[widget_name]
            print('Widget Deleted')
        
        elif choice == '3':
            print('Exiting...')
         
        else:
            print('Invalid option...')




           
