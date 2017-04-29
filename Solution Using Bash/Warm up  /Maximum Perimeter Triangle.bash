read n
read array
array=$(echo "$array" | sed 's/ /\n/g' | sort -nr | paste -s -d " ")
array=($array)
while :
do
    sum=$((${array[$(($i+1))]} + ${array[$(($i+2))]}))
    if [ $sum -gt ${array[$i]} ]
    then
        echo "${array[$(($i+2))]} ${array[$(($i+1))]} ${array[$i]}"
        break
    else
        array=(${array[@]:1})
    fi
    if [ ${#array[@]} -lt 3 ]
    then
        echo "-1"
        break
    fi
done