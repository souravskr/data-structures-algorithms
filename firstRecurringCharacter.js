//Google Question
//Given an array = [2,5,1,2,3,5,1,2,4]:
//It should return 2

//Given an array = [2,1,1,2,3,5,1,2,4]:
//It should return 1

//Given an array = [2,3,4,5]:
//It should return undefined


const inputArr = [2,1,1,2,3,5,1,2,4]
let j = -1

for (let i = 0; i < inputArr.length -1; i++) {
    if (inputArr[i] === inputArr[i+1]) {
        j = i
        break;
    }
}

// console.log(j)

if (j === -1) {
    console.log(undefined)
}else console.log(inputArr[j])