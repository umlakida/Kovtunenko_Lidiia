from copy import deepcopy

class House:
    def __init__(self, area, floors, address, owner):
        self.area = area
        self.floors = floors
        self.address = address
        self.owner = owner

    def __str__(self):
        return f"Площа: {self.area}\nКількість поверхів: {self.floors}\nАдреса: {self.address}\nВласник: {self.owner}"


class ApartmentBuilding(House):
    def __init__(self, area, floors, address, owners):
        super().__init__(area, floors, address, None)
        self.owners = owners

    def __str__(self):
        return f"Площа: {self.area}\nКількість поверхів: {self.floors}\nАдреса: {self.address}\nВласники: {self.owners}"


class Cottage(House):
    def __init__(self, area, floors, address, owner):
        super().__init__(area, floors, address, owner)

    def __str__(self):
        return f"Площа: {self.area}\nКількість поверхів: {self.floors}\nАдреса: {self.address}\nВласник: {self.owner}"


class HouseContainer:
    def __init__(self):
        self.houses = []

    def add(self, house):
        self.houses.append(house)

    def get_by_index(self, index):
        return self.houses[index]

    def get_by_address(self, address):
        for house in self.houses:
            if house.address == address:
                return house
        return None

    def get_all_apartment_buildings(self):
        return [house for house in self.houses if isinstance(house, ApartmentBuilding)]

    def get_all_cottages(self):
        return [house for house in self.houses if isinstance(house, Cottage)]

    def update(self, index, house):
        self.houses[index] = house

    def delete(self, index):
        del self.houses[index]


def main():
    house_prototype = House(100, 5, "вул. Чупринки, 103", "Ковтуненко Л.С.")
    house_container = HouseContainer()

    # Заповнюємо контейнер будинками прототипно
    house_container.add(deepcopy(house_prototype))
    house_container.add(deepcopy(house_prototype))


    print("\t--- Info about houses ---")
    for house in house_container.houses:
        print(house)
        print()

    house_container.update(0, House(200, 10, "вул. Стрийська, 45", "Наливайко Д.Ю."))

    print("\t--- Edited info about houses ---")
    for house in house_container.houses:
        print(house)
        print()

    # print("-----Houses-----")
    # for apartment_building in house_container.get_all_apartment_buildings():
    #     print(apartment_building)
    #     print()
    #
    # print("-----Cottages-----")
    # for cottage in house_container.get_all_cottages():
    #     print(cottage)
    #     print()


if __name__ == "__main__":
    main()
