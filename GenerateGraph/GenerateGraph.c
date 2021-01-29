#include<stdio.h>
#include<stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <string.h>


#define SIZE 100



int  *produceDegrees(int x){   /* here takes the number of vertices where user inputs and  create  5 vertices by giving them a degree */

    static int  deg[(sizeof(x))];
    int sum=0;

    srand(time(NULL));
    int a = x;
    for(int i=0;i<x;i++){
        deg[i]= rand()%a;   /* give random numbers from 0 to x , where x is the number of vertices where user inputs */
    }
    /* declining order!   */
    
    for(int i = 0;i<x;i++){
        for(int j = i+1;j<x;j++){
            if(deg[i]<deg[j]){
                int a = deg[i];
                deg[i]=deg[j];
                deg[j] = a ;
            }
        }
    }
    
    for(int i=0;i<x;i++){
        printf("vert(%d) has degree : %d\n",i,deg[i]);
    }
    
    return deg;
}

bool graphExists(int x,int *deg){

    int take;

    while(1){
        
        if(deg[0]==0) /* if all the elements are equal to zero return true */
            return true; 


        /* Now take the first element  and delete it from the array also at the end we decrise the size of the array . */ 
        take = deg[0];
        if(take<0){
            return false;
        }

        x--;
        for(int i=-1;i<=x;i++){
            deg[i]=deg[i+1];
        }
        // for check
        printf("-------------\n");
        for(int i=0;i<x;i++){
            printf("vert(%d)=%d\n",i,deg[i]);
        }
        
        /*Checking if  we dont have enough elements as the value of the first element of the array says */
        if(take>x)
            return false;

        /* At this loop we take the next "take"(number of the first element we deleted at the array) elements and subtract them with one */
        
        for(int i=0;i<take;i++){
            deg[i]=deg[i] - 1;
            if(deg[i]<0) /* if appears an element with a negative number after subtraction return false */
                return false;
        }
        
        
      /* Makes again the sequence of degrees in a declining order , if it is necessery */
        for(int i = 0;i<x;i++){
            for(int j = i+1;j<x;j++){
                if(deg[i]<deg[j]){
                  int a = deg[i];
                  deg[i]=deg[j];
                  deg[j] = a ;
                }
            }
        }
    }
    
}



void createGraph(int vert , int *deg){ 

    int array[vert][vert]; 
    
    
    /* set all the elements into zero .*/
    for(int i=0;i<vert;i++){
        for(int j=0;j<vert;j++){
            array[i][j]=0;
        }
    }
    

    /* check the degrees of the verteces to find neighbors */
    for(int i=0;i<vert;i++){
        for(int j=i+1;j<vert;j++){
            if(deg[i]>0 && deg[j]>0){
                deg[i]=deg[i]-1;
                deg[j]=deg[j]-1;
                array[i][j] = 1;
                array[j][i] = 1; 
            }
        }
    }


    /*RESULT*/

    printf("----------------------------------\n");
    printf("PRINTING THE GRAPH !\n");

    for(int n=0;n<vert;n++){
        printf("           (%d)",n);
    }
    for(int m=0;m<vert;m++){
        
        printf("  \n  \n  (%d)  ",m);
        for(int l=0;l<vert;l++){
            printf("      %d      " ,array[m][l]);
        }
    }
}


int main(){

    int vertices; /* user sets how many nodes he wants */ 
    int *p;
    int deg[SIZE]; /* array where keeps the degrees of the vertices */
    bool isGraph = true;
    int times=0;
    int newdeg[SIZE];

    printf("IF THE SYSTEM FAIL TO PRODUCE A VALID SEQUENCE OF DEGREES ,IT WILL  LET YOU PUT YOUR OWN SEQUENCE!\n");
    printf("-------------------------------------------------------------------------------------------------------------------\n");

    do{ /*  User must ender at least 2 nodes */ 
        printf("Enter , the number of vertices : \n");
        scanf("%d",&vertices);
        if(vertices<2){
            printf("WARNING : Vertices must be  at least 2 \n");
            printf("--------------------------------------\n");
        }
    }while(vertices<2);

    p=produceDegrees(vertices);  
    if(graphExists(vertices,p)==isGraph){ 
        printf("this sequence of degrees is a graphic! according to hakimi theorem. \n");
        /* DREW THE SEQUENCE IN A GRAPH */
        createGraph(vertices,p);
        /*-----------------------------*/
    }else if (graphExists(vertices,p)!=isGraph){
        printf("this sequence of degrees is not a graphic according to hakimi theorem. \n");
        printf("---------------------------------------------------------------------\n");
        printf("Enter valid degrees for verticies! \n"); /*If the system fails to procude a valid sequence of degrees */
        for(int i=0;i<vertices;i++){
            printf("Input Element %d:",i+1);
            scanf("%d",&newdeg[i]);
        }
        if(graphExists(vertices,newdeg)){
           printf("this sequence of degrees is a graphic! according to hakimi theorem. \n");
            /* DREW THE SEQUENCE IN A GRAPH */
            createGraph(vertices,newdeg);
            /* -----------------------------*/
        }else{
            printf("this sequence of degrees is not a graphic according to hakimi theorem. \n");
        }
    }
    
    return 0;
}
