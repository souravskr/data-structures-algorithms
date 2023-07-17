package main

import "fmt"

type bot interface {
	getGreetings() string
}

type englishBot struct {
}
type spanishBot struct {
}

func (englishBot) getGreetings() string {
	return "Hello 👋🏼"
}

func (spanishBot) getGreetings() string {
	return "Hola 👋🏼"
}

func printGreetings(b bot) {
	fmt.Println(b.getGreetings())
}

func main() {
	eb := englishBot{}
	sb := spanishBot{}
	printGreetings(eb)
	printGreetings(sb)
}
