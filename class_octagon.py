import math
import matplorlib.pyplot as mp

class Octagon:
   def __init__(self, side):
    self.side = side
    self.corner = 
    self.k = 1 + math.sqrt(2)

    def octagon(self):
        perimetr = self.side * 8
        area = 2 * self.side ** 2 * self.k
        print(f"Периметр октагона: {perimetr} Площадь октагона: {area}")

    def opis_circle(self):
        r = self.side * math.sqrt((self.k/(self.k-1)))
        a = math.pi * r** 2
        print(f"Радиус описанной окружности: {r} Площадь описанной окружности: {a}")

    def vpis_circle(self):
        rad = self.k / 2 * self.side
        ar = math.pi * rad**2 
        print(f"Радиус вписанной окружности: {rad} Площадь вписанной окружности: {ar}")

    #график
    def grafic(self):
        #вписанная окр-ть
        rad = self.k / 2 * self.side
        #описанная окр-ть
        r = self.side * math.sqrt((self.k/(self.k-1)))

        fig, ax = mp.subplots(figsize=(20, 20))  
        #равное соотношение сторон
        ax.set_aspect('equal')
        x = [R* math.cos(i * self.corner) for i in range(10)] 
        y = [R* math.sin(i * self.corner) for i in range(10)] 
        #Замыкание фигуры
        x.append(x[0])  
        y.append(y[0])
        #октагон
        ax.plot(x,y,color='blue',markersize=10) 
        #описанная окружность
        circle_out = mp.Circle((0, 0), R, color='red', fill=False, label=" График описанной окружности" )

        #Добавляем на график
        ax.add_patch(circle_out)
        #вписанная окружность
        circle_in = mp.Circle((0, 0), r, color='pink', fill=False, label=" График вписанной окружности" ) 
        #Добавляем на график
        ax.add_patch(circle_in) 
        #цвета
        mp.legend() 
        #вывод графика
        mp.show() 
       
    def __del__(self):
        print('Данные удалены',self.side) 

    
