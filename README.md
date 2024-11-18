# Badanie położenia punktu względem prostej i przynależności punktu do odcinka

Położenie punktu, odcinka czy prostej określamy na płaszczyźnie kartezjańskiej.  

Położenie punktu wyznaczamy za pomocą liczbowych wartości jego współrzędnych x i y – P(x, y) – które odpowiednio odnoszą się do osi poziomej OX i osi pionowej OY. 

Prosta to krzywa na płaszczyźnie zawierająca w sobie zbiór punktów o współrzędnych spełniających pewne równanie. Jest ona nieograniczona z żadnej strony. 
Równanie prostej może być zapisane w postaci: 
- ogólnej - 0 = Ax + By + C – gdzie A, B i C są liczbami rzeczywistymi i A + B ≠ 0
- kanonicznej (kierunkowej) - y = ax + b – gdzie a jest współczynnikiem kierunkowych i określa kąt nachylenia prostej względem osi OX, a wyraz wolny b wyznacza punkt przecięcia prostej z osią OY

Odcinek to część prostej zawarta pomiędzy dwoma punktami tej prostej, z tymi punktami włącznie. Współrzędne jego krańców odpowiadają współrzędnym ograniczających go punktów. 


# Badanie położenia punktu względem prostej 
Istnieją dwie opcje położenia punktu względem prostej – albo on do niej należy albo nie. 
Żeby sprawdzić która z opcji jest właściwa dla danych prostej i punktu trzeba: 

Wersja A 
podstawić współrzędne punktu P(xp, yp) do równania prostej, najlepiej tego w postaci kierunkowej k: y = ax + b
jeżeli po przyrównaniu wartości obu stron równania zachodzi tożsamość, punkt należy do prostej

Przykładowy program 
KOD PYTHON 

Wersja B
Podstawić współrzędne punktu i dwóch innych punktów należących do prostej do wzoru 
(y-yA)(xB-xA)-(x-xA)(yB-yA)=0
Jeżeli wartość wyrażenia jest równa 0, to punkt należy do prostej

Przykładowy program 
KOD PYTHON

# Badanie przynależności punktu do odcinka 
Sprawdzając czy na płaszczyźnie kartezjańskiej punkt należy do odcinka należy: 
1.	Pobrać współrzędne danego punktu
2.	Pobrać współrzędne 2 punktów ograniczających ten odcinek
3.	Sprawdzić czy punkt należy do prostej według wzoru na prostą przechodzącą przez trzy punkty (funkcja wcześniej)
4.	Jeśli punkt należy do prostej, sprawdzić czy spełnione są warunki 
XC >= min(XA ; XB), XC <= max(XA ; XB) i YC >= min(YA ; YB), YC <= max(YA ; YB) 
5.	Jeśli wszystkie warunki są spełnione to punkt należy do odcinka 


