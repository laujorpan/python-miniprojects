from InitialClass import InitialClass


def initial_test():
    # type: () -> None
    print("Remembering Python knowledge")
    init_object = InitialClass("primero", "otro")
    print(init_object.attributes_str())


initial_test()
