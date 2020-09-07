Algoritmo TeoremaDePitagoras
	Definir co como real;
	Definir ca Como real;
	Definir hipotenusa_cuadrada como real;
	Definir hipotenusa como real;
	
	Escribir "Ingrese longitud del cateto opuesto en cm: ";
	Leer co;
	
	Escribir "Ingrese longitud del cateto adyacente en cm: ";
	Leer ca;
	
	hipotenusa_cuadrada <- co*co + ca*ca;
	
	hipotenusa <- raiz (hipotenusa_cuadrada);
	
	Escribir "La hipotenusa del triangulo es: ",hipotenusa," cm";
	
FinAlgoritmo
