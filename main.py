from class_octagon import Octagon

def main():
    Octagon_side=Octagon(float(input('Введите длину стороны октагона в см:')))
    Octagon_side.opis_circle()
    Octagon_side.vpis_circle()
    Octagon_side.octagon()
    Octagon_side.grafik()

if __name__ == '__main__':
    main()
