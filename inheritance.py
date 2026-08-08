
class GenericAgent:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"{self.name} says: 'System online.'")


class VisionAgent(GenericAgent):
    def __init__(self, name, camera_resolution):
     
        super().__init__(name) 

        self.camera_resolution = camera_resolution 

eye_bot = VisionAgent("Optimus", "4K")

eye_bot.introduce()  
print(eye_bot.camera_resolution) 

