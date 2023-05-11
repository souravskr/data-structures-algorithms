package main

import (
	"fmt"
	"net/http"
	"time"
)

func checkStatus(link string, c chan string) {
	_, err := http.Get(link)
	if err != nil {
		fmt.Printf("%s 🌎 is down!\n", link)
		c <- link
		return
	}
	fmt.Printf("%s 🌎 is up!\n", link)
	c <- link
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
	for l := range c {
		go func(link string) {
			time.Sleep(time.Second)
			checkStatus(link, c)
		}(l)
	}
}
