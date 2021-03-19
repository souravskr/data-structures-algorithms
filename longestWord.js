const a = "flight"
const b = "flow"

let count = 0

let aStart = a[0]
let bStart = b[0]

let index = b.indexOf(aStart)

while (index != -1) {
    
    for (const char of a) {
        index = b.indexOf(char)
        if (index == -1) {
            break
        }
        count++
    }

}


const longestCommonPrefix = strs => {
    for (let i = 1; i < strs.length; i++) {
        
        // console.log(strs[0])
        console.log(strs[i])
        
    }
}







// console.log(a.slice(0, count))
longestCommonPrefix(["flower","flow","flight"])