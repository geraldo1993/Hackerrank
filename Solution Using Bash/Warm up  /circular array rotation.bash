read n k q
read -a array
[ $k -gt $n ] && k=$(($k % $n))
posan=$(($n - $k))
while read -r question || [ -n "$question" ]; do
  pos=$(($posan + $question))
  [ $pos -ge $n ] && pos=$(($pos - $n))
  echo ${array[$pos]}
done