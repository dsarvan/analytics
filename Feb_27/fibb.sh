# File: fibb.sh
# Name: D.Saravanan    Date: 27/02/2020
# Bash script to generate Fibbonaci series

m=0; echo $m
n=1; echo $n

while [ $n -le 100 ]
do
	nxt=`echo "$m+$n"|bc -l`; echo $nxt
	m=$n; n=$nxt
done
