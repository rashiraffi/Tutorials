#!/bin/sh
if [ $# -eq 2 ]
then
	if ! [ -f $1 ]
	then
		echo "File not exist"
	else
		c=$(grep -c "$2" "$1")
		if ! [ $c ]
		then
			echo "File already exist"
		else
			echo $1 >> $2 
		fi
	fi

else
	echo "Invalid entry"
	echo "try again"
fi