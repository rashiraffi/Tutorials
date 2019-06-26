#!/bin/sh
echo "Enter two numbers"
read a
read b
echo "1.ADD 2.SUB 3.MUL 4.DIV"
echo "Enter any option"
read c
if [ $c = 1 ]
then
	d=$(( $a + $b ))
elif [ $c = 2 ]
then
	d=$(( $a - $b ))
elif [ $c = 3 ]
then
	d=$(( $a \* $b ))
elif [ $c = 4 ]
then
	d=$(( $a / $b ))
else
	echo "Invalid input"
fi
echo $d