read n
IFS=' ' read -a arr
plus=0
minus=0
zero=0
for i in $(seq 0 $(echo "$n-1" | bc))
do
    s=${arr[$i]}
    if [[ $s == "0" ]]
    then
        zero=$((zero+1))
    elif [[ $s == "-"* ]]
    then
        minus=$((minus+1))
    else
        plus=$((plus+1))
    fi
done
printf "%.3f\n" $(bc -q -l <<<  "$plus/$n" )
printf "%.3f\n" $(bc -q -l <<<  "$minus/$n" )
printf "%.3f\n" $(bc -q -l <<<  "$zero/$n")
