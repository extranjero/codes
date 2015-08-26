for i in 1 2 3 4 5
do
	echo "welcome $i times"
done

for (( i = 5; i != 0; i-- ))
do 
	echo "welcome $i times"
done


while [ $i -le 10 ]
do
  echo "$n * $i = `expr $i \* $n`"
  i=`expr $i + 1`
done
