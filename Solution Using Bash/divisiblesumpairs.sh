read n k
read vals
result=0

for val in $vals; do
    ((result += mods[(k - val % k) % k]))
    ((mods[val % k] += 1))
done
echo "$result"
