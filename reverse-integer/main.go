package main

import "fmt"

func reverseNumber(num int) bool {
	if num < 0 {
		return false
	}
	tmp := num
	r := 0
	var l int
	for num > 0 {
		fmt.Println(num)
		l = num % 10
		num = num / 10
		r = r*10 + l
	}
	if tmp == r {
		return true
	}
	return false
}

func main() {
	fmt.Println("Hello, reverse")
	fmt.Println(reverseNumber(121))
	//fmt.Println(reverseNumber(123))
}
