class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person = Person(name=person["name"], age=person["age"])
        person_list.append(person)
    for person in people:
        if "wife" in person and person["wife"] is not None:
            husband_obj = Person.people[person["name"]]
            wife_obj = Person.people[person["wife"]]
            husband_obj.wife = wife_obj
        elif "husband" in person and person["husband"] is not None:
            wife_obj = Person.people[person["name"]]
            husband_obj = Person.people[person["husband"]]
            wife_obj.husband = husband_obj
    return person_list
