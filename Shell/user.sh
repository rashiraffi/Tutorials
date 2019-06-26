#!/bin/sh
if [ $# = 2 ]
then
	if ! [ -f $1 ]
	then
		echo "File not exist..."
	else
		c=$(grep -w "$2" "$1")
		if [ $c ]
		then
			echo "User already exist..."
		else
			echo $2 >> $1
		fi
	fi
else
	echo "Invalid input"
	echo "user....."
fi