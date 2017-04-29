read -a A_arr
read -a B_arr

a=0
b=0

for i in $( seq 0 4 ); do
  
  eval a$i=${A_arr[$i]}
  eval b$i=${B_arr[$i]}

  if (( $(echo $((a$i))) > $(echo $((b$i))) )); then
    (( a+=1 ))
  elif (( $(echo $((a$i))) < $(echo $((b$i))) )); then
    (( b+=1 ))
  fi
  
done

echo $a $b
