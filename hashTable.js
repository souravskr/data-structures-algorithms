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
            // this.data[address].push([key, value])
        }
        
        this.data[address].push([key, value])
        

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

    keys(){
        let allKeyValues = []
        const onlyKeys = []

        // console.log(this.data)

        this.data.forEach(item => {
           allKeyValues.push(item.flat())
        });
        allKeyValues = allKeyValues.flat()
        for (let i = 0; i < allKeyValues.length; i++) {
            if (i % 2 === 0 ) {
                onlyKeys.push(allKeyValues[i])
            }
            
        }
        console.log((onlyKeys))

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
//   myHashTable.set('grapes', 100)

//   myHashTable.set('grapes', 200)
//   myHashTable.get('grapes')
  myHashTable.set('apples', 9)
  myHashTable.set('bananas', 19)
  myHashTable.set('oranges', 29)
  myHashTable.set('mangoes', 39)

//   console.log(myHashTable.get('mangoes'))

// myHashTable.get('grapes')
 
  myHashTable.keys()