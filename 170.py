from math import sin , fabs
from time import sleep

def f(x):
    return sin(x)

# Definejam argumenta x robezhas:
a = 1.1
b = 3.2

# Aprekjinam funkcijas vertibas dotajos punktos:
funa = f(a)
funb = f(b)

# paarbaudam, vai dotajaa intrvaalaa ir saknes:
if ( funa * funb > 0.0) :
    print("Dotajaa intervaalaa [%s, %s] saknju nav"%(a,b))
    sleep(1); exit()  # Zinjo uz ekraana, gaida 1 sec. un darbu pabeidz
else:
    print("Dotajaa intervaalaa sakne(s) ir!")

# Defineejam pricizitaati, ar kaadu meklesim sakni:
deltax = 0.01

# Sashaurinam saknes mekleshanas robezhas:
while (fabs(b-a) > deltax):
    x = (a+b)/2; funx = f(x)
    if ((funa*funx = f(x)):
        b = x
    else:
        a = x
print ("Sakne ir: ", x)
