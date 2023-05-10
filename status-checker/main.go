package main

import (
	"fmt"
	"net/http"
)

func checkStatus(link string) {
	_, err := http.Get(link)
	if err != nil {
		fmt.Printf("%s 🌎 is down!\n", link)
		return
	}
	fmt.Printf("%s 🌎 is up!\n", link)
}
func main() {
	urls := []string{
		"https://google.com",
		"https://facebook.com",
		"https://golang.org",
		"https://sequencebio.com",
	}
	for _, url := range urls {
		checkStatus(url)
	}
}
