#!/bin/sh
echo "Enter a string"
read string
echo "Enter a substring"
read substring
for i in $string
do
	if [ $i = $substring ]
	then
		echo "Found at position $n"
		n=`expr $n + 1`
	else
		n=`expr $n + 1`
	fi
done