from InitialClass import InitialClass


def initial_test():
    # type: () -> None
    print("Remembering Python knowledge")
    init_object = InitialClass("primero", "otro")
    init_object.print_attributes()


initial_test()
