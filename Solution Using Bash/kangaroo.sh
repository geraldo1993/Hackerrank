read x1 v1 x2 v2
x=$(($x2-$x1))
v=$(($v1-$v2 ))
t2=$(($x%$v))
t=$(($x/$v))

if [ $x -gt $v ] && [ $t2 -eq 0 ] && [ $t -gt 0 ]
then
  echo "YES"
else
  echo "NO"
fi
