/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package AreaCirculo;
import Generadores.Generadores;
import java.util.Scanner;

/**
 *
 * @author David
 */
public class Area {
    Scanner sc;
    int n=0;
    public double[] randuX(){
        
        int a=5,b=1,xi=0,cant=0,x0=0;
        double m=9,ui,u[]=null;
        sc=new Scanner(System.in);
                do{
                    try{
                        System.out.println("Ingrese el valor la semilla: ");
                        x0=sc.nextInt();
                        xi=x0;
                    }catch(Exception ex){
                        System.out.println("La semilla debe ser un numero mayor a cero");
                        x0=0;
                    }
                }while(x0<0);
                do{
                    try{
                        System.out.println("Ingrese el numero de alatorios a generar: ");
                        sc=new Scanner(System.in);
                        cant=sc.nextInt();
                        u=new double[cant];
                    }catch(Exception ex){
                        System.out.println("El numero de aleatorios a generar debe ser mayor a cero");
                        cant=0;
                    }
                }while(cant<0);
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
            u[i-1]=ui;
            
        }
        return u;
    }
    
    public double[] randuY(){
        
        int a=6,b=3,xi=0,cant=0,x0=0;
        double m=11,ui,u[]=null;
        sc=new Scanner(System.in);
                do{
                    try{
                        System.out.println("Ingrese el valor la semilla: ");
                        x0=sc.nextInt();
                        xi=x0;
                    }catch(Exception ex){
                        System.out.println("La semilla debe ser un numero mayor a cero");
                        x0=0;
                    }
                }while(x0<0);
                do{
                    try{
                        System.out.println("Ingrese el numero de alatorios a generar: ");
                        sc=new Scanner(System.in);
                        cant=sc.nextInt();
                        u=new double[cant];
                    }catch(Exception ex){
                        System.out.println("El numero de aleatorios a generar debe ser mayor a cero");
                        cant=0;
                    }
                }while(cant<0);
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
            u[i-1]=ui;
            
        }
        return u;
    }    
    public static void main(String [] args){
        double [] randux=null,randuy=null,xi=null,yi=null;
        double area1=0,area2=0;
        int r=5,k=6,aux=0;
        Area a=new Area();
        
        randux=a.randuX();
        randuy=a.randuY();
        xi=new double[randux.length+randuy.length];
        yi=new double[xi.length];
        //Llena los puntos de x 
        for(int i=0;i<xi.length;i++){
            if(i<randux.length){
                xi[i]=randux[i];
            }
            else{ 
                System.out.println(i);
                xi[i]=randuy[aux];
                aux++;
            }
            
        }       
       //Llena los valores de Y
       for(int i=0;i<=yi.length;i++){
           
           yi[i]=2*k*(xi[i]-1);
       }
       for(int i=0;i<=xi.length;i++){
           double v=(Math.pow(xi[i],2))+(Math.pow(yi[i],2));
           if(v<=(r*r))  area2=v/(xi.length*Math.pow(2*r, 2));
       }
       
       area1=Math.PI*Math.pow(r,2);
        System.out.println("Area Analitica: "+area1+"\n Area calculada: "+area2);
        
    }
    
}
