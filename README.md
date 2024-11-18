# Badanie położenia punktu względem prostej i przynależności punktu do odcinka

## 1. Definicje 
Położenie punktu, odcinka czy prostej określamy na płaszczyźnie kartezjańskiej.  

### PŁASZCZYZNA KARTEZJAŃSKA
*Płaszczyzna kartezjańska* to dwuwymiarowa płaszczyzna współrzędnych utworzona przez przecięcie dwóch prostopadłych linii. Linia pozioma jest znana jako oś OX, a linia pionowa jako oś OY.

### PUNKT
Położenie *punktu* wyznaczamy za pomocą liczbowych wartości jego współrzędnych x i y - **P(x, y)** - które odpowiednio odnoszą się do osi poziomej OX i osi pionowej OY. 


### ODCINEK
*Odcinek* to część prostej zawarta **pomiędzy dwoma punktami** tej prostej, z tymi punktami włącznie. Współrzędne jego krańców odpowiadają współrzędnym ograniczających go punktów. 

### PROSTA
*Prosta* to krzywa na płaszczyźnie zawierająca w sobie zbiór punktów o współrzędnych spełniających pewne równanie. Jest ona nieograniczona z żadnej strony. 
Równanie prostej może być zapisane w postaci: 
- **ogólnej** --->   **0 = Ax + By + C**,

    gdzie **A**, **B** i **C** są liczbami rzeczywistymi i **A + B ≠ 0**

- **kanonicznej (kierunkowej)** --->   **y = ax + b**,

    gdzie **a** jest współczynnikiem kierunkowych i określa kąt nachylenia prostej względem osi OX, a wyraz wolny **b** wyznacza punkt przecięcia prostej z osią OY


## 2. Badanie położenia punktu względem prostej 
Istnieją dwie opcje położenia punktu względem prostej – albo on do niej należy albo nie. 

Żeby sprawdzić, która z opcji jest właściwa dla danych prostej i punktu, trzeba: 

### Wersja A 
podstawić współrzędne punktu **P(x, y)** do równania prostej, najlepiej tego w postaci kierunkowej **k: y = ax + b**. 
Jeżeli po przyrównaniu wartości obu stron równania zachodzi **TOŻSAMOŚĆ**, punkt należy do prostej.

Przykładowy program 
KOD PYTHON 

### Wersja B
podstawić współrzędne punktu i dwóch innych punktów należących do prostej do wzoru 
**(y-yA)(xB-xA)-(x-xA)(yB-yA)=0**.
Jeżeli po przyrównaniu wartości obu stron równania zachodzi **TOŻSAMOŚĆ**, punkt należy do prostej.

Przykładowy program 
KOD PYTHON

## 3. Badanie przynależności punktu do odcinka 
Sprawdzając czy na płaszczyźnie kartezjańskiej punkt należy do odcinka należy: 
1.	Pobrać współrzędne danego punktu
2.	Pobrać współrzędne 2 punktów ograniczających ten odcinek
3.	Sprawdzić czy punkt należy do prostej według wzoru na prostą przechodzącą przez trzy punkty (funkcja wcześniej)
4.	Jeśli punkt należy do prostej, sprawdzić czy spełnione są warunki XC >= min(XA ; XB), XC <= max(XA ; XB) oraz YC >= min(YA ; YB), YC <= max(YA ; YB) 
5.	Jeśli wszystkie warunki są spełnione to punkt należy do odcinka

## 4. Zadania 

## Źródła 
