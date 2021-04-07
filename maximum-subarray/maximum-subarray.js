/**
 * @param {number[]} nums
 * @return {number}
 */
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