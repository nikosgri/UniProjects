/* server.c

   Sample code of 
   Assignment L1: Simple multi-threaded key-value server
   for the course MYY601 Operating Systems, University of Ioannina 

   (c) S. Anastasiadis, G. Kappes 2016

*/


#include <signal.h>
#include <sys/stat.h>
#include "utils.h"
#include "kissdb.h"
#include <time.h>

//------------------------------------------------------------------------------------------------------
//DEFINITIONS

#define MY_PORT                 6767
#define BUF_SIZE                1160
#define KEY_SIZE                 128
#define HASH_SIZE               1024
#define VALUE_SIZE              1024
#define MAX_PENDING_CONNECTIONS   40
#define QUEUE_SIZE 		30

//------------------------------------------------------------------------------------------------------
//DOMES DEDOMENWN

// domi ouras pou periexei ton perigrafea arxeiou kai tin ora enarksis tis sindesis !!!
typedef struct queue {
	
	int socketfd;
	time_t startTime;
	struct timeval tv;
}connection;

// Definition of the operation type.
typedef enum operation {
  PUT,
  GET
} Operation; 

// Definition of the request.
typedef struct request {
  Operation operation;
  char key[KEY_SIZE];  
  char value[VALUE_SIZE];
} Request;

//------------------------------------------------------------------------------------------------------
//GLOBAL METAVLITES

// Definition of the database.
KISSDB *db = NULL;

// metavlites pou  eksipiretoun tin oura ipothetontas oti stin arxi einai adia !
connection fifo[QUEUE_SIZE]; // pinakas pou afora tin oura kai einai koinoxristos !
int head=-1;
int tail=-1;

int size=0;
int stop_pthreads=0;

pthread_t consumerN[4];// tin kano global gia na mporei i terminate na kanei join ta nimata !


long completed_requests=0;
float total_waiting_time=0;
float total_service_time=0;

// MUTEXES
pthread_mutex_t one_at_a_time = PTHREAD_MUTEX_INITIALIZER; // afora tin prospelasi stin oura paragogos - katanalotis 
pthread_mutex_t calculations = PTHREAD_MUTEX_INITIALIZER; // sxetizetai gia ton ipologismo ton metavliton total pou mas dinontai 
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER; // AFORA TOUS GRAFEIS !

//CONDITIONS 
pthread_cond_t  consum = PTHREAD_COND_INITIALIZER;
pthread_cond_t  parag = PTHREAD_COND_INITIALIZER;




//------------------------------------------------------------------------------------------------------
//FUNCTIONS GIA TIN OURA

// tsekarei an einai adia i oura 
int isempty(){
	if(!size)
		return 1;
	return 0;
	
}

//tsekarei an i oura einai gemati 
int isfull(){
	
	if(size==QUEUE_SIZE)
		return 1;//getati 
	return 0;

	
}
 
// akolouthoun sinartiseis eisagogis kai eksogogis stoixeiou apo tin oura !
void insertX(int elem){
	
	
	if(isfull())
		return -1;
	else{
		
		if(tail==QUEUE_SIZE-1) // AN EINAI STIN TELEUTAIA THESI TOU PINAKA 		
			tail=0;
		else
			tail=(tail+1);
	}
	fifo[tail].socketfd=elem;
	gettimeofday(&fifo[tail].tv,NULL);
	fifo[tail].startTime =fifo[tail].tv.tv_usec;//dino stin metavliti pou krataei ton xrono mia sinartisi gia kathisterisi se us kai epeita stin process request to xrisimopoio katallila gia na mporeso na vro to waiting time tis aithshs !
	size++;
}

int   popX(int elem){
	
	if(isempty())
		return -1;
	else{
		if(head==QUEUE_SIZE-1)
			head=0;
		else
			head=(head+1)%QUEUE_SIZE;

	}

	
	elem=fifo[head].socketfd;
	size--;
	return elem;
	
}

