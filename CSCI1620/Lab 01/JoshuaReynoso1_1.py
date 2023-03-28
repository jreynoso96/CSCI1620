def main_menu(c,s,w,co):
    print("----MAIN MENU----\ns: Shop \nx: Exit")
    while True:
        user_input = str(input("Please select an option from above: ").strip())
        if user_input == 's' or user_input == 'S':
            return cart_menu(c,s,w,co)
        elif user_input == 'x' or user_input == 'X':
            return main(c,s,w,1)
        print("Invalid. Please select valid response")
    return

def cart_menu(c,s,w,co):
    print("----CART MENU----\n1: Cookie - $1.50\n2: Sandwhich - $4.00\n3: Water - $1.00")
    temp_cookie = c
    temp_sandwhich = s
    temp_water = w
    while True:
        item_num = input("Please select an item from above: ")
        if item_num.isnumeric():
            if int(item_num) > 0 and int(item_num) < 4:
                if int(item_num) == 1:
                    return main(temp_cookie+1,temp_sandwhich,temp_water,0)
                if int(item_num) == 2:
                    return main(temp_cookie,temp_sandwhich+1,temp_water,0)
                if int(item_num) == 3:
                    return main(temp_cookie,temp_sandwhich,temp_water+1,0)
        print("Invalid. Please select valid response")

def main(in_cookie, in_sandwhich, in_water, checkout):
    cookie = in_cookie
    sandwhich = in_sandwhich
    water = in_water
    total = cookie * 1.50 + sandwhich * 4.00 + water * 1.00

    if checkout == 1:
        return print('-----------------\n('
                     + format(cookie, '.0f') + ') - Cookie = $' + format((cookie * 1.50),'.2f')+'\n('
                     + format(sandwhich, '.0f') + ') - Sandwhich = $' + format((sandwhich * 4.00), '.2f') + '\n('
                     + format(water, '.0f') + ') - Water = $' + format((water * 1.00), '.2f') + '\n'
                     + '-----------------\nGRAND TOTAL = $' +  format((total),'.2f')
                     )
    main_menu(in_cookie, in_sandwhich, in_water,checkout)

if __name__ == '__main__':
    main_menu(0.00,0.00,0.00,0)