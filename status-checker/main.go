package main

import (
	"fmt"
	"net/http"
)

func checkStatus(links []string) {
	for _, link := range links {
		_, err := http.Get(link)
		if err != nil {
			fmt.Printf("%s 🌎 is down!\n", link)
		} else {
			fmt.Printf("%s 🌎 is up!\n", link)
		}
	}
}
func main() {
	urls := []string{
		"https://google.com",
		"https://facebook.com",
		"https://golang.org",
		"https://sequencebio.com",
	}
	checkStatus(urls)
}
