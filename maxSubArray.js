const inArr = [-1]

// const add = (a, b) => a + b

// const maxItem = Math.max(...inArr)

// Brute Force Method ==> Complexity is O(n^2) ==> Not accepted in Leetcode

const maxSubArray = (inArr)=>{

    const add = (a, b) => a + b
    let maxSum = 0;
    let tempSum = 0


    for (let i = 0; i < inArr.length; i++) {

        if ( i == 0 || inArr[i] > maxSum) {
            maxSum = inArr[i]
        }

        for (let j = 1; j < inArr.length; j++) {

            if (i > j) {
                j = i + 1
            }


            let tempArr = inArr.slice(i, j + 1)
            

            tempSum = tempArr.reduce(add)

            if (maxSum > tempSum){
                continue
            }else{
                maxSum = tempSum
            }


        }
        
    }

    return maxSum

}



console.log(maxSubArray(inArr))