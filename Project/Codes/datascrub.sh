#!/usr/bin/env bash

for n in {2..14..2}
do
    cut -d '"' -f $n data2019.csv > file$n.txt
done

paste -d ',' file{2..14..2}.txt > result.csv
