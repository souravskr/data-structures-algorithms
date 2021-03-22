//Google Question
//Given an array = [2,5,1,2,3,5,1,2,4]:
//It should return 2

//Given an array = [2,1,1,2,3,5,1,2,4]:
//It should return 1

//Given an array = [2,5,5,2,3,5,1,2,4]
//It should return 5

//Given an array = [2,3,4,5]:
//It should return undefined


// With traditional array method
const firstRecurringChar1 = inputArr => {
  
    for (let i = 0; i < inputArr.length -1; i++) {
        if (inputArr[i] === inputArr[i+1]) {
            return inputArr[i];
        }
    }
    return undefined
}

const inputArr = [2, 5, 1 , 2, 3, 5, 1, 2, 4]
console.log(firstRecurringChar1(inputArr))

// With hash function

const firstRecurringChar = arr => {
    const map = {}
    for (let i = 0; i < arr.length; i++) {
        
        if (map[arr[i]] != undefined) {
            return arr[i]
        } else {
            map[arr[i]] = i
        }
    }

    return undefined
}

// console.log(firstRecurringChar(inputArr))