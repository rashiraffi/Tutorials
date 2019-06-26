#!/bin/sh
echo "Enter a string"
read string
echo "Enter a number"
read x
n=0
for i in $string
do
	if [ $n = $x ]
	then
		echo $i
		n=$(( $n + 1 ))
	else
		n=$(( $n + 1 ))
	fi
done
