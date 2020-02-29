# File: age.sh
# Name: D.Saravanan    Date: 24/02/2020
# Bash script to display number of persons in a given age group

while read line
do
	echo "$line"
done < list.csv

min=`cat list.csv | tail -n +2 | cut -d "," -f 3 | sort -n | head -1`
max=`cat list.csv | tail -n +2 | cut -d "," -f 3 | sort -n | tail -1`

echo "Enter lower limit age: "
read ll

if [ $ll -lt $min ]
then
	echo "The minimum age value in the list is $min."
	echo "Enter lower limit age: "
	read ll
fi

echo "Enter upper limit age: "
read ul

if [ $ul -gt $max ]
then
	echo "The maximum age value in the list is $max."
	echo "Enter upper limit age: "
	read ul
fi

count=0

#No_of_entries=`cat list.csv | tail -n +2 | wc -l`
#echo $No_of_entries

#sorted_age_list=`cat list.csv | tail -n +2 | cut -d "," -f 3 | sort -n`
#echo $sorted_age_list

for n in `cat list.csv | tail -n +2 | cut -d "," -f 3`
do
	if [ $n -ge $ll ] && [ $n -lt $ul ];
	then
		((count++))
	fi
done

echo "The number of persons between the age $ll and $ul is $count."
