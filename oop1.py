class SmartPhone:
    def __init__(self, brand,color, battery_level ):
        self.brand = brand 
        self.color = color
        self.battery=  battery_level
        # When we make two different phones:
    def stream_video(self):
        self.battery -= 15
        print(f"Streaming video on your {self.brand}. Battery is now {self.battery}%.")

phone_a = SmartPhone("Apple", "Silver",90)
phone_b = SmartPhone("Samsung", "Black",70)

print(phone_a.battery)
phone_b.stream_video()

