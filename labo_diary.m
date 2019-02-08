
	Classroom License -- for classroom instructional use only.

mans_grafiks.m
Undefined variable "mans_grafiks" or class "mans_grafiks.m".
 
mkdir ld0
Warning: Directory already exists. 
cd ld0
mans_grafiks.m
Undefined variable "mans_grafiks" or class "mans_grafiks.m".
 
C = [ 4 5 8];
x = [ -6 -4 -2 0 2 4 6]

x =

    -6    -4    -2     0     2     4     6

x = -6:2:6

x =

    -6    -4    -2     0     2     4     6

y = C(1)*x.^2+C(2)*x+C(3)

y =

   122    52    14     8    34    92   182

plot(x,y)
mans_grafiks.m
Undefined variable "mans_grafiks" or class "mans_grafiks.m".
 
x2 = -6:0.01:6;
y2 = C(1)*x.^2+C(2)x*+C(3);
 y2 = C(1)*x.^2+C(2)x*+C(3);
                    ↑
Error: Invalid expression. Check for missing multiplication operator, missing or unbalanced delimiters, or other
syntax error. To construct matrices, use brackets instead of parentheses.
 
Did you mean:
y2 = C(1)*x.^2 + C(2)*x* + C(3);
%ka zimet vairakus grafikus 2
t = 0:0.01:1;
y1 = sin(2*pi*t);
y2 = cos(2*pi*t);
stem(t,y1)
hold on % iesaldet asis
stem(t,y2)
hold off
xlabel('t,s')
ylabel('signāls,V')
title('Mans pirmais grafiks')
grid
legend('sin','cos')
gtext('\leftarrow sin')
gtext('\alpha \beta \gamma')
gtext('\Omega \omega')

% Lisažu figuras zimešana
edit
lisazu.m
Undefined variable "lisazu" or class "lisazu.m".
 
lisazu
lisazu
lisazu_funkcija(2,3)
lisazu_funkcija(5,9)
lisazu_funkcija(13,7)
lisazu_funkcija(87,63)
lisazu_funkcija(87,24)
lisazu_funkcija(87,24)
lisazu_funkcija(35,18)
lisazu_funkcija(13,7)
lisazu_funkcija(13,7)

lisazu_funkcija(5,7)


lisazu_funkcija(35,18)
Error using pause
Operation terminated by user

Error in lisazu_funkcija (line 8)
pause(0.01)
 

lisazu_funkcija
Not enough input arguments.

Error in lisazu_funkcija (line 5)
x = cos(2*pi*f1*t+i);
 
lisazu_funkcija(5,9)
lisazu_funkcija(5,89)
lisazu_funkcija(5,89)



lisazu_funkcija(35,18)
lisazu_funkcija(450,13)


