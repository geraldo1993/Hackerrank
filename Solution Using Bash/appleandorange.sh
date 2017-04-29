read s t
read a b
read m n
read apples
declare -i count=0
for val in $apples; do
    ((a + val >= s && a + val <= t)) && count+=1
done
echo $count
count=0
read oranges
for val in $oranges; do
    ((b + val >= s && b + val <= t)) && count+=1
done
echo $count

