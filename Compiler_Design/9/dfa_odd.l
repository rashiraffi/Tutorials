%{
%} 

%s A B C

%% 
<INITIAL>0 BEGIN B; 
<INITIAL>1 BEGIN A;
<A>0 BEGIN C;
<A>1 BEGIN INITIAL;
<B>0 BEGIN INITIAL;
<B>1 BEGIN C;
<C>0 BEGIN A;
<C>1 BEGIN B;
<INITIAL>\n BEGIN INITIAL; {printf("Not Accepted\n");}{return 0;}
<A>\n BEGIN A; {printf("Not Accepted\n");}{return 0;}
<B>\n BEGIN B; {printf("Not Accepted\n");}{return 0;}
<C>\n BEGIN C; {printf("Accepted\n");}{return 0;}
%%

void main() 
{ 
    yylex();
} 

int yywrap(){
    return 1;
}