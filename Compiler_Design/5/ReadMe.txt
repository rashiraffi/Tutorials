flex .\calculator.l
bison -dy .\calculator.y
gcc .\lex.yy.c .\y.tab.c
.\a.exe