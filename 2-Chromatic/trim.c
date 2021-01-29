#include <stdio.h>
#include<stdlib.h>
#include <stdbool.h>
#include<limits.h>



#define SIZE 4


typedef struct Queue{
    int front;
    int near;
    int size;
    unsigned cap; // coritikotita
    int *arr;
}fifo;

struct Queue* createQueue(unsigned capacity) 
{ 
    struct Queue* queue = (struct Queue*)malloc( 
        sizeof(struct Queue)); 
    queue->cap = capacity; 
    queue->front = queue->size = 0; 
  
    // This is important, see the enqueue 
    queue->near = capacity - 1; 
    queue->arr = (int*)malloc( 
        queue->cap * sizeof(int)); 
    return queue; 
} 

int isFull( fifo *queue){

    return (queue->size==queue->cap);

}
int isEmpty(fifo *queue){

    return (queue->size==0);
}
void push(fifo *queue ,int item){

    if(isFull(queue)){
        printf("queue is full!\n");
        return;
    }
    queue->near=(queue->near+1) % queue->cap;
    queue->arr[queue->near]=item;
    queue->size=queue->size+1;

}

int front(fifo *queue){
    if(isEmpty(queue)){
        return INT_MIN;
    }
    return (queue->arr[queue->front]);

}
int near(fifo *queue){
    if(isEmpty(queue)){
        return INT_MIN;   
    }
    return (queue->arr[queue->near]);
}
int pop(fifo *queue){

    if(isEmpty(queue)){
        printf("Empty queue!\n");
        return INT_MIN;
    }
    int item = queue->arr[queue->front];
    queue->front=(queue->front+1) % queue->cap;
    queue->size =queue->size -1;
    return item;
}


bool isBipartiteCheck(int **G,int x,int colorarr[]){

    colorarr[x]=1;
    struct  Queue *queue = createQueue(SIZE);

    push(queue,x);

    do{
        int x=front(queue);
        pop(queue);
        
        if(G[x][x] == 1)
            return false;
        
        for(int i=0;i<SIZE;i++){
            if(G[x][i] && colorarr[i] == -1){
                colorarr[i]= 1-colorarr[x];
                push(queue,i);
            }
            else if(G[x][i] && colorarr[i] == colorarr[x]){
                return false;
            }
        }
    }while(!isEmpty(queue));

    return true;
}
bool isBipartite(int **G){
    
    int colorarr[SIZE];
    /*arxikopoio ton pinaka xromaton me -1 , opou vlepei -1 tha simainei oti autos o komvos den exei xroma .*/
    /*ostoso o arithmos 1 afora ton proto xromatismo kai o arithmos 0 afora ton deutero xromatismo */
    for(int i=0;i<SIZE;i++){
        colorarr[i]= -1;
    }

    for(int i=0;i<SIZE;i++){
        if(colorarr[i]==-1){
            if(isBipartiteCheck(G,i,colorarr)==false){
                return false;
            }
        }
    }


    return true;

}


int main(){

    int rows,cols;
    int **G1;
    int value,insertValue;


   
    
        printf("write down below how many cols and rows has your graph.\n");
        printf("rows=:");
        scanf("%d",&rows);
        printf("cols=:");
        scanf("%d",&cols);

        *G1=(int*)malloc(rows*sizeof(int*));
        if(G1==NULL){
             exit(1);
       }
        for(int i=0;i<rows;i++){
            G1[i]=(int*)malloc(cols*sizeof(int));
            if(G1[i]==NULL){
                exit(1);
            }
        }


        printf("Enter your graph .\n");
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                 printf("G[%d][%d]=",i,j);
                scanf("%d",&G1[i][j]);
            
            }
        } 
        printf("-------------\n");
        printf("\tGRAPH OUTPUT\n");
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                printf("%d ",G1[i][j]);
                if(j==cols-1){
                     printf("\n");
                }
            }
        } 
        printf("\tRESULTS\n");
        if(isBipartite(G1)){
            printf("This graph is 2-Chromatic because it is also bipartite Graph!\n");
            return true; 
        }else{
            printf("This is not a bipartite graph so it is not also a 2-Chromatic graph!\n");
            return false;
        }
        free(G1);
        for(int i=0;i<rows;i++){
            free(G1[i]);
        }
   
    
    return 0;
}