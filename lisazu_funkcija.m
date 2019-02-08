function lisazu_funkcija(f1,f2)
t = 0:0.01:1;
%f1=6; f2=4;
for i = 0:pi/100:2*pi
x = cos(2*pi*f1*t+i);
y = sin(2*pi*f2*t);
plot(x,y)
pause(0.01)
end
