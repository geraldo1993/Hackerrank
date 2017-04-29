read n
sum1=0
sum2=0
for ((row=1; row <= $n; row++))
    do
    read colw
    col=1
    for x in $colw
        do                                 

        if [ $row -eq $col ]
        then
            sum1=$(($sum1 + $x))
        fi
        if [ $row -eq $(($n + 1 - $col)) ]
        then
            sum2=$(($sum2 + $x))
        fi
        col=$(($col+1))
    done
done

dif=$(($sum1 - $sum2))
if [ $dif -lt 0 ]; then dif=$((-1 * $dif)); fi
echo $dif





