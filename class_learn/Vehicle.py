class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self, distance):
        print('花费 %f 小时' % round(distance / self.speed, 2))


class Car(Vehicle):
    def __init__(self, fuel, speed):
        Vehicle.__init__(self, speed)
        self.fuel = fuel

    def drive(self, distance):
        Vehicle.drive(self, distance)
        print('消耗 %f 升油' % (round(distance * self.fuel, 2)))


class Bike(Vehicle):
    pass


b = Bike(15.0)
c = Car(80.0, 0.012)
b.drive(100.0)
c.drive(100.0)


