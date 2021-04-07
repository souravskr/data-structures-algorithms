const inArr = [1, -3, 2, 1, -1]

// const add = (a, b) => a + b

// const maxItem = Math.max(...inArr)

// Brute Force Method ==> Complexity is O(n^2) ==> Not accepted in Leetcode

const maxSubArray1 = (inArr)=>{

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

// Khadane's Algorithm 

const maxSubArray = (arr)=> {
    let c_sum = arr[0]
    let g_sum = arr[0]

    for (let i = 1; i < arr.length; i++) {
        c_sum = Math.max(arr[i], c_sum + arr[i])

        if (c_sum > g_sum) {
            g_sum = c_sum
        }
    }

    return g_sum
}





console.log(maxSubArray(inArr))