const greatestNumber = arr => {
    const new_arr = []
    arr.forEach(i => {
        new_arr[i] = i
    });

    return new_arr[new_arr.length - 1]
}

arr = [200, 3, 8, 5, 100]

console.log(greatestNumber(arr))