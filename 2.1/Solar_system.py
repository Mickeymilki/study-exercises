import tkinter as tk
class Planet:
    def __init__(self, name, Diameter, distance_from_TheSun, pozition, description):
      self.name = name
      self.diameter = Diameter
      self.distance_from_TheSun = distance_from_TheSun
      self.pozition = pozition
      self.description = description
      
class TheSun(Planet):
    pass

class Moon(Planet):
    pass

Mercury = Planet( 'Mercury', '4 876 км', '69,8 млн км', '#выводить угол вектора от Солнца', '#описание')
Venus = Planet()
Earth = Planet()
Mars = Planet()
Jupiter = Planet()
Saturn = Planet()
Uranus =Planet()
Neptune = Planet()
Pluto = Planet()

      
    