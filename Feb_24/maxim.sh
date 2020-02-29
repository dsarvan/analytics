# File: maxim.sh
# Name: D.Saravanan    Date: 24/02/2020
# Bash script to display maximum of two numbers for the user input

echo "Enter first number: "
read x
echo "Enter second number: "
read y

echo " "

if [ $x -ge $y ]
then
	echo "$x is maximum"
else
	echo "$y is maximum"
fi
