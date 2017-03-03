#!/bin/sh
read N
read array
array=( `echo ${array[@]}` )

p=0
n=0
z=0

for (( i = 0; i < N; i++ )); do
b=${array[$i]}

if [ $b -lt 0 ]; then
p=$(($p+1))
elif [ $b -gt 0 ]; then
n=$(($n+1))
else
z=$(($z+1))
fi
done

echo "$n/$N" | bc -l
echo "$p/$N" | bc -l
echo "$z/$N" | bc -l
