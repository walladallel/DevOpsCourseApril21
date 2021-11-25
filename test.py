end = 0
while end == 0:
    show_list = input('Whould You Like To Print A list Of Users After Deletion? (yes or no)')
    Fl = show_list[0].lower()
    if Fl == ['y']:
        show_list = True
        end = 1
        break
    if Fl == ['n']:
        show_list = False
        end = 1
        break

    if show_list == '' or not Fl in ['y', 'n']:
        print('Please answer with yes or no!')
        show_list = input('Whould You Like To Print A list Of Users After Deletion? (yes or no)')
    else:
        print("showlist is ", Fl)
