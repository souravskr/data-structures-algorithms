package main

import "fmt"

type Node struct {
	data int
	next *Node
}

type LinkedList struct {
	head   *Node
	length int
}

func (l *LinkedList) prepend(n *Node) {
	second := l.head
	l.head = n
	l.head.next = second
	l.length += 1
}

func (l *LinkedList) printList() {
	current := l.head
	for l.length != 0 {
		fmt.Print(current.data)
		current = current.next
		l.length -= 1
	}
	fmt.Println()
}

func main() {
	newList := LinkedList{}
	node1 := &Node{data: 8}
	node2 := &Node{data: 10}
	node3 := &Node{data: 18}
	newList.prepend(node3)
	newList.prepend(node2)
	newList.prepend(node1)
	newList.printList()

}
