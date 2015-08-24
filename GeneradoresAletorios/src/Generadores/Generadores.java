
package Generadores;

import java.util.Scanner;

/**
 *
 * @author David
 */
public class Generadores {
    
    public void GeneradorCongruencial(int x0,int cant){
        double m=9;
        int a=5,b=1,xi=x0;
        double ui;
        System.out.printf("\t"+"%-5s %-1s %-10s %-1s %-10s %-1s %-10s %n","a= "+a," ","   b= "+b," ","m= "+(int)m," ","X0= "+x0);
        System.out.printf("\n\t"+"%-1s %-28s %-1s %n","+","--------------------------------","+");
        System.out.printf("\t"+"%-1s %-6s %-1s %-10s %-1s %-10s %-1s %n","|","  i","|","    Xi","|","    Ui","|");
        System.out.printf("\t"+"%-1s %-6s %-1s %-10s %-1s %-10s %-1s %n","+","------","+","----------","+","----------","+");
          
        for(int i=1;i<=cant;i++){
            xi=(int)((a*xi+b)%m);
            ui=xi/m; 
            System.out.printf("\t"+"%-1s %-6s %-1s %-10s %-1s %.8f %-1s %n","|",i,"|",xi,"|",ui,"|");
            if(i<cant)
                System.out.printf("\t"+"%-1s %-6s %-1s %-10s %-1s %-10s %-1s %n","|","------","+","----------","+","----------","|");
            else
                System.out.printf("\t"+"%-1s %-28s %-1s %n","+","--------------------------------","+");               
            
        }        
    }
    
    
    @SuppressWarnings("empty-statement")
    public void GeneradorMidsquare(int x0,int cant){
                
        int n=0,aux=x0;
        String cuadrado=String.valueOf(x0*x0);
        String ui="0,"+x0,xi;
        
        while(aux>0){  aux=aux/10;n++;}//obtiene el # de cifras de las semilla        
        n=n/2;        
        while(cuadrado.length()<4*n)cuadrado="0"+cuadrado;//Completa con ceros si el cuadrado es menor a 4n la primera vez.
            
        System.out.printf("\t"+"%-10s %-1s %-10s %-1s %-10s %-1s %-10s %n","n= "+n," ","  X0= "+x0," ","  X0^2= "+cuadrado," ","U0= "+ui);
        System.out.printf("\n\t"+"%-1s %-39s %-1s %n","+","---------------------------------------------","+");
        System.out.printf("\t"+"%-1s %-6s %-1s %-10s %-1s %-10s %-1s %-10s %-1s %n","|","  i","|","    Xi","|","   Xi^2","|","    Ui","|");
        System.out.printf("\t"+"%-1s %-6s %-1s %-10s %-1s %-10s %-1s %-10s %-1s %n","+","------","+","----------","+","----------","+","----------","+");
        for(int i=1;i<=cant;i++)
        {   //obtiene la siguiente semila.         
            xi=cuadrado;        
            xi=xi.substring(n);
            xi=xi.substring(0,xi.length()-n);
            //---------------------------
            ui="0,"+xi;
            cuadrado=String.valueOf(Integer.valueOf(xi)*Integer.valueOf(xi));
            while(cuadrado.length()<4*n)cuadrado="0"+cuadrado;//Completa con ceros si el cuadrado es menor a 4n.
            //obtiene la siguiente semila.
            System.out.printf("\t"+"%-1s %-6s %-1s %-10s %-1s %-10s %-1s %-10s %-1s %n","|",i,"|",xi,"|",cuadrado,"|",ui,"|");
            if(i<cant)
                System.out.printf("\t"+"%-1s %-6s %-1s %-10s %-1s %-10s %-1s %-10s %-1s %n","+","------","+","----------","+","----------","+","----------","+");
            else
                System.out.printf("\t"+"%-1s %-39s %-1s %n","+","---------------------------------------------","+");
        }
    }
            
    public static void main(String[]args){
        Scanner sc=new Scanner(System.in);
        int opc,x0,n;
        do{
            try{
            System.out.println("Seleccione una opcion: \n 1. Generador Midsquare \n 2. Generador Congruencial \n 3. Salir.");
            opc=sc.nextInt();
            }catch(Exception ex){
                System.out.println("La entrada debe ser un número natural válido"); 
                opc=0;
            }
        }while(opc<1||opc>3);
        Generadores g=new Generadores();
        switch(opc){
            case 1:
                sc=new Scanner(System.in);
                do{
                    try{
                        System.out.println("Ingrese el valor la semilla: ");
                        x0=sc.nextInt();
                    }catch(Exception ex){
                        System.out.println("La semilla de ser mayor a cero y cantidad de digitos par");
                        x0=0;
                    }
                }while(String.valueOf(x0).length()%2!=0 || x0<=0);
                
                do{
                    try{
                        System.out.println("Ingrese el numero de alatorios a generar: ");
                        sc=new Scanner(System.in);
                        n=sc.nextInt();
                    }catch(Exception ex){
                        System.out.println("El numero de aleatorios a generar debe ser mayor a cero");
                        n=0;
                    }
                }while(n<0);
                g.GeneradorCongruencial(x0, n);
                main(args);
            case 2:
                sc=new Scanner(System.in);
                do{
                    try{
                        System.out.println("Ingrese el valor la semilla: ");
                        x0=sc.nextInt();
                    }catch(Exception ex){
                        System.out.println("La semilla debe ser un numero mayor a cero");
                        x0=0;
                    }
                }while(x0<0);
                do{
                    try{
                        System.out.println("Ingrese el numero de alatorios a generar: ");
                        sc=new Scanner(System.in);
                        n=sc.nextInt();
                    }catch(Exception ex){
                        System.out.println("El numero de aleatorios a generar debe ser mayor a cero");
                        n=0;
                    }
                }while(n<0);
                g.GeneradorCongruencial(x0, n);
                main(args);
            
            case 3: System.exit(0);
                
        }
        
    }
}
