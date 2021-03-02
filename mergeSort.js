let arrayA = [0, 3,4,31]
let arrayB = [4, 6, 30, 5]

// arrayB.forEach(element => {
//     arrayA.push(element)
// });

let i = 1;
let j = 1;

let elemA = arrayA[0]
let elemB = arrayB[0]

const arrayC = [...arrayA];

let notSorted = true;

// while (notSorted) {

//     for (let index = 0; index < arrayA.length; index++) {
//         if (index <= 6) {
//             if (arrayA [index] > arrayA[index + 1]) {
//                 arrayC[index + 1] = arrayA[index] 
//                 arrayC[index] = arrayA[index+1]
//                 arrayA[index + 1] = arrayA[index]
//                 console.log(arrayC)
//             }    
//         }    
        
//     }
    

    
// }

const newArray = []

while (elemA || elemB) {

    console.log(elemA, elemB)
    
    if (!elemB || elemA < elemB) {
        newArray.push(elemA)
        elemA = arrayA[i]
        i++
    }else{
        newArray.push(elemB)
        elemB = arrayB[j]
        j++
    }
}






// console.log(arrayA)
console.log(newArray)