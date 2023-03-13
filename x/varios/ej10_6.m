t = linspace(0,8e-3,1000);
v = 8*cos(1000*t);
i = 0.222*cos(1000*t - 56.3*pi/180);
plotyy(t,v,t,i);
xlabel('time(s)');