def is_in_line_1(x, y, a, b):
    if(y == a*x + b):
        return("Punkt należy do prostej")
    else:
        return("Punkt nie należy do prostej")

def is_in_line_2(x, y, xa, ya, xb, yb):
    if((y-ya)*(xb-xa)-(x-xa)*(yb-ya) == 0):
        return("Punkt należy do prostej")
    else:
        return("Punkt nie należy do prostej")

def is_in_segment(x, y, xa, ya, xb, yb):
    if((y-ya)*(xb-xa)-(x-xa)*(yb-ya) == 0):
        x_minimum = min(xa, xb)
        y_minimum = min(ya, yb)
        x_maksimum = max(xa,xb)
        y_maksimum = max(ya, yb)
        if (x>=x_minimum and x<=x_maksimum and y>=y_minimum and y<=y_maksimum):
            return("Punkt należy do odcinka")
    else:
        return("Punkt nie należy do odcinka")

if __name__ == '__main__':
    while True:
        try:
            print("Podaj współrzędne x i y punktu")
            x = float(input("x: "))
            y = float(input("y: "))
            break
        except ValueError:
            print("Nieprawidłowy typ wprowadzonych danych! Wprowadź liczbę")

    while True:
        try:
            print("Podaj współczynniki a i b równania prostej w postaci kierunkowej y = a*x + b")
            a = float(input("a: "))
            b = float(input("b: "))
            break
        except ValueError:
            print("Nieprawidłowy typ wprowadzonych danych! Wprowadź liczbę")

    print(is_in_line_1(x, y, a, b))

    while True:
        try:
            print("Podaj współrzędne x i y punktów A i B należących do prostej")
            xA = float(input("Ax: "))
            yA = float(input("Ay: "))
            xB = float(input("Bx: "))
            yB = float(input("By: "))
            break
        except ValueError:
            print("Nieprawidłowy typ wprowadzonych danych! Wprowadź liczbę")

    print(is_in_line_2(x, y, xA, yA, xB, yB))

    print(is_in_segment(x, y, xA, yA, xB, yB))
