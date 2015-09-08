package main 

import (
	m "github.com/keighl/mandrill"

	"log"
	"fmt"
)

func main(){
	client := m.ClientWithKey("TOKEN")

	message := &m.Message{}
	message.AddRecipient("ahidoyatov@gmail.com", "Abdullo Xidoyatov", "to")
	message.FromEmail = "ahidoyatov@gmail.com"
	message.FromName = "Shoptolidan"
	message.Subject = "Test"
	message.HTML = "<h1>You won!!</h1>"

	responses, err := client.MessagesSend(message)

	if err != nil {
		log.Fatal("Message send error: ", err)
	}

	fmt.Println("Responces ", responses)
}


