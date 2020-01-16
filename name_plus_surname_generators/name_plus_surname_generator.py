from name_plus_surname_generators import name_generator, surname_generator


def name_plus_surname_generator():
    name = name_generator.name_generator()
    surname = surname_generator.surname_generator()
    name_plus_surname = name, surname
    return name_plus_surname


name_plus_surname_generator()
