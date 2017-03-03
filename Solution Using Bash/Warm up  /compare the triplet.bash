a=0
b=0

read -a A_arr
read -a B_arr

for i in $( seq 0 2 ); do

  eval a$i=${A_arr[$i]}
  eval b$i=${B_arr[$i]}

  if (( $(echo $((a$i))) > $(echo $((b$i))) )); then
    (( a+=1 ))
  elif (( $(echo $((a$i))) < $(echo $((b$i))) )); then
    (( b+=1 ))
  fi
done

echo $a $b
