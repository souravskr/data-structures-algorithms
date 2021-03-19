class HashTable {
    constructor(size){
      this.data = new Array(size);
    }

    set(key, value){
        const keyValue = []
        keyValue.push(key)
        keyValue.push(value)
        this.data.push(keyValue)
    }

    get(key){
        
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
  myHashTable.set('apples', 9)
  myHashTable.get('apples')
  