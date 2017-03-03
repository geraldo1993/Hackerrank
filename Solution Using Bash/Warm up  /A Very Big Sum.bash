function sum {
    s=0
    for i in `seq 1 $#`; do
        s=$(($s + ${!i}))
    done
    echo $s
}

read n
read a
sum $a
