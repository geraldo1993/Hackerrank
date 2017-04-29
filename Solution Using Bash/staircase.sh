read n
for i in $(seq 1 $n); do
  for j in $(seq 1 $(($n - $i))); do
    echo -n ' '
  done
  for j in $(seq 1 $i); do
    echo -n '#'
  done
  echo
done
     
