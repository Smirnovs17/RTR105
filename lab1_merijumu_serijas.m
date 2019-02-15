%% ja ir zdotas merijumu serijas
Um = [-1 0.3 1.5 2.5 3.2]
Im = [1.1 2.2 2.1 3.2 4.7;
      0.9 1.8 2.6 3.3 4.5;
      1.0 2.0 2.4 3.2 4.3;
      0.8 1.9 2.2 3.1 4.4;
      1.1 2.1 2.3 3.2 4.6];
  % katra merijuma serija ir uzdota ka jauna matricas rinda
  % lai rezultats butu pareizs matrica ir jatransporte '
  figure,plot(Um,Im','o-')
  % meklesim videjo vertibu
  Iv = mean(Im)
  % adradisim videjo novirzi
  Ikluda = std(Im)
  % uzzimesim grafiku
  errorbar(Um,Iv,Ikluda)
  % atkal nejauka lauzta linija
  C = polyfit(Um,Iv,4);
  U = -1:0.01:3.2;
  I = polyval(C,U);
  errorbar(Um,Iv,Ikluda)
  hold on
  plot(U,I)
  hold off
  % manuali no grafika janoņem lauzta linija aktivizejam bultiņu figure
  % logā
  %klikšķinam uz linijas ar labo pogu
  %izvelejamies LineStyle none
  
  % 2.variants
  figure
  errorbar(Um,Iv,Ikluda,'o')
  hold on
  plot(U,I)
  hold off