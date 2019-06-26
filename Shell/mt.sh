#!/bin/sh
echo "enter the number"
read n
i=0
while [ $i -le 10 ]
do
	s=$(( $i \* $n ))
	echo "$i * $n = $s"
	i=`expr $i + 1`
done