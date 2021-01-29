#Am:3252 Onoma:Dhmhtrios Epi8eto:Koliatos username:cse3252
#Am:3208 Onona:Nikolaos Epi8eto:Grhgoriadhs username:cse3208

import sys
#desmeumenes le3eis
committed_lets=['program','declare','function','procedure','in','inout','if','else','while','doublewhile','loop','exit','forcase','incase','when','default','not','and','or','call','return','input','print','then']

#statements
state=['program','declare','function','procedure','in','inout','if','else','while','doublewhile','loop','exit','forcase','incase','when','default','call','return','input','print']

#simvola
simbols=['{','}',';',',','[',']',':','(',')','=','<','>','<=','>=','+','-','*','/',':=','==','<>']

#pinakas me ola ta noumera
numbers=['0','1','2','3','4','5','6','7','8','9']

#pinakas me ola ta grammata kefalaia mikra
letters=['A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#anigma arxeiou
file=open(sys.argv[1],"r")

#pinakes gia Scope Entities and Arguments
entities=[]
metavlith=[]
sunatrish=[]
sta8era=[]
parametroi=[]
prosparametros=[]
scopes=[]
arguments=[]
scope = []
joinedlist=[]
	
#lektikos analiths
def lex():
	#pinakas analishs arxeiou
	result=[]
	#le3h enoshs xarakthrwn
	le3h =""
	#ari8mos enoshs ari8mwn
	ari8mos=""
	
	#voi8iitkoi pinakes gia apo8hkeush
	chars=[]
	stoixia=[]
	toke=[]
	xsimb=[]
	lines=[]
	tok=[]	
	
	#apo arxeio se pinaka chars
	while(1):	
		diavase=file.read(1)
		if(diavase==''):
			break
		else:
			chars.append(diavase)
	
	#apoklismo sxoleiwn
	q=0
	while(len(chars)!=q):
		if(chars[q]=='/'):
			if(chars[q+1]=='/'):
				chars[q]=' '
				q+=1
				chars[q]=' '
				q+=1
				while(chars[q]!='\n'):
					chars[q]=' '
					q+=1
				q+=1
			elif(chars[q+1]=='*'):
				chars[q]=' '
				chars[q+1]=' '
				q+=2
				while(chars[q]!='*' or chars[q+1]!='/' ):
					chars[q]=' '
					if(q+2==len(chars)):
						print("Error ,program cannot close because of commends ")
						exit(-1)
					q+=1
				chars[q]=' '
				chars[q+1]=' '
			else:
				q+=1
		else:
			q+=1
	
	#enosh xaraktirwn kai ari8mwn
	for x in chars:
		if(x in letters):
			le3h += x
		elif(x in numbers):
			le3h +=x
		else:
			if(le3h != ""):
				stoixia.append(le3h)
			le3h=""
			stoixia.append(x)

	#egirotita ari8mou
	z=0
	while(len(stoixia)!=z):
		if(stoixia[z].isdigit()):
			if(float(stoixia[z])>32767):
				stoixia[z]='number_error'
		z+=1	

	#poliploka simvola
	a=0
	while(len(stoixia)!=a):
		if(stoixia[a]==':'):
			a+=1
			if(stoixia[a]=='='):
				a+=1
				toke.append(':=')
			else:
				toke.append(':')
		elif(stoixia[a]=='<'):
			a+=1
			if(stoixia[a]=='>'):
				a+=1
				toke.append('<>')	
			elif(stoixia[a]=='='):
				a+=1
				toke.append('<=')
			else:
				toke.append('<')
		elif(stoixia[a]=='>'):
			a+=1
			if(stoixia[a]=='='):
				a+=1
				toke.append('>=')
			else:
				toke.append('>')
		elif(stoixia[a]=='='):
			a+=1
			if(stoixia[a]=='='):
				a+=1
				toke.append('==')	
			else:
				toke.append('=')	
		else:
			toke.append(stoixia[a])
			a+=1

	#egirothta sumbolosirwn
	k=0
	while(len(toke)!=k):
		if(type(toke[k])==int):
			k+=1
		else:
			if(len(toke[k])>30):
				toke[k]='string_error'
			k+=1
	
	#diwxnei ta kena 
	p=0
	while(len(toke)!=p):
		if(toke[p]==' ' or toke[p]=='\t'):
			p+=1
		else:
			xsimb.append(toke[p])
			p+=1

	#katanomi seirwn
	z=0
	j=0
	l=1
	while(len(xsimb)!=z):
		if(xsimb[z]!='\n'):
			tok.append(xsimb[z])
			lines.append(l)
			j+=1
		else:
			l+=1
		z+=1
	
	#diplos pinakas me stoixia kai seires
	result.append(tok)
	result.append(lines)	
	return result 

global allItems   # afora ton arithmo tetradon pou tha paraxthoun stin sinexeia !
global variableList  # einai i lista pou tha xrisimopoihthei stin ilopoisi ton prosorinon met.
allItems=[]
variableList=[] 
counterfor4=1 	#  einai enas counter opou tha mas voithisei na arithmisoume tis tetrades !!
def nextquad():
	global counterfor4
	return counterfor4 # apla tha epistrefei ton antistixo arithmo tetradas 

def genquad(x,y,z,w): 
	#tis dino 4 orismata pou stin ousia einai auta pou tha paragei dld 
	#paradigma 100,:=,a,_,insert  dld ftiaxno tin insert=a kai stin ousia eisago  
	#ton arithmo tetradas dld ton counterfor4 kai epeita ta ipoloipa tha paragoun auto pou tha
	#zitao 
	global counterfor4
	global allItems 
	production=[]
	production =[nextquad()] 
	production += [x] + [y] + [z] + [w]
	#molis ginei locate mia tetrada tha prepei na einai einai se thesi i nextquad otan 
	#ksanaklithei na  mporei na allaksei arithmo kai na dosei epomenis tetradas 
	#i opoia tha perimenei na ilopoithei 
	counterfor4 += 1
	allItems += [production]
	return production

#Voithitiki sinartisei gia tis prosorines metavlites t_i
counter2=1 # afora tin metavliti t_i  opou i=1,2,3...
def newtemp():
	global variable
	global counter2
	global variableList
	newlist = ['T_']
	newlist.append(str(counter2))
	variable = ''.join(newlist)
	counter2 = counter2 + 1
	variableList  +=  [variable]
	return   variable

def emptylist():
	global empty
	empty=[] # dimiourgia kenis listas kai epeita epistrofi 
	return empty 

def makeList(x):
	listX=[x]
	return listX

def merge(list1,list2):
	dimiourgia=[]
	dimiourgia+=list1 + list2
	return  dimiourgia 

def backPatch(list,z):
	# apo diavasma diafaneion auto pou katalabaino einai oti prepei se kathe tetrada pou tha dimiourgeite meso tis genquad() px _,_,_,_ i teleutaia paula se kathe tetrada tha prepei na exei 
	# to gramma z !  diladi _,_,_,z kapos etsi ara me loop tha psakso tin arxiki m allItem lista 
	# kai mexri prin allaksei o counterfor4 pou deixnei se epomeni tetrada tha topotheto 
	# stin teleutaia paula to z 
	i=0
	j=0
	k=4
	while(i<len(list)):
		for j in list:
			if(list[i]==allItems[j-1][0]):
				while(k!=0):
					if(allItems[j-1][k]=="_"):
						allItems[j-1][k]=z
						break
					k=k-1	
		i+=1
		break


#voi8itikes metavlites
mainflag=0
counter=0
bytes = 12
depth=0
dist=0
offset=0

#sintaktikos analitis 
def editorial_analyst():
	global result
	result=lex()
	#voi8itikes metavlites
	global name
	global flag  
	flag = 0

	def program():
		global token
		global onoma
		global mainflag
		global depth
		global bytes
		token=result[0]
		line=result[1]
		global counter	
		if(token[counter]=='program'):
			counter+=1
			if token[counter] not in committed_lets and  token[counter] not in simbols:
				onoma=token[counter]
				counter+=1
				RecordScope(entities,depth)
				if(token[counter]=='{'):
					counter+=1
					block(onoma)
					if(token[counter]=='}'):
						scopes[0][1]=bytes+4
						counter+=1
						return 
					else:
						print('   On line {} :'.format(line[counter]))
						print("Error!, program cant close,  expected '}'")
						exit(-1)
				else:
					print('   On line {} :'.format(line[counter]))
					print("Error! , you might need '{' bracket")
					exit(-1)
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error! , no name of program exists!")
				exit(-1)
		else:
			print('   On line {} :'.format(line[counter]))
			print("Error ,  word 'program' cannot be found ")
			exit(-1)
	
	def block(nameID):
		global token
		global counter
		global mainflag
		token=result[0]
		line=result[1]
		declarations()
		genquad('begin_block',nameID,'_','_')
		subprograms()
		statements()
		if(mainflag==0):
			genquad('halt','_','_','_')
		genquad('end_block',nameID,'_','_')

	def declarations():
		global token
		global counter
		token=result[0]
		line=result[1]	
		if(token[counter]=='declare'):
			counter+=1
			varlist()
			if(token[counter]==';'):
				counter+=1
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error! , you might need ';' bracket ")
				exit(-1)
		return

	def varlist():
		global token
		global counter
		global bytes
		global depth
		global metavlith
		global joinedlist
		metavlith=[]
		joinedlist=[]
		token=result[0]
		line=result[1]
		
		if token[counter] not in committed_lets and  token[counter] not in simbols:
			AddEntityMetavlith(token[counter],"int",bytes)
			bytes += 4
			counter+=1
			while(token[counter]==','):
				counter+=1
				if token[counter] not in committed_lets and  token[counter] not in simbols:
					AddEntityMetavlith(token[counter],"int",bytes)
					bytes += 4					
					counter+=1
				else:
					print('   On line {} :'.format(line[counter]))
					print("Error , Syntax Error ! No id was found!")
					exit(-1)
		
		joinedlist=[]
		joinedlist = parametroi + metavlith
		if(len(scopes[depth][0])==0):
			scopes[depth][0]=metavlith
		else:
			scopes[depth][0].append(metavlith)
		if(len(parametroi)!=0):			
			scopes[depth][0]=joinedlist
		return 

	def subprograms():
		global token
		global counter
		global mainflag
		token=result[0]
		line=result[1]	
		while(token[counter]=='function' or token[counter]=='procedure'):
			subprogram()
		return

	def subprogram():
		global token
		global counter
		global put
		global put2
		global depth
		global metavlith
		global parametroi
		global offset
		global dist
		parametroi=[]
		token=result[0]
		line=result[1]	
		if(token[counter]=='function'):
			counter+=1
			if token[counter] not in committed_lets and  token[counter] not in simbols:
				dist +=1				
				depth += 1
				AddEntityFunction(token[counter],"function","",parametroi,offset)
				RecordScope(entities,depth)
				#parametroi.clear()
				put=token[counter]
				counter+=1
				funcbody(put)
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , expected the name of the function")
				exit(-1)

		elif(token[counter]=='procedure'):
			counter+=1
			if token[counter] not in committed_lets and  token[counter] not in simbols:
				dist +=1
				entities.clear()
				depth += 1
				AddEntityFunction(token[counter],"procedure","",parametroi,offset)
				RecordScope(entities,depth)
				parametroi.clear()				
				put2=token[counter]
				counter+=1
				funcbody(put2)
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , waiting the name of the procedure!")
				exit(-1)

	def funcbody(nameID):
		global token
		global counter
		global mainflag
		global depth
		global dist
		token=result[0]
		line=result[1]	
		formalpars()
		if(token[counter]=='{'):
			counter+=1
			mainflag+=1
			if(mainflag!=0):#simainei oti teleiose tin douleia tou programma	
			 	block(nameID)
			if(token[counter]=='}'):
				dist -=1
				#scopes[depth]=""
				#scopes.remove("")
				#print(scopes)
				DeleteSame()
				#depth = depth - 1
				
				counter+=1
				mainflag-=1
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error expected  right bracket  ' } '")
				exit(-1)
		else:
			print('   On line {} :'.format(line[counter]))
			print("Error expected left bracket '{'")
			exit(-1)

	def formalpars():
		global token
		global counter
		token=result[0]
		line=result[1]	
		if(token[counter]=='('):
			counter+=1
			formalparlist()
			if(token[counter]==')'):
				counter+=1
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , expected  right parenthesis ')'")
				exit(-1)
		else:
			print('   On line {} :'.format(line[counter]))
			print("Error , expected left parenthesis '('")
			exit(-1)

	def formalparlist():
		global token
		global counter
		global metavlith
		global bytes
		bytes = 12
		metavlith=[]
		token=result[0]
		line=result[1]	
		formalparitem()
		while(token[counter]==','):
			counter+=1
			if(token[counter]=='in' or token[counter]=='inout'):
				formalparitem()
		return

	def formalparitem():
		global token
		global counter
		global depth
		global metavlith
		global bytes
		token=result[0]
		line=result[1]	
		metavlith=[]
		if(token[counter]=='in'):
			counter+=1
			if token[counter] not in committed_lets and  token[counter] not in simbols:
				AddEntityParameter(token[counter],"in",bytes)
				#scopes[depth][0].append([token[counter],"cv",depth])
				AddEntityMetavlith(token[counter],"cv",bytes)
				bytes+=4
				counter+=1
				return
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , perimeno onoma metablitis meta to in ")
				exit(-1)
		elif(token[counter]=='inout'):
			counter+=1
			if token[counter] not in committed_lets and  token[counter] not in simbols:
				AddEntityParameter(token[counter],"inout",bytes)
				#scopes[depth][0].append([token[counter],"cv",depth])
				AddEntityMetavlith(token[counter],"cv",bytes)
				bytes+=4
				counter+=1
				return
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , perimenoume onoma metavlitis meta to inout")
				exit(-1)
		
	def statements():
		global token
		global counter
		token=result[0]
		line=result[1]
		if token[counter] not in simbols :
			statement()
		elif(token[counter]=='{'):
			counter+=1
			if token[counter] not in simbols:
				statement()
				while(token[counter]==';'):
					counter+=1
					statement()
				if(token[counter]=='}'):
					counter+=1
				else:
					print('   On line {} :'.format(line[counter]))
					print("Error , perimenei deksia agkili gia na klisei kai na ksekinisei '}'")
					exit(-1)	
		return

	def statement():
		global token
		global counter
		token=result[0]
		line=result[1]	
		if token[counter] not in committed_lets and  token[counter] not in simbols:
			assignment_stat()
		elif(token[counter]=='if'):
			counter+=1
			if_stat()
		elif(token[counter]=='while'):
			counter+=1
			while_stat()
		elif(token[counter]=='doublewhile'):
			counter+=1	
			doublewhile_stat()
		elif(token[counter]=='loop'):
			counter+=1		
			loop_stat()
		elif(token[counter]=='exit'):
			exit_stat()
		elif(token[counter]=='forcase'):
			forcase_stat()
		elif(token[counter]=='incase'):
			incase_stat()
		elif(token[counter]=='call'):
			call_stat()
		elif(token[counter]=='return'):
			return_stat()
		elif(token[counter]=='input'):
			input_stat()
		elif(token[counter]=='print'):
			print_stat()
		
	def assignment_stat(): 
		global iffunction 
		global token
		global counter
		token=result[0]
		line=result[1]	
		if token[counter] not in committed_lets and  token[counter] not in simbols:
			idk=token[counter] 
			counter+=1
			if(token[counter]==':='):
				counter+=1
				Ep=expression()
				#p1
				genquad(':=',Ep,'_',idk)
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , leipei to simvolo anathesis gia mia metabliti ':=' ")
				exit(-1)
		return

	def if_stat():
		global token
		global counter
		global iftrue
		global iffalse
		iftrue=[]
		iffalse=[]
		token=result[0]
		line=result[1]	
		if(token[counter]=='('):
			counter+=1
			b=condition()
			if(token[counter]==')'):
				counter+=1
				if(token[counter]=='then'):
					counter+=1
					#p1
					backPatch(b[0],nextquad()) # b[0] kathos einai i proti thesi gia to true
					statements()
					#p2
					iflist=makeList(nextquad())
					genquad('jump','_','_','_')
					backPatch(b[1],nextquad())
					elsepart()
					#p3
					backPatch(iflist,nextquad())
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , den iparxei aristeri parenthesi ")
				exit(-1)
		else:
			print('   On line {} :'.format(line[counter]))
			print("Error , meta apo kathe if statement ksekina parethesi! edo leipei kai tin xreiazete ")
			exit(-1)
		iftrue=b[0]
		iffalse=b[1]
		return iftrue , iffalse

	def elsepart():
		global token
		global counter
		token=result[0]
		line=result[1]	
		if(token[counter]=='else'):
			counter+=1
			statement()
		return
	
	def while_stat():
		global token
		global counter
		global bquad		
		global wtrue
		global wfalse
		wfalse=[]
		wtrue=[]
		token=result[0]
		line=result[1]	
		if(token[counter]=='('):
			counter+=1
			#p1
			bquad=nextquad()
			b=condition()
			wtrue=b[0] # for true
			wfalse=b[1]#for false
			if(token[counter]==')'):
				counter+=1
				#p2
				backPatch(wtrue,nextquad())
				statements()
				#p3
				genquad('jump','_','_','_')
				backPatch(wfalse,nextquad())
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , den iparxei deksia parenthesi ")
				exit(-1)
		else:
			print('   On line {} :'.format(line[counter]))
			print("Error , meta apo kathe while statement ksekina parethesi! edo leipei kai tin xreiazete ")
			exit(-1)
		wtrue=b[0]
		wfalse=b[1]
		return wtrue,wfalse

	def doublewhile_stat():
		global token
		global counter
		token=result[0]
		line=result[1]	
		if(token[counter]=='('):
			counter+=1
			condition()
			if(token[counter]==')'):
				counter+=1
				statements()
				if(token[counter]=='else'):   
					counter+=1
					statements()
					return
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , leipei i deksia parenthesi")
				exit(-1)
		else:
			print('   On line {} :'.format(line[counter]))
			print("Error , leipei i aristeri parenthesi tou statement gia na mporesei na ksekinisei")
			exit(-1)
		return 
		
	def loop_stat():
		statements()
		return

	def exit_stat():
		global token
		global counter
		token=result[0]
		line=result[1]	
		if(token[counter]=='exit'):
			counter+=1
			return
		else:
			print('   On line {} :'.format(line[counter]))
			print("Error , den iparxei 'exit'")
			exit(-1)
			
	def forcase_stat():
		global token
		global counter
		token=result[0]
		line=result[1]	
		if(token[counter]=='forcase'):
			counter+=1
			while(token[counter]=='when'):
				counter+=1
				if(token[counter]=='('):
					counter+=1
					condition()
					if(token[counter]==')'):
						counter+=1	
						while(token[counter]==':'):
							counter+=1
							if(token[counter]=='when'):
								counter+=1
								if(token[counter]=='('):
									counter+=1
									condition()
									if(token[counter]==')'):
										counter+=1
									else:
										print('   On line {} :'.format(line[counter]))
										print("Error , den iparxei de3ia parenthesi ')'")
										exit(-1)
								else:
									print('   On line {} :'.format(line[counter]))
									print("Error , den iparxei aristerh parenthesi '( '")
									exit(-1)
							else:
								print('   On line {} :'.format(line[counter]))
								print("Error , den iparxei 'when'")
								exit(-1)
					else:
						print('   On line {} :'.format(line[counter]))
						print("Error , den iparxei de3ia parenthesi ')'")
						exit(-1)
				else:
					print('   On line {} :'.format(line[counter]))
					print("Error , den iparxei aristerh parenthesi '( '")
					exit(-1)
		else:			
			print('   On line {} :'.format(line[counter]))
			print("Error , den iparxei 'forcase '")
			exit(-1)
		if(token[counter]=='default'):
			counter+=1
			if(token[counter]==':'):
				counter+=1
				statements()
				return
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error, leipei i ano kai kato teleia ':'")
				exit(-1)
		else:
			print('   On line {} :'.format(line[counter]))
			print("Error , den iparxei default sto loop!")
			exit(-1)
		return 


	def incase_stat():
		global token
		global counter
		token=result[0]
		line=result[1]	
		if(token[counter]=='incase'):
			counter+=1
			while(token[counter]=='when'):
				counter+=1
				if(token[counter]=='('):
					counter+=1
					condition()
					if(token[counter]==')'):
						counter+=1	
						while(token[counter]==':'):
							counter+=1
							if(token[counter]=='when'):
								counter+=1
								if(token[counter]=='('):
									counter+=1
									condition()
									if(token[counter]==')'):
										counter+=1
									else:
										print('   On line {} :'.format(line[counter]))
										print("Error , den iparxei de3ia parenthesi ')'")
										exit(-1)
								else:
									print('   On line {} :'.format(line[counter]))
									print("Error , den iparxei aristerh parenthesi '( '")
									exit(-1)
							else:
								print('   On line {} :'.format(line[counter]))
								print("Error , den iparxei 'when'")
								exit(-1)
					else:
						print('   On line {} :'.format(line[counter]))
						print("Error , den iparxei de3ia parenthesi ')'")
						exit(-1)
				else:
					print('   On line {} :'.format(line[counter]))
					print("Error , den iparxei aristerh parenthesi '( '")
					exit(-1)
		else:			
			print('   On line {} :'.format(line[counter]))
			print("Error , den iparxei 'incase '")
			exit(-1)		
		if(token[counter]=='default'):
			counter+=1
			if(token[counter]==':'):
				counter+=1
				statements()
				return
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error, leipei i ano kai kato teleia ':'")
				exit(-1)
		else:
			print('   On line {} :'.format(line[counter]))
			print("Error , den iparxei default sto loop!")
			exit(-1)
		return
		
	def return_stat():
		#i ilopoish tou p1 ginete simfona me tis  diafaneies
		global token
		global counter
		global depth
		global bytes
		token=result[0]
		line=result[1]	
		if(token[counter]=='return'):
			counter+=1
			Ep=expression()
			#P1
			genquad('retv',Ep,'_','_')
			scopes[depth-1][0][len(scopes[depth-1][0])-1][4]=bytes
			
		else:
			print('   On line {} :'.format(line[counter]))
			print("Error , you mist an expression after return !")
			exit(-1)
		return
			
	def call_stat():
		global token
		global counter 
		global flag
		token=result[0]
		line=result[1]	
		if(token[counter]=='call'):
			counter+=1
			if token[counter] not in committed_lets and  token[counter] not in simbols:
				tok1=token[counter]
				counter+=1
				flag=11
				actualpars(tok1)	
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , den iparxei onoma metavlitis meta to call ")
				exit(-1)

	def print_stat():
		#ginete ilopoihsh simfona me diafaneies 
		#Eplace=Ep
		global token
		global counter
		token=result[0]
		line=result[1]	
		if(token[counter]=='print'):
			counter+=1
			if(token[counter]=='('):
				counter+=1
				Ep=expression()
				if(token[counter]==')'):
					counter+=1
					#p2
					genquad('out',Ep,'_','_')
				else:
					print('   On line {} :'.format(line[counter]))
					print("Error , leipei i deksia parenthesi ')'")
					exit(-1)
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , leipei i aristeri parenthesi '('")
				exit(-1)
			return
		return
	
	def input_stat():
		#i ilopoihsh ginete simfona me tis diafaneies 
		#idplace = idp
		global token
		global counter
		token=result[0]
		line=result[1]	
		if(token[counter]=='input'):
			counter+=1
			if(token[counter]=='('):
				counter+=1
				if token[counter] not in committed_lets and  token[counter] not in simbols:
					idp=token[counter]
					counter+=1
					if(token[counter]== ')'):
						counter+=1
						#p1
						genquad('inp',idp,'_','_')
					else:
						print('   On line {} :'.format(line[counter]))
						print("Error leipei i deksia parenthesi ')")
						exit(-1)
				else:
					print('   On line {} :'.format(line[counter]))
					print("Error , leipei to id  tou input pou kataxoreis ")
					exit(-1)
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , leipei i aristeri parenthesi '('")
				exit(-1)
		return
		
	def actualpars(name):
		global token
		global counter
		global flag
		token=result[0]
		line=result[1]	
		if(token[counter]=='('):
			counter+=1
			actualparlist()
			if(token[counter]==')'):
				counter+=1
				if(flag==10): # irtha apo tin idtail ara den eimai sinartisi
					w=newtemp()
					genquad('par',w,'RET','_')
					genquad('call',name,'_','_')
					flag=0
				elif(flag==11):
					genquad('call',name,'_','_')
					flag=0
			else:	
				print('   On line {} :'.format(line[counter]))
				print("Error ,leipei i deksia parenthesh gia na mporesei na oloklhrothei i ekfrash")
				exit(-1)
		return
	
	def actualparlist():
		global token
		global counter
		token=result[0]
		line=result[1]	
		actualparitem()
		while(token[counter]==','):
			counter+=1
			actualparitem()
		return
	
	def actualparitem():
		global token
		global counter
		token=result[0]
		line=result[1]	
		if(token[counter]=='in'):
			counter+=1
			expr=expression()
			genquad('par',expr,'CV','_')
		elif(token[counter]=='inout'):
			counter+=1
			if token[counter] not in committed_lets and  token[counter] not in simbols:
				tok=token[counter] # apothikeuse to string or name pou tha deis kai valto stin tetrada!
				counter+=1
				genquad('par',tok,'REF','_')	
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , den prosdioristike id ")
				exit(-1)
				
		return
###############################################
	def condition():
		global token
		global counter
		global btrue
		global bfalse
		btrue=[]
		bfalse=[]
		line=result[1]	
		q1=boolterm()
		#p1
		btrue=q1[0] # dose to q1.true 
		bfalse=q1[1]# dose to q1.false
		while(token[counter]=='or'):
			#p2
			backPatch(bfalse,nextquad())
			counter+=1
			#p3
			q2=boolterm()
			btrue=merge(btrue,q2[0])
			bfalse=q2[1]	
		return btrue,bfalse

	def boolterm():
		global token
		global counter
		global qtrue 
		global qfalse
		global r1
		qtrue=[]
		qfalse=[]
		token=result[0]
		line=result[1]
		#p1	
		r1=boolfactor()
		qtrue=r1[0] # true
		qfalse=r1[1]# false
		while(token[counter]=='and'):
			counter+=1
			#p2
			r2=boolfactor()
			backPatch(qtrue,nextquad())
			#p3
			qfalse=merge(qfalse,r2[0])
			qtrue=r2[1]
		return qtrue , qfalse
		
	def boolfactor():
		global token
		global counter	
		global rtrue
		global rfalse
		rtrue=[]
		rfalse=[]
		token=result[0]
		line=result[1]	
		if(token[counter]=='not'):
			counter+=1
			if(token[counter]=='['):
				counter+=1
				b=condition()
				if(token[counter]==']'):
					counter+=1
					#p1
					rtrue=b[0] # for true
					rfalse=b[1] # for false
				else:
					print('   On line {} :'.format(line[counter]))
					print("Error , leipei i deksia agkili ']' ")
					exit(-1)
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , leipei i aristeri agkikili '[' stin ekfrash sou ")
				exit(-1)
		elif(token[counter]=='['):
			counter+=1
			b=condition()
			if(token[counter]==']'):
				counter+=1
				#p1
				rtrue=b[0] # for true
				rfalse=b[1] #for false
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , leipei i deksia agkili stin sintaksi sou ']' ")
				exit(-1)
		else:
			e1=expression()
			relop=relational_oper()
			e2=expression()
			#p1 - apo logikes prakseis sel 33 
			#R->E1 relop E2{P1}
			#opote san E1.place = e1 , E2.place=e2 relop =relop
			#-------
			#p1
			rtrue=makeList(nextquad())
			genquad(relop,e1,e2,'_')
			rfalse=makeList(nextquad())
			genquad('jump','_','_','_')
		return  rtrue , rfalse
#####################################################		
	def expression():
		# i hlopoihsh paei simfona me tis diafaneies alla kai me tin grammatiki tis minimal++
		#t1place=t1 , t2place=t2  kai Eplace = Ep
		global token
		global counter
		global t1
		global t2
		global bytes
		global dist
		global metavlith
		metavlith=[]
		token=result[0]
		line=result[1]	
		optional_sign()
		t1=term()
		while(token[counter]=='+' or token[counter]=='-'):
			operation=add_oper()
			t2=term()
			#p1
			w=newtemp()
			genquad(operation,t1,t2,w)
			AddEntityMetavlith(w,"int",bytes)
			bytes += 4
			dist += 1
			t1=w
			scopes[depth][0]=scopes[depth][0]+metavlith
			break
		#p2
		Ep=t1
		return Ep
	
	def term():
		# i hlopoihsh paei simfona me tis diafaneies alla kai me tin grammatiki tis minimal++
		#f1place = f1  , f2place=f2 kai Tplace=Tp
		global token
		global counter
		global bytes
		global dist
		global metavlith
		global depth
		para=[]
		metavlith=[]
		token=result[0]
		line=result[1]	
		f1=factor()
		while(token[counter]=='*' or token[counter]=='/'):
			operation2=mul_oper()
			f2=factor()
			#p1
			w=newtemp()
			genquad(operation2,f1,f2,w)
			AddEntityMetavlith(w,"int",bytes)
			bytes += 4
			dist += 1
			
			f1=w
			scopes[depth][0]=scopes[depth][0]+metavlith
			
		#p2
		Tp=f1
		return Tp
	
	def factor():
		global token
		global counter
		token=result[0]
		line=result[1]
		if(token[counter]=='number_error'):
			print('   On line {} :'.format(line[counter]))
			print("Apagoreumenos ari8mos ")
			exit(1)
		elif token[counter]  in numbers:
			#eide constant opote apothikeuetai 
			check = token[counter]
			fp=token[counter]
			counter+=1
			return fp
		elif(token[counter]=='('):
			counter+=1
			Ep=expression()
			if(token[counter]==')'):
				fp=Ep
				counter+=1
				return fp
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , leipei h de3ia ')'")	
				exit(-1)
		elif token[counter] not in committed_lets and  token[counter] not in simbols:
			idp1=token[counter]
			fp=idp1
			counter+=1
			idtail(fp)
			return fp
		else:
			print('   On line {} :'.format(line[counter]))
			print(" Theloume constant h expression h variable ")
			exit(1)
		return fp

	def constant():
		global token
		global counter
		token=result[0]
		line=result[1]
		if(token[counter]=='{'):
			counter+=1
			factor()
			if(token[counter]=='}'):
				counter+=1
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , leipei to de3io '}'")
		elif(toket[counter]=='['):
			counter+=1
			factor()
			if(token[counter]==']'):
				counter+=1
			else:
				print('   On line {} :'.format(line[counter]))
				print("Error , leipei to de3io ']'")
		return
		
	def idtail(name):
		global token
		global counter
		global flag
		token=result[0]
		line=result[1]	
		if(flag==0): #simainei oti teleiose i call tin douleia tis 
			flag=10
			actualpars(name)
		return
	
	def relational_oper():
		global token
		global counter
		token=result[0]
		line=result[1]
		if(token[counter]=='='):
			counter+=1
		elif(token[counter]=='<='):
			counter+=1
		elif(token[counter]=='>='):
			counter+=1
		elif(token[counter]=='>'):
			counter+=1
		elif(token[counter]=='<'):
			counter+=1
		elif(token[counter]=='=='):
			counter+=1
		elif(token[counter]=='<>'):
			counter+=1
		else:
			print('   On line {} :'.format(line[counter]))
			print("Error , leipei mia apo tis epomenes perigrafes ' == , <= ,>= , <, >,<>")
			exit(-1)
		return token[counter-1]
	
	def add_oper():
		global x
		global token
		global counter
		x=0
		token=result[0]
		line=result[1]	
		if(token[counter]=='+'):
			x=token[counter]
			counter+=1
		elif(token[counter]=='-'):
			x=token[counter]
			counter+=1
		return x
	
	def mul_oper():
		global found 
		found=0
		global token
		global counter
		token=result[0]
		line=result[1]	
		if(token[counter]=='*'):
			found=token[counter]
			counter+=1
		elif(token[counter]=='/'):
			found=token[counter]
			counter+=1
		return found
	
	def optional_sign():
		global token
		global counter
		token=result[0]
		line=result[1]	
		add_oper()
		return
	
	program()
	return
	
	

Cfile=0
w=0
def makeCfile():
	global Cfile
	global w 
	if(Cfile==0):
		w=open(allItems[0][2]+".c","w+")
		Cfile=1
	programName=allItems[0][2]
	begBlock=0
	i=0
	while(len(allItems)!=i):
		if(allItems[i][1]=='begin_block' and begBlock==0):
			w.write('int main(){' + '\n')
			begBlock=1
		if(allItems[i][1]=='+' or allItems[i][1]=='-' or allItems[i][1]=='*' or allItems[i][1]=='/'):
			w.write('\t' + str(allItems[i][0]) + ': ' + str(allItems[i][4]) + "=" + str(allItems[i][3]) + str(allItems[i][1]) + str(allItems[i][2]) + ';' + '\n')
		if(allItems[i][1]=='<>' or allItems[i][1]=='==' or allItems[i][1]=='<=' or allItems[i][1]=='>=' or allItems[i][1]=='<' or allItems[i][1]=='>'):
			if(allItems[i][4]=='_'):		
				if(allItems[i][1]=='<>'):		
					w.write('\t' + str(allItems[i][0]) + ': if(' + str(allItems[i][2]) + '!=' + str(allItems[i][3]) + ') goto ' + str(allItems[i+1][4]) + ';' + '\n')
				else:		
					w.write('\t' + str(allItems[i][0]) + ': if(' + str(allItems[i][2]) + '' + str(allItems[i][1]) + '' + str(allItems[i][3]) + ') goto ' + str(allItems[i+1][4]) + ';' + '\n')
			else:
				if(allItems[i][1]=='<>'):		
					w.write('\t' + str(allItems[i][0]) + ': if(' + str(allItems[i][2]) + '!=' + str(allItems[i][3]) + ') goto ' + str(allItems[i][4]) + ';' + '\n')
				else:		
					w.write('\t' + str(allItems[i][0]) + ': if(' + str(allItems[i][2]) + '' + str(allItems[i][1]) + '' + str(allItems[i][3]) + ') goto ' + str(allItems[i][4]) + ';' + '\n')	
		if(allItems[i][1]=='jump'):
			if(allItems[i][4]!='_'):
				w.write('\t' + str(allItems[i][0]) + ": goto " + str(allItems[i][4]) + ';' + '\n')
		if(allItems[i][1]==':='):
			w.write('\t' + str(allItems[i][0]) + ': ' + str(allItems[i][4]) + '=' + str(allItems[i][2]) + ';' + '\n')
		if(allItems[i][1]=='out'):
			w.write('\t' + str(allItems[i][0]) + ': ' + 'printf(' + str(allItems[i][2]) + ');' + '\n')
		if(allItems[i][1]=='retv'):
			w.write('\t' + str(allItems[i][0]) + ': return(' + str(allItems[i][2]) + ');' + '\n')
		if(allItems[i][1]=='inp'):
			w.write('\t' + str(allItems[i][0]) + ': return(' + str(allItems[i][2]) + ');' + '\n')
		if(allItems[i][1]=='call'):
			w.write('\t' + str(allItems[i][0]) + ': ' + str(allItems[i][2]) + '(')
			i=i-1
			k=0
			while(allItems[i-k][1]=='par'):
				if(k!=0):
					w.write(',')
				k+=1
				if(allItems[i][3]=='CV'):
					w.write('int ' + str(allItems[i][2]))
				if(allItems[i][3]=='REF'):
					w.write('char ' + str(allItems[i][2]))
			w.write(');' + '\n')
			i=k+i
		if(allItems[i][1]=='halt'):
			w.write('\t' + str(allItems[i][0]) + ': return;' + '\n')
		if(allItems[i][1]=='end_block' and allItems[i][2]==programName):
			w.write('}' + '\n')
		i+=1

#Pinakas Symvolwn
def AddEntityMetavlith(name,typee,offset):
	metavlith.append([name,typee,offset])

def AddEntityFunction(name,typee,starQuad,argument,frameLength):
	metavlith.append([name,typee,starQuad,argument,frameLength])

#def AddEntitySta8era(name,value):


def AddEntityParameter(name,parMode,offset):
	metavlith.append([name,parMode,offset])
	parametroi.append([name,parMode,offset])

#def AddEntityProsParametros(name,offset):


def RecordScope(entity,depth):
	scopes.append([entity,depth])

#def RecordArgument(parMode,typee):

def DeleteSame():
	i=0
	j=0
	k=0
	while(len(scopes[0])+1!=i):
		j=0
		while(len(scopes[i][0])!=j):
			x=scopes[i][0][j]
			k=j+1
			while(len(scopes[i][0])!=k):
				if(x==scopes[i][0][k]):
					scopes[i][0][k]=""
					scopes[i][0].remove("")
				k+=1
			j+=1
		i+=1
	i=0



AsmFile=0
k=0
def makeAsmFile():
	global AsmFile
	global k 
	if(AsmFile==0):
		k=open(allItems[0][2]+".asm","w+")
		AsmFile=1
	programName=allItems[0][2]
	i=0
	a=0
	begBlock=0
	ba8os=0
	while(len(allItems)!=i):
		if(allItems[i][1]=='begin_block' and begBlock==1):
			k.write('\n')			
			k.write("L" + str(allItems[i][0]) + ":")
			l=0
			while(len(scopes[ba8os][0])!=l):
				if(len(scopes[ba8os][0][l])==5):
					k.write('   ' + '\t' + 'sw $ra,-0($sp)' + '\n')				
				l+=1
			ba8os+=1
			a+=1
		elif(allItems[i][1]=='begin_block' and begBlock==0):
			begBlock=1
			k.write("Lmain:" + '\n')
			k.write('\n')
			k.write("L" + str(allItems[i][0]) + ":" + '\t' + "addi $sp,$sp,"  + str(scopes[ba8os][1]) + '\n')
			k.write("   " + '\t' + "move $s0,$sp" + '\n')
		elif(allItems[i][1]=='end_block' and begBlock!=0):
			k.write('\n')			
			k.write("L" + str(allItems[i][0]) + ":")
			k.write('   ' + '\t' + 'lw $ra,-0($sp)' + '\n')
			k.write('   ' + '\t' + 'jr $ra' + '\n')					
			ba8os-=1
		elif(allItems[i][1]=='end_block'and begBlock==0):
			k.write('\n')			
			k.write("L" + str(allItems[i][0]) + ":" + '\n')
		elif(allItems[i][1]=="halt"):
			begBlock=0
			k.write('\n')			
			k.write("L" + str(allItems[i][0]) + ":" + '\n')
		elif(allItems[i][1]=='+' or allItems[i][1]=='-' or allItems[i][1]=='*' or allItems[i][1]=='/'):
			k.write('\n')			
			k.write("L" + str(allItems[i][0]) + ":")
			l=0
			prwth=0
			deuterh=0
			trith=0		
			while(len(scopes[ba8os][0])!=l):
				if(allItems[i][2]==scopes[ba8os][0][l][0]):
					prwth=scopes[ba8os][0][l][2]
				if(allItems[i][3]==scopes[ba8os][0][l][0]):
					deuterh=scopes[ba8os][0][l][2]
				if(allItems[i][4]==scopes[ba8os][0][l][0]):
					trith=scopes[ba8os][0][l][2]
				l+=1;
			if(prwth==0):
				k.write('   ' + '\t' + 'li $t1,' + str(allItems[i][2]) + '\n')
			else:
				k.write('   ' + '\t' + 'lw $t1,-' + str(prwth) + '($sp)' + '\n')
			if(deuterh==0):
				k.write('   ' + '\t' + 'li $t2,' + str(allItems[i][3]) + '\n')
			else:
				k.write('   ' + '\t' +'lw $t2,-' + str(deuterh) + '($sp)' + '\n')
			if(allItems[i][1]=='+'):
				k.write('   ' + '\t' + 'add $t1,$t1,$t2' + '\n')
			if(allItems[i][1]=='-'):
				k.write('   ' + '\t' + 'sub $t1,$t1,$t2' + '\n')
			if(allItems[i][1]=='*'):
				k.write('   ' + '\t' + 'mul $t1,$t1,$t2' + '\n')
			if(allItems[i][1]=='/'):
				k.write('   ' + '\t' + 'div $t1,$t1,$t2' + '\n')
			if(trith==0):
				k.write('   ' + '\t' + 'li $t2,' + str(allItems[i][4]) + '\n')
			else:
				k.write('   ' + '\t' + 'lw $t1,-' + str(trith) + '($sp)' + '\n')
			prwth=0
			deuterh=0
			trith=0
		elif(allItems[i][1]=='<>' or allItems[i][1]=='==' or allItems[i][1]=='<=' or allItems[i][1]=='>=' or allItems[i][1]=='<' or allItems[i][1]=='>'):						
			k.write('\n')			
			k.write("L" + str(allItems[i][0]) + ":")
			prwth=0
			deuterh=0
			l=0		
			while(len(scopes[ba8os][0])!=l):
				if(allItems[i][2]==scopes[ba8os][0][l][0]):
					prwth=scopes[ba8os][0][l][2]
				if(allItems[i][3]==scopes[ba8os][0][l][0]):
					deuterh=scopes[ba8os][0][l][2]
				l+=1
			if(prwth==0):
				k.write('   ' + '\t' + 'li $t1,' + str(allItems[i][2]) + '\n')
			else:
				k.write('   ' + '\t' + 'lw $t1,-' + str(prwth) + '($sp)' + '\n')
			if(deuterh==0):
				k.write('   ' + '\t' + 'li $t2,' + str(allItems[i][3]) + '\n')
			else:
				k.write('   ' + '\t' +'lw $t2,-' + str(deuterh) + '($sp)' + '\n')
			if(allItems[i][1]=='<>'):
				k.write('   ' + '\t' + 'bne $t1,$t2,' + str(allItems[i][4]) + '\n')
			elif(allItems[i][1]=='=='):
				k.write('   ' + '\t' + 'beq $t1,$t2,' + str(allItems[i][4]) + '\n')
			elif(allItems[i][1]=='<='):
				k.write('   ' + '\t' + 'ble $t1,$t2,' + str(allItems[i][4]) + '\n')
			elif(allItems[i][1]=='>='):
				k.write('   ' + '\t' + 'bge $t1,$t2,' + str(allItems[i][4]) + '\n')
			elif(allItems[i][1]=='>'):
				k.write('   ' + '\t' + 'bgt $t1,$t2,' + str(allItems[i][4]) + '\n')
			elif(allItems[i][1]=='<'):	
				k.write('   ' + '\t' + 'blt $t1,$t2,' + str(allItems[i][4]) + '\n')	
		elif(allItems[i][1]==':='):
			k.write('\n')			
			k.write("L" + str(allItems[i][0]) + ":")
			prwth=0
			deuterh=0
			l=0
			while(len(scopes[ba8os][0])!=l):
				if(allItems[i][2]==scopes[ba8os][0][l][0]):
					prwth=scopes[ba8os][0][l][2]
				if(allItems[i][4]==scopes[ba8os][0][l][0]):
					deuterh=scopes[ba8os][0][l][2]	
				l+=1
			if(prwth==0):
				k.write('   ' + '\t' + 'li $t1,' + str(allItems[i][2]) + '\n')
			else:
				k.write('   ' + '\t' + 'lw $t1,-' + str(prwth) + '($sp)' + '\n')
			if(deuterh==0):
				k.write('   ' + '\t' + 'sw $t1,-' + str(allItems[i][4]) + '($sp)' + '\n')
			else:
				k.write('   ' + '\t' + 'sw $t1,-' + str(deuterh) + '($sp)' + '\n')
		elif(allItems[i][1]=="out"):
			k.write('\n')			
			k.write("L" + str(allItems[i][0]) + ":")
			prwth=0
			l=0
			while(len(scopes[ba8os][0])!=l):
				if(allItems[i][2]==scopes[ba8os][0][l][0]):
					prwth=scopes[ba8os][0][l][2]
				l+=1					
			if(prwth==0):
				k.write('   ' + '\t' + 'lw $t1,-' + str(allItems[i][4]) + '($sp)' + '\n')
			else:
				k.write('   ' + '\t' + 'lw $t1,-' + str(prwth) + '($sp)' + '\n')
			k.write('   ' + '\t' + 'li $v0,1' + '\n')
			k.write('   ' + '\t' + 'move $a0, $t1' + '\n')
			k.write('   ' + '\t' + 'syscall' + '\n')	
		elif(allItems[i][1]=="inp"):
			k.write('\n')			
			k.write("L" + str(allItems[i][0]) + ":")
			prwth=0
			l=0
			while(len(scopes[ba8os][0])!=l):
				if(allItems[i][2]==scopes[ba8os][0][l][0]):
					prwth=scopes[ba8os][0][l][2]
				l+=1					
			if(prwth==0):
				k.write('   ' + '\t' + 'lw $t1,-' + str(allItems[i][4]) + '($sp)' + '\n')
			else:
				k.write('   ' + '\t' + 'lw $t1,-' + str(prwth) + '($sp)' + '\n')
			k.write('   ' + '\t' + 'li $v0,5' + '\n')
			k.write('   ' + '\t' + 'syscall' + '\n')
		elif(allItems[i][1]=="retv"):
			k.write('\n')			
			k.write("L" + str(allItems[i][0]) + ":")
			prwth=0
			l=0
			if(allItems[i][2]=="_"):
				k.write('   ' + '\t' + 'move $v0,$t1' + '\n')
			else:
				while(len(scopes[ba8os][0])!=l):
					if(allItems[i][2]==scopes[ba8os][0][l][0]):
						prwth=scopes[ba8os][0][l][2]
					l+=1
				if(prwth==0):
					k.write('\t' + 'l1 $t0,-' + str(allItems[i][4]) + '\n')
				else:
					k.write('   ' + '\t' + 'lw $t0,-' + str(prwth) + '($sp)' + '\n')
				k.write('   ' + '\t' + 'lw $t1,($t0)' + '\n')
				k.write('   ' + '\t' + 'lw $t0,-8($sp)' + '\n')
				k.write('   ' + '\t' + 'sw $t1,($t0)' + '\n')
		elif(allItems[i][1]=="par"):
			k.write('\n')			
			k.write("L" + str(allItems[i][0]) + ":")
			prwth=0
			l=0
			while(len(scopes[ba8os][0])!=l):
				if(allItems[i][2]==scopes[ba8os][0][l][0]):
					prwth=scopes[ba8os][0][l][2]
				l+=1	
			if(allItems[i][3]=='CV'):
				k.write('   ' + '\t' + 'addi $fp, $sp, ' + str(prwth) + '\n')#ti einai to 24
				k.write('   ' + '\t' + 'lw $t1,-' + str(prwth) + '($sp)' + '\n')
				k.write('   ' + '\t' + 'sw $t1,-' + str(12+4*a) + '($fp)' + '\n')
			if(allItems[i][3]=='RET'):
				k.write('   ' + '\t' + 'add $t0,$sp,' + str(prwth) + '\n')
				k.write('   ' + '\t' + 'sw $t0,-8($fp)' + '\n')
			if(allItems[i][3]=='REF'):
				k.write('   ' + '\t' + 'addi $t0,$sp,' + str(prwth) + '\n')
				k.write('   ' + '\t' + 'sw $t0,-' + str(12+4*a) + '\n')
				a+=1
		elif(allItems[i][1]=="call"):
			k.write('\n')			
			k.write("L" + str(allItems[i][0]) + ":")
			prwth=0
			l=0	
			p=0		
			while(len(scopes)!=l):
					while(len(scopes[l][0])!=p):
						if(len(scopes[l][0][p])==5):
							if(allItems[i][2]==scopes[l][0][p][0]):
								prwth=scopes[l][0][p][4]
						p+=1
					l+=1
					p=0
							
			k.write('   ' + '\t' + 'sw $sp,-4($fp)' + '\n')
			k.write('   ' + '\t' + 'addi $sp, $sp, ' + str(prwth+4) + '\n')
			k.write('   ' + '\t' + 'jal L1' + '\n')
			k.write('   ' + '\t' + 'addi $sp, $sp, -' + str(prwth+4) + '\n')
		elif(allItems[i][1]=='jump'):
			k.write('\n')			
			k.write("L" + str(allItems[i][0]) + ":")
			k.write('   ' + '\t' +"b " + str(allItems[i][4]) + '\n')		
		i+=1
		

#shnarthsh gia na apotiponei tis 4-ades se arxeio .int !!
def intFile(x):
	for i in range(len(allItems)):
		inputX=allItems[i]
		x.write(str(inputX[0]))
		x.write(".(")
		x.write(str(inputX[1]))
		x.write(",")
		x.write(str(inputX[2]))
		x.write(",")
		x.write(str(inputX[3]))
		x.write(",")
		x.write(str(inputX[4]))
		x.write(")")
		x.write("\n")

def open_new_files():
	# einai gia to arxeio me kataliksi .int alla kai to c an ginei (xaxa)
	first=open(allItems[0][2]+'.int','w')
	intFile(first)
	first.close()

editorial_analyst()
open_new_files()
makeCfile()
makeAsmFile()

print(scopes)

