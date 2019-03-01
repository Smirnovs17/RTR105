%% Ievads simboliskaja matematika
syms a b c d
syms a2 b2 c2 d2
A = [a b ; c d ];
B = [a2 b2; c2 d2];
C = A*B
%% 1.simbolisko mainigo definešana
syms a b c d
%Seit tiek defineti simboliskie mainigie a b c d
A = [a b ; c d];
A'
% definesim simboliskus mainigus kas nav kompleksi
syms a b c d real
A = [a b; c d];
A'
%% kā definet simboliskos mainigos 2
x = sym('x'); y = sym('y');
y =sqrt(x^2)
% definesim x ka tikai pozitivu mainigu
x = sym('x','positive');
y = sqrt(x^2)
%% ka definet simboliskus mainigus 3
A = sym('a',[2 3])
%% Atvasinašana
syms x
y = diff(x^2)
y = x^2;
diff(y)
% sintakse
% diff(atvasinajuma funkcija, pec ka atvasinat,cik reizes atvasinat)
syms x y
z = x^5*y^4;
diff(z,x)
diff(z,y)
z = x^5;
diff(z,x,2)
%% Integrešana
syms x
int(x^2,x)
% sintekse
% int(integrejuma funkcija,pec ka integret)
%% Noteiktais integralis
int(x,x,0,3)
int(x^2,x,-3,3)
%% Vienadojumu risinašana
syms x 
% saknesbus 5 un 3
% x^2 -8*x+15=0
% 1.pieraksta veids
solve(x^2-8*x+15==0,x)
syms a b c real
solve(a*x^2+b*x+c==0,x)
% 2.pieraksta veids (ko lietoja vecakam matlaba versijam)
solve(x^2-8*x+15,x)
% rakstijam tikai vienadojuma kreiso pusi kreisaja puse ir jabut 0
%% vienadojuma sistemas
% 1.pieraksta veids
syms x y
atb = solve(x-y==-2,x+y==6)
% 2.pieraksta veids
syms x y
atb = solve(x-y+2,x+y-6)
%% izteiksmju vienkaršošana
syms x
y = (x-1)*(x-2)/((x-3)*(x-4))
z = diff(y,x)
simplify(z)
%% citi vienkaršojumi
syms x
y = (x-3)*(x-5)
z = expand(y)
factor(z)
horner(y)
% citam metodem var skatities
syms(x)
methods(x)
%% Robežas
limit(1/(x-1),x,1,'left')
limit(1/(x-1),x,1,'right')
%% simboliskas izteiksmes uzzimešan
y = 1/(x-1);
ezplot(y)
%% simboliskas izteiksmes uzzimešana
% ta bus japilda laborotorijas darbs!
% Dots: f(x)=sqrt(x);
% Atrast f'(x)-?
% Uzzimet intervala [-3,3]
% 1.definesim izteiksmi, atrisinam f'syms x
syms x
y = sqrt(x);
yd=diff(sqrt(x))
% 2.definesim x ka skaitļu vektoru
x = -3:0.01:3;
% 3.izteiksmes vektorizacija
% (ieliksim "." pirms *,/,^)
yv = vectorize(y)
ydv = vectorize(yd)
% 4.ieliksim x ka skaitļu vektoru
yn = eval(yv);
ydn = eval(ydv);
% 5.uzzimesim grafiku
plot(x,yn,x,ydn)
% 6. pieliksim "skaistu" anotaciju
yltx = latex(y)
ydltx = latex(yd)
h = legend(['$',yltx,'$'],['$',ydltx,'$'])
set (h,'Interpreter','latex')
