read n k q
read -a Arr

if [ "$k" -gt "$n" ]
then

  let k=$k%$n
fi

for (( i=$q ; i>0; i-- )) do
   read newpos
   let oldpos=${#Arr[@]}-$k+$newpos
   if [ "$oldpos" -ge ${#Arr[@]} ]
   then
     let oldpos=$oldpos-${#Arr[@]}
   fi
   echo "${Arr[$oldpos]}"   
done
