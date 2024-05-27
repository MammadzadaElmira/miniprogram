from random import randint


class Yacht:
    def __init__(self, model, production_year, capacity, color, manufacture_country) -> None:
        self.model = model
        self.production_year = production_year
        self.capacity = capacity
        self.color = color
        self.manufacture_country = manufacture_country
        self.passengers = [ ]
        self.speed = 0

    def start_motor(self):
        print("🚢Yacht is moving......")
    
    def stop_motor(self):
        print("🚢Yacht is stopping......")
    
    def add_speed(self, ph):
        self.speed += ph

    def get_youngs(self):
        return len(list(filter(lambda p: p.age >= 15, self.passengers)))
    
    def get_adults(self):
        return len(list(filter(lambda p: p.age <= 45, self.passengers)))
    
    def take_away_passengers(self, passport):
        for passenger in self.passengers:
            if passenger.passport_num == passport:
                self.passengers.remove(passenger)
                return f"{passenger.name} was removed "
    
    
class Passenger:
    def __init__(self, name, age, nationality, gender, passport_num) -> None:
        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender
        self.passport_num = passport_num


passenger_1 = Passenger("Anna", 15, "American", "female", "123Emsdf")
passenger_2 = Passenger("Marina", 25, "Turkish", "female", "Fd23ghfd")
passenger_3 = Passenger("Bob", 32, "Polish", "male", "Abc9876dfg")
passenger_4 = Passenger("Maks", 41, "Russian", "male", "9a7g8dfr")


royal_pearl = Yacht("Royal Pearl", 2024, 150, "white", "America")

print(royal_pearl.model)
print(royal_pearl.production_year)
print(royal_pearl.capacity)
print(royal_pearl.color)
print(royal_pearl.manufacture_country)
royal_pearl.start_motor()
royal_pearl.stop_motor()
royal_pearl.passengers.append(passenger_1)
royal_pearl.passengers.append(passenger_3)
print(len(royal_pearl.passengers))
print(royal_pearl.get_youngs())
print(royal_pearl.get_adults())
print(royal_pearl.take_away_passengers("123Emsdf"))


for _ in range(5):
    royal_pearl.add_speed(randint(25, 100))
    if royal_pearl.speed > 300:
        break

    print(royal_pearl.speed)
print("Yacht is goingg🚢....")