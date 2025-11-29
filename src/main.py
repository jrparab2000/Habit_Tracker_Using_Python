from reporter import Reporter

def main():
    r = Reporter()
    r.welcome()
    while True:
        number = r.menu()
        if number == 1:
            r.add_user()
        if number == 2:
            r.list_users()
        if number == 3:
            user = r.enter_user()
            if user != "":
                r.user_menu(user)
        if number == 4:
            r.save()
        if number == 5:
            r.u.print_all()
        if number == 6:
            break

if __name__ == "__main__":
    main()