# File: problem2.sh
# Name: D.Saravanan    Date: 27/02/2020
#

m=0; n=1
sum=0

while [ $n -le 4000000 ]
do
	s=`echo "$m+$n"|bc -l` 
	if(($s%2 == 0))
	then
		sum=`echo "$sum+$s"|bc -l`
	fi
	m=$n; n=$s
done

echo $sum
