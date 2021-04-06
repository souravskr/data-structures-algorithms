const printNumber = n => {
    if (n > 0){
        printNumber(n -1)
        console.log(n)
    }
}

console.log(printNumber(100))