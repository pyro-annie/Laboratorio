#include <stdio.h>
#include <stdlib.h>
#include <conio.h>


//TAREA #3
/*crear un menu */

void opcion1(){
	char name[20];
	int a, b;
	int suma;
	
	fflush(stdin);
	printf("Ingresa nombre: ");
	gets(name);
	
	printf("Indica primer numero: ");
	scanf("%d",&a);
	printf("Indica segundo numero: ");
	scanf("%d",&b);
	
	suma=a+b;
	
	printf("%s la suma de %d + %d = %d", name, a, b, suma);
}

void opcion2(){
		char name[20];
	int a, b, resta;
	
	fflush(stdin);
	printf("Ingresa nombre: ");
	gets(name);
	
	printf("Indica primer numero: ");
	scanf("%d",&a);
	printf("Indica segundo numero: ");
	scanf("%d",&b);
	
	resta=a+b;
	
	printf("%s la resta de %d + %d = %d", name, a, b, resta);
}

void opcion3(){
	char name[20];
	int a, b, mult;
	fflush(stdin);
	
	printf("Ingresa nombre: ");
	gets(name);
	
	printf("Indica primer numero: ");
	scanf("%d",&a);
	printf("Indica segundo numero: ");
	scanf("%d",&b);
	
	mult=a+b;
	
	printf("%s la multiplicacion de %d + %d = %d",name, a, b, mult);
}

void opcion4(){
	char name[20];
	float a, b, divisioon;
	
	fflush(stdin);
	printf("Ingresa nombre: ");
	gets(name);
	
	printf("Indica primer numero: ");
	scanf("%d",&a);
	printf("Indica segundo numero: ");
	scanf("%d",&b);
	
	divisioon=a+b;
	
	printf("%s la division de %.2f + %.2f = %.2f",name, a, b, divisioon);
}


int main(){
	int op;
		
	printf("BIENVENIDO AL MENU\n");
	printf("1. Sumar\n");
	printf("2. Resta\n");
	printf("3. Multiplicacion\n");
	printf("4. Division\n");
	printf("0. Salir\n");
	scanf("%d",&op);
	
	
	switch(op){
		case 1:
			opcion1();
			break;
			
		case 2:
			opcion2();
			break;
			
		case 3:
			opcion3();
			break;
			
		case 4:
			opcion4();
			break;
		
		default:
			printf("Opcion no valida\n");
			break;				
		
		
	}
	
	
	return 0;
}