import admin_and_privileges

main_user = admin_and_privileges.Admin(
    'Max', 'Auramenka', 'titan@tut.by', '19.12.2021'
)
main_user.privileges_list.show_privileges()
