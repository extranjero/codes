if cat $1; then
	echo -e "\n\nFile $1 found"
else 
	echo "File not found"
fi

#test or expr for logical checks
if test 5 -eq 6; then # 5 == 6
	echo "equal"
fi

if [5 -ne 6]; then 
	echo "not equal"
fi


#multilevel if else

if [ $1 -gt 0 ]; then
  echo "$1 is positive"
elif [ $1 -lt 0 ]
then
  echo "$1 is negative"
elif [ $1 -eq 0 ]
then
  echo "$1 is zero"
else
  echo "Opps! $1 is not number, give number"
fi

# -s file  // file not empty
# -f file  // file exist, normal, not directory
# -d dir   // directory exist and not file
# -w file  // is writable file
# -r file  // is readeble file
# -x file  // is executable file

## Logical

# ! expression             //Logical NOT
# expression -a expression // Logical AND
# expression -o expression //Logical OR


