.MODEL SMALL
.STACK
S MACRO P
        LEA DX,P
        MOV AH,09H
        INT 21H
        ENDM
R MACRO
	MOV BL,0AH
        MOV AH,01H
        INT 21H
        SUB AL,30H
	MUL BL
	MOV BL,AL
	MOV AH,01H
        INT 21H
        SUB AL,30H
	ADD BL,AL
        ENDM
P MACRO
        MOV CL,0AH
        MOV AH,00H
        DIV CL
        MOV BL,AH
        ADD AL,30H
        MOV DL,AL
        MOV AH,02H
        INT 21H
        MOV AL,BL
        ADD AL,30H
        MOV DL,AL
        MOV AH,02H
        INT 21H
        ENDM
CLR MACRO 
	MOV SI,00H
	MOV DL,00H
	MOV AL,00H
	ENDM
.DATA
        a DB 10,13, 'ENTER THE NUMBER OF NUMBERS: $'
        res DB 10,13, 'LARGEST NUMBER IS : $'
	b DB 10,13, 'ENTER THE NUMBER : $'
	ress DB 10,13, 'SMALLEST NUMBER IS : $'
	l DB 10 dup ('$')
	ct DB 0
	lg DB 0
	sm DB 0
.CODE
	.STARTUP
        S a
	R
	MOV CL,BL
	MOV SI,00H
	MOV DL,00H
NEXT:	CMP CL,DL
	JE NEXT1
	MOV ct,DL
	S b
	MOV DL,ct
	R
	MOV l[SI],BL
	INC SI
	INC DL
	JMP NEXT
NEXT1:	CLR
	MOV AL,l[SI]
	MOV lg,AL
L1:	CMP CL,DL
	JE NEXT2
	MOV AL,l[SI]
	MOV BL,lg
	CMP AL,BL
	JL SP1
	MOV lg,AL
SP1:	INC SI
	INC DL
	JMP L1
NEXT2:	CLR
	MOV AL,l[SI]
	MOV sm,AL
S1:	CMP CL,DL
	JE EX
	MOV AL,sm
	MOV BL,l[SI]
	CMP AL,BL
	JL SP2
	MOV sm,BL
SP2:	INC SI
	INC DL
	JMP S1
EX:	S res
	MOV AL,lg
	P
	S ress
	MOV AL,sm
	P
	.EXIT
END
