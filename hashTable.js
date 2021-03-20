class HashTable {
    constructor(size){
      this.data = new Array(size);
      this.keyValue = []
    }

    // Without considering the hash memory address

    // set(key, value){
    //     // const keyValue = []
    //     let keyIndex = this.data.flat().indexOf(key)
        
    //     if ( keyIndex === -1) {
    //         this.keyValue.push(key)
    //         this.keyValue.push(value)
    //     } 
    //     else{
            
    //         this.keyValue.splice(keyIndex + 1, 1, value)
    //     }        
    //     return this.data.push(this.keyValue)
    // }

    // get(key){
    //     let flatArr = this.data.flat()
    //     let keyIndex = flatArr.indexOf(key)
    //     console.log(flatArr[keyIndex + 1])
    // }


    // Considering hash memory address

    set(key, value){
        let address = this._hash(key)
        
        if (!this.data[address]) {
            this.data[address] = []
            this.data[address].push([key, value])
        }else{
            let flatArr = this.data[address].flat()
            let keyIndex = flatArr.indexOf(key)
            flatArr.splice(keyIndex + 1, 1, value)
            this.data[address][0] = flatArr
        }
        
        return this.data
    }

    get(key){
        let address = this._hash(key)

        if (this.data[address]) {
            // console.log(this.data[address])
            let flatArr = this.data[address].flat()
            let keyIndex = flatArr.indexOf(key)
            return flatArr[keyIndex + 1]
        }

        return undefined
    }


  
    _hash(key) {
      let hash = 0;
      for (let i =0; i < key.length; i++){
          hash = (hash + key.charCodeAt(i) * i) % this.data.length
      }
      return hash;
    }
  }
  
  const myHashTable = new HashTable(50);
  myHashTable.set('grapes', 10000)


// console.log(myHashTable.get('grapes'))
  myHashTable.set('grapes', 100)

  myHashTable.set('grapes', 200)
//   myHashTable.get('grapes')
  myHashTable.set('apples', 9)
  console.log(myHashTable.get('grapes'))

// myHashTable.get('grapes')
 
  