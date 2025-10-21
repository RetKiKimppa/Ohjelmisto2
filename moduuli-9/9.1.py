class Car:
    def __init__(self, plate, top_speed, speed = 0, distance = 0):
        self.plate = plate
        self.top_speed = top_speed
        self.speed = speed
        self.distance = distance

opel = Car("MOR-0", "200 km/h",)

print(f"Plate: {opel.plate}, Top speed: {opel.top_speed}, Speed: {opel.speed}, Distance: {opel.distance}")


