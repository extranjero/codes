##GB tool

GB is a new generation tool for working with golang and its dependencies

#Advantages

1. all your dependencies is in your project you dont need to collect your dependencies with Godeps
2. You can build your project and its dependencies to bin auto generated folder

#Disadvantages

1. Goimports doesnt work in editors
2. You cannot use go get(you have gb vendor fetch instead but it cannot get dpenedencies from private repos)
3. You cant use go run normally

