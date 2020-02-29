# File: combination.sh
# Name: D.Saravanan    Date: 24/02/2020
# Bash script to find C(n,r)

echo "Enter value n: "
read n

echo "Enter value r: "
read r

if [ $n -lt $r ]
then
	echo "Error: The value of n should be greater than or equal to r."
	echo "Enter value n: "
	read n
fi

diff=`echo "$n-$r"|bc`

x=1

nvalue=1
while [ $n -ge $x ]
do
	nvalue=`echo "$nvalue*$n"|bc`
	((n--))
done

rvalue=1
while [ $r -ge $x ]
do
	rvalue=`echo "$rvalue*$r"|bc`
	((r--))
done

diffvalue=1
while [ $diff -ge $x ]
do
	diffvalue=`echo "$diffvalue*$diff"|bc`
	((diff--))
done

nCr=`echo "$nvalue/($rvalue*$diffvalue)"|bc`
echo "The number of combinations are $nCr."
