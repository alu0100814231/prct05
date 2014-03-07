#!/usr/bin/python
n = int( raw_input('Introduzca el numero entero de intervalos '))
decimalespi = "3.1415926535897931159979634685441852"
suma=0 
for i in range(1,n+1):
  xi = ((i - 0.5)/float(n))
  f_xi = 4/(1+xi**2)
  suma = suma + f_xi
  a = float(i-1)/n
  b = float(i)/n
  print 'Subintervalo: [%f, %f] xi: %f f_xi: %f ' % (a, b, xi, f_xi)
pi = suma/n   
print "El valor aproximado de pi es : ", pi
print "El valor de pi con 35 decimales es: ", decimalespi

  


