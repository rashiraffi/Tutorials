#!/bin/sh
if [ $# = 1 ]
then
	cd
	cd Documents/Jyothi_17-21
	if [ -d $1 ]
	then
		echo "Students of "$1" department"
		cd $1
		ls -1
	else
		echo "Invalid Input"
		echo "Use UPPERCASE for department"
	fi
else
	echo "Invalid input "
	echo "try again"
fi