//------------------------------------------------------------------------------------------------------
//THREAD FUNCTION
// auto to dimiourgo gia na prostheso se lista osa simata thelo oi katanalotes na agnooun !
static sigset_t signal_mask;
void consumer(const int  socket_fd){	
	
	int pop,fd,ignore;
	struct timeval hold_time;
	long h_usec;
	
	
	while(!stop_pthreads){
    /* Oso i oura mou einai adeia vale kathe nima na perimenei.Otan i oura parei ena dedomeno tha stalthei
     * apo tin main ena sima (pthread_cond_signal(&consum);) opoio nima prolavei kai parei to sima tha bgei
     * apo tin pthread_cond_wait , ta ipoloipa tha sinexisoun na perimenoun na piaoun kapoio sima.
     */
		
    	pthread_mutex_lock(&one_at_a_time);
   	 	if(isempty())
			pthread_cond_wait(&consum,&one_at_a_time);
    /* Se periptosi pou o xristis termatisei to programma (SIGNAL STOP) tha kleithei i terminate.H terminate
     * tha allaksei tin metavliti stop_pthreads se 1 etsi ola ta nimata pou teleionoun kapoia douleia kai
     * pane pali stin arxi tis while tha doun tin allagi kai tha bgoun apo tin while.Meta i terminate tha kanei
     * ena broadcast sto mutex consum giati kapoia nimata endexetai na exoun kollisei perimenontas stin 
     * pthread_cond_wait , to bradcast tha ta ksekolisei kai to if(stop_pthreads) tha ta kanei na termatisoun
     * kai auta
     */
    	if(stop_pthreads)
      		return;
  
    /* EDW EINAI TO KRISIMO SIMEIO GIA TA NIMATA,DEN PREPEI NA EXOUN PROSVASI TAUTOXRONA STIN OURA
     * KATHWS TIN STIGMI POY KAPIO NIMA DIAVAZEI TO socket_fd ENA ALLO MPOREI NA PAREI SIMA KAI NA
     * ARXISEI NA DIAVAZEI KAI AYTO TO IDIO socket_fd KATHWS TO PRWTO DEN PROLAVE NA KANEI popX KAI
     * NA TO AFAIRESEI.
     */
		
		
		pop=popX(fd); //aferese to file descriptor pou dimiourgise i accept stin main
		pthread_cond_signal(&parag);// enimerose oti afairethike stixeio 
		pthread_mutex_unlock(&one_at_a_time);
    	gettimeofday(&hold_time,NULL);
		h_usec=hold_time.tv_usec-fifo[size].tv.tv_usec +(hold_time.tv_sec - fifo[size].tv.tv_sec)*1000000;

		process_request(pop); //Eksipiretise ton client
		
		//gia na agnooun ta nimata to control z
		sigaddset(&signal_mask,SIGTSTP);
		ignore =pthread_sigmask(SIG_BLOCK,&signal_mask,NULL);
	



    	close(pop); //Den mas xreiazetai allo to file descriptor kai to kleinoume
	}

}
//------------------------------------------------------------------------------------------------------
//FUNCTIONS EKSIPIRETISIS CLIENT

/**
 * @name parse_request - Parses a received message and generates a new request.
 * @param buffer: A pointer to the received message.
 *
 * @return Initialized request on Success. NULL on Error.
 */
Request *parse_request(char *buffer) {
  char *token = NULL;
  Request *req = NULL;
  
  // Check arguments.
  if (!buffer)
    return NULL;
  
  // Prepare the request.
  req = (Request *) malloc(sizeof(Request));
  memset(req->key, 0, KEY_SIZE);
  memset(req->value, 0, VALUE_SIZE);

  // Extract the operation type.
  token = strtok(buffer, ":");    
  if (!strcmp(token, "PUT")) {
    req->operation = PUT;
  } else if (!strcmp(token, "GET")) {
    req->operation = GET;
  } else {
    free(req);
    return NULL;
  }
  
  // Extract the key.
  token = strtok(NULL, ":");
  if (token) {
    strncpy(req->key, token, KEY_SIZE);
  } else {
    free(req);
    return NULL;
  }
  
  // Extract the value.
  token = strtok(NULL, ":");
  if (token) {
    strncpy(req->value, token, VALUE_SIZE);
  } else if (req->operation == PUT) {
    free(req);
    return NULL;
  }
  return req;
}

/*
 * @name process_request - Process a client request.
 * @param socket_fd: The accept descriptor.
 *
 * @return
 */
void process_request(const int socket_fd) {
    char response_str[BUF_SIZE], request_str[BUF_SIZE];
    int numbytes = 0;
    Request *request = NULL;
		
	struct timeval service_time,hold_time;
	long s_usec,h_usec;
	
	gettimeofday(&hold_time,NULL);
	h_usec=hold_time.tv_usec-fifo[tail].startTime + 1000000*(hold_time.tv_sec-fifo[tail].tv.tv_sec);
	
	
	// stin sinartisi auti tha ipologistoun ta total service kai wait time !
			
		
    // Clean buffers.
    memset(response_str, 0, BUF_SIZE);
    memset(request_str, 0, BUF_SIZE);
    
    // receive message.
    numbytes = read_str_from_socket(socket_fd, request_str, BUF_SIZE);
    
	
/*		sto shmeio auto tha anaferthoume stous grafeis kai stou anagnostes !
		prepei enas grafeas na tropopoiei tin apothikeush kleidiou timis opote tha prepei na kleidosoume tin perioxi pou ginontai ta put !!
		kai pollaploi anagnostes na kanoun oses anazitiseis theloun ara tis periptoseis pou kanei get tis afinoume os exei giati den mas peirazei auto pou theloume einai na kleidosoume ta put diladi tous grafeis !!
*/



    // parse the request.
    if (numbytes) {
      request = parse_request(request_str);
      if (request) {
        switch (request->operation) {
          case GET:
            // Read the given key from the database.
            if (KISSDB_get(db, request->key, request->value))
              sprintf(response_str, "GET ERROR\n");
            else
              sprintf(response_str, "GET OK: %s\n", request->value);		
            break;
          case PUT:
			//kleidonoume tin periptosi ton put !
			 pthread_mutex_lock(&lock);
            // Write the given key/value pair to the database.
            if (KISSDB_put(db, request->key, request->value)) {
              sprintf(response_str, "PUT ERROR\n");
			  pthread_mutex_unlock(&lock);
			}
            else{
              sprintf(response_str, "PUT OK\n");
			  pthread_mutex_unlock(&lock);	
			}
            break;
          default:
            // Unsupported operation.
            sprintf(response_str, "UNKOWN OPERATION\n");
        }
        // Reply to the client.
        write_str_to_socket(socket_fd, response_str, strlen(response_str));
        if (request)
          free(request);
        
  
      }
    }
	
	gettimeofday(&service_time);
	s_usec=service_time.tv_usec-hold_time.tv_usec + 1000000*(service_time.tv_sec-hold_time.tv_sec);
	printf("request's service time is :%ld microsec\n",s_usec);
	printf("---------------------------------\n");
	pthread_mutex_lock(&calculations);
	completed_requests=completed_requests + 1;
	total_service_time=total_service_time + s_usec;
	total_waiting_time=total_waiting_time + h_usec;
	pthread_mutex_unlock(&calculations);


	
    // Send an Error reply to the client.
    sprintf(response_str, "FORMAT ERROR\n");
    write_str_to_socket(socket_fd, response_str, strlen(response_str));

}
//------------------------------------------------------------------------------------------------------
//FUNCTION GIA TON TERMATISMO TOU PROGRAMATOS OTAN O XRISTIS PATISEI Ctrl+Z

void terminate(){

	int i;


	// enimerose ta nimata na termatisoun !
	stop_pthreads=1;
	//Steile sima se osa nimata perimenoun gia na figoun
	pthread_cond_broadcast(&consum);
	
	

	printf("total service time:%f,total waiting time:%f ,completed request :%ld\n",total_service_time/completed_requests,total_waiting_time/completed_requests,completed_requests);
	

	//apodesmeusi ton nimaton 
	for(i=0;i<4;i++)
		pthread_join(consumerN[i],NULL);


	// Destroy the database.
  	// Close the database.
	KISSDB_close(db);
  	// Free memory.
  	if (db)
    	free(db);
  	db = NULL;
	exit(1);

}
//------------------------------------------------------------------------------------------------------

/*
 * @name main - The main routine.
 *
 * @return 0 on success, 1 on error.
 */
int main() {

  int socket_fd,              // listen on this socket for new connections
      new_fd;                 // use this socket to service a new connection
  socklen_t clen;
  struct sockaddr_in server_addr,  // my address information
                     client_addr;  // connector's address information
	time_t connectTime;
	struct tm *tm_struct;
	int hour,min,sec,insert;
	
	
  // create socket
  if ((socket_fd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
    ERROR("socket()");

  // Ignore the SIGPIPE signal in order to not crash when a
  // client closes the connection unexpectedly.
  signal(SIGPIPE, SIG_IGN);
  
  // create socket adress of server (type, IP-adress and port number)
  bzero(&server_addr, sizeof(server_addr));
  server_addr.sin_family = AF_INET;
  server_addr.sin_addr.s_addr = htonl(INADDR_ANY);    // any local interface
  server_addr.sin_port = htons(MY_PORT);
  
  // bind socket to address
  if (bind(socket_fd, (struct sockaddr *) &server_addr, sizeof(server_addr)) == -1)
    ERROR("bind()");
  
  // start listening to socket for incomming connections
  listen(socket_fd, MAX_PENDING_CONNECTIONS);
  fprintf(stderr, "(Info) main: Listening for new connections on port %d ...\n", MY_PORT);
  clen = sizeof(client_addr);
  
  // Allocate memory for the database.
  if (!(db = (KISSDB *)malloc(sizeof(KISSDB)))) {
    fprintf(stderr, "(Error) main: Cannot allocate memory for the database.\n");
    return 1;
  }
  
  // Open the database.
  if (KISSDB_open(db, "mydb.db", KISSDB_OPEN_MODE_RWCREAT, HASH_SIZE, KEY_SIZE, VALUE_SIZE)) {
    fprintf(stderr, "(Error) main: Cannot open the database.\n");
    return 1;
  }

  //Otan o xristis patisei Ctrl+Z ektelese tin terminate gia na kleiseis ta nimata
  if(signal(SIGTSTP,terminate)==SIG_ERR)	
		exit(1);

	
  /*sto loop pou ksekina apo kato anagnorizoume pos ginete i sindesi sinepos prosthetoume kodika  gia tin ora pou ksekina i sindesi kathos episis elegxoume an i oura einai gemati me skopo ... auto to kanoume gia na min epitrepsoume ston paragogo na prothesi stoixeio stin oura epeita an den einai prosthetoume ston pinaka pou sxetizete me tin oura to new_fd perigrafea arxeiou kathos kai tin ora sindesis tis sindesis */ 

   for(int i=0;i<4;i++){
	 	pthread_create(&consumerN[i],NULL,consumer,&socket_fd);
  }
	
  // main loop: wait for new connection/requests
  while (1) { 
    // wait for incomming connection
   	 if ((new_fd = accept(socket_fd, (struct sockaddr *)&client_addr, &clen)) == -1) {
      		ERROR("accept()");
    }
	//kodikas pou afora tin ora pou ginetai to connection !
	time(&connectTime);
	tm_struct = localtime(&connectTime);
	hour = tm_struct->tm_hour;
	min = tm_struct->tm_min;
	sec = tm_struct->tm_sec;
	printf("--------------------------------\n");
	printf("The Connection time is %d:%d:%d\n",hour,min,sec);
    fprintf(stderr, "(Info) main: Got connection from '%s'\n", inet_ntoa(client_addr.sin_addr));
	
	pthread_mutex_lock(&one_at_a_time);
	//Oso i oura einai gemati perimene
	while(isfull())
		pthread_cond_wait(&parag,&one_at_a_time);
  	//Prosthese stin oura auto pou peires
	insertX(new_fd); 
	
  	//Steile ena sima sta threads oti kati prostethike sti oura.An ta threads einai kolimena stin
  	//pthread_cond_wait tote tha mas eksipiretisei opoio prolavei kai kleidwsei tin consum.An ola
  	//eksipiretoun kati tote to prwto pou tha teleiwsei tha ksanakleidwsei tin consum kai paei legontas
	pthread_cond_signal(&consum);
	pthread_mutex_unlock(&one_at_a_time);
  }  
	

  return 0; 
}

