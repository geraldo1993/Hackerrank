read  t # number of cases
for (( case=0; case<t; case++))
do
    read n k
    let late=0
    read times
    for student in ${times[@]}
    do
        if (( student > 0 ));
        then (( late++ ))
        fi
    done
    if (( late <= n - k));
    then echo "NO"
    else echo "YES"
    fi
done
