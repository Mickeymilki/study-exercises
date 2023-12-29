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
Venus = Planet( 'Venus', '12 103,6 км', '108 млн км', '#выводить угол вектора от Солнца', '#описание')
Earth = Planet( 'Earth', '12 756 км', '149,6 млн км', '#выводить угол вектора от Солнца', '#описание')
Mars = Planet( 'Mars', '6 794 км', 'более 227 млн км', '#выводить угол вектора от Солнца', '#описание')
Jupiter = Planet( 'Jupiter', '139 822 км', '778 млн км', '#выводить угол вектора от Солнца', '#описание')
Saturn = Planet( 'Saturn', '58 232 км','1,4 млрд км', '#выводить угол вектора от Солнца', '#описание')
Uranus =Planet( 'Uranus', '51 000 км', '2,8 млрд км', '#выводить угол вектора от Солнца', '#описание')
Neptune = Planet( 'Neptune', '49 528 км', '4,55 млрд км', '#выводить угол вектора от Солнца', '#описание')
Pluto = Planet( 'Pluto', '2 376 км', '5,9 млрд км', '#выводить угол вектора от Солнца', '#описание')

win = tk.Tk()
icon = tk.PhotoImage(file='logo.png')
win.iconphoto(False, icon)
win.config(bg='window_bg.jpg')
win.geometry(newGeometry="600x600")
win.resizable(True,True)
win.title("Solar system")
win.mainloop()
      
    