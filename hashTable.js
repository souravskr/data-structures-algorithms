class HashTable {
    constructor(size){
      this.data = new Array(size);
      this.keyValue = []
    }

    set(key, value){
        // const keyValue = []
        let keyIndex = this.data.flat().indexOf(key)
        
        if ( keyIndex === -1) {
            this.keyValue.push(key)
            this.keyValue.push(value)
        } 
        else{
            
            this.keyValue.splice(keyIndex + 1, 1, value)
        }

        // console.log(this.keyValue)
        // console.log(keyIndex)
        
        return this.data.push(this.keyValue)
    }

    get(key){
        let flatArr = this.data.flat()
        let keyIndex = flatArr.indexOf(key)
        console.log(flatArr[keyIndex + 1])
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
  myHashTable.get('grapes')
  myHashTable.set('grapes', 100)
  myHashTable.get('grapes')
  myHashTable.set('apples', 9)
  myHashTable.get('apples')
  