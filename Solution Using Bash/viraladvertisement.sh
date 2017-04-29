read n
pl=0 #people who liked
newl=0 #new likers

for ((i=0; i <= $n; i++)) 
do
	if [ $i -eq 1 ]; then
		newl=$((5/2))
	else
		newl=$((newl*3/2))
	fi
	pl=$(($pl + $newl))
done

echo $pl
