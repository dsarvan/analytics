#!/usr/bin/env bash
# File: sampling.sh
# Name: D.Saravanan    Date: 26/02/2020
# Bash script to analyse adult.csv data

fname="adult.csv"
min=`cat $fname|grep ^[0-9]|cut -d "," -f 1|sort -n|head -n 1`
max=`cat $fname|grep ^[0-9]|cut -d "," -f 1|sort -n|tail -n 1`

echo "Minimum age : $min"
echo "Maximum age : $max"

echo "Enter class interval : "
read interval

echo "-------------------------------------------------------------------"
printf "%10s\t%10s\t%10s\t%4s\t%10s\t%5s\t%10s\n" "Class" "Freq" "CFreq" "Mean" "Freq*Mean" "Mean^2" "Freq*Mean^2"
echo "-------------------------------------------------------------------"

funct ($m, $nval)
{
	sum=0; count=0
	for val in `seq $m 1 $nval`
	do
		sum=`echo "$sum+$val"|bc -l`
		count='echo "$count+1"|bc -l`
	done
	return `echo "scale=4;$sum/$count"|bc -l`
}

cfreq=0
for m in `seq $min $interval $max`
do
	incr=`echo "$m+$interval"|bc -l`
	if [ $incr -le $max ]
	then
#		sum=0; nval=`echo "$incr-1"|bc` 
#		for val in `seq $m 1 $nval`
#		do
#			sum=`echo "$sum+$val"|bc -l`
#		done
#		mean=`echo "scale=4;$sum/$interval"|bc -l` 
		mean=funct ($m, $nval)

		freq=0
		for n in `cat $fname|grep ^[0-9]|cut -d "," -f 1`
		do
			if [ $n -ge $m ] && [ $n -lt $incr ]
			then
				freq=`echo "$freq+1"|bc -l`
				cfreq=`echo "$cfreq+1"|bc -l`
			fi
		done

		means=`echo "scale=4;$mean^2"|bc -l` 
		freqm=`echo "scale=4;$freq*$mean"|bc -l`
		freqs=`echo "scale=4;$freq*$means"|bc -l`

		echo "[$m $incr) | $freq | $cfreq | $mean | $freqm | $means | $freqs"
	fi

	if [ $incr -ge $max ]
	then
#		sum=0; count=0
#		for val in `seq $m 1 $max`
#		do
#			sum=`echo "$sum+$val"|bc -l`
#			count=`echo "$count+1"|bc -l`
#		done
#		mean=`echo "scale=4;$sum/$count"|bc -l`
		mean=fucnt ($m, $max)

		freq=0
		for n in `cat $fname|grep ^[0-9]|cut -d "," -f 1`
		do
			if [ $n -ge $m ] && [ $n -le $max ]
			then
				freq=`echo "$freq+1"|bc -l`
				cfreq=`echo "$cfreq+1"|bc -l`
			fi
		done

		means=`echo "scale=4;$mean^2"|bc -l` 
		freqm=`echo "scale=4;$freq*$mean"|bc -l`
		freqs=`echo "scale=4;$freq*$means"|bc -l`

		echo "[$m $max] | $freq | $cfreq | $mean | $freqm | $means | $freqs"
	fi
done
