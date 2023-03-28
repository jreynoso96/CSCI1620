def main_menu():
    print("----MAIN MENU----\ns: Shop \nx: Exit")
    while True:
        user_input = str(input("Please select an option from above: ").strip())
        if user_input not in ['s','S','x','X']:
            print("Invalid. Please select valid response")
            continue
        else:
            break

    return user_input

def cart_menu():
    print("----CART MENU----\n1: Cookie - $1.50\n2: Sandwhich - $4.00\n3: Water - $1.00")
    while True:
        item_num = input("Please select an item from above: ").strip()
        if item_num.isnumeric():
            if int(item_num) > 0 and int(item_num) < 4:
                return int(item_num)
        print("Invalid. Please select valid response")

def main():
    cookies = 0
    sandwhich = 0
    water = 0

    while True:
        user_input = main_menu()
        print(user_input)
        if user_input == 'x' or user_input == 'X':
            break
        elif user_input == 's' or user_input == 'S':
            item = cart_menu()
            if item == 1:
                cookies += 1
                print("Added cookie")
            elif item == 2:
                sandwhich += 1
                print("Added sandwhich")
            elif item == 3:
                water += 1
                print("Added water")

    total = cookies * 1.50 + sandwhich * 4.00 + water * 1.00
    print('-----------------\n('
          + format(cookies, '.0f') + ') - Cookie = $' + format((cookies * 1.50), '.2f') + '\n('
          + format(sandwhich, '.0f') + ') - Sandwhich = $' + format((sandwhich * 4.00), '.2f') + '\n('
          + format(water, '.0f') + ') - Water = $' + format((water * 1.00), '.2f') + '\n'
          + '-----------------\nGRAND TOTAL = $' + format((total), '.2f')
          )

if __name__ == '__main__':
    main()