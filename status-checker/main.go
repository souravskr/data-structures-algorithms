package main

import (
	"fmt"
	"net/http"
)

func checkStatus(link string, c chan string) {
	_, err := http.Get(link)
	if err != nil {
		fmt.Printf("%s 🌎 is down!\n", link)
		c <- "Down"
		return
	}
	fmt.Printf("%s 🌎 is up!\n", link)
	c <- "Up"
}
func main() {
	urls := []string{
		"https://google.com",
		"https://facebook.com",
		"https://golang.org",
		"https://amazon.com",
	}
	c := make(chan string)

	for _, url := range urls {
		go checkStatus(url, c)
	}
	for i := 0; i < len(urls); i++ {
		fmt.Println(<-c)
	}
}
