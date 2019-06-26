#!/bin/sh
i=0
while [ $i -le 100 ]
do
	n=$(( i % 2 ))
	if [ $n = 1 ]
	then
		echo $i
		i=$(( i + 1 ))
	else
		i=$(( i + 1 ))
	fi
done