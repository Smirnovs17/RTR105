%% Kā iegut merijuma datus no grafika
% (ja ir dots grafiks *.jpg formatā)
A = imread('bilde1.png');
B = imread('bilde2.png');
% uzzimesim
figure(1),image(A)
figure(2),image(B)
% pa x ir jabut 500-800
%pa y ir jabut 0 - 1
figure(2),image([500 800],[1 0],B)
% y ierakstisim otradi jo image y ass ir otradi
set(gca,'Ydir','normal')
% nolasisim datus 10 - cik ir merijumu punkti
[x,y] = ginput(10)
