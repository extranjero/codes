echo "Choose number 1 to 5"
read choice

case $choice in
	"1") echo "You choose 1";;
	"2") echo "You choose 2";;
	"3") echo "You choose 3";;
	"4") echo "You choose 4";;
	"5") echo "You choose 5";;
   	*) echo "Sorry, I can not gat a $choice for you";;
esac

#run shell script on debug mode

bash -x myshell.bash
sh -v myshell.sh
