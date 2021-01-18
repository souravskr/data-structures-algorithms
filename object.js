// Reference type is created by programmers, whereas premitive type is a feature of a programming languate

// Reference Type

let arr1 = [1];
let arr2 = arr1;
arr1.unshift(0);
console.log(arr2);

let object1 = { value: 1 };
let object2 = object1;

object1.value = 10;

console.log(object2);

// Premitive type --> Number, boolean, string, null, undefined

// Context Type --> Where we are within the object

const aFunction = {
  a: () => console.log(this),
};

aFunction.a();
// Here a is the context, it only works in aFunction context

// Instantiation

class Player {
  constructor(name, type) {
    this.name = name;
    this.type = type;
  }

  introduce() {
    console.log(`${this.name} & ${this.type}`);
  }
}

class Wizard extends Player {
  constructor(name, type) {
    super(name, type);
  }

  play() {
    console.log(`${this.type}`);
  }
}

const wizard1 = new Wizard("Sara", "Healer");
const player1 = new Player("John", "Magician");
wizard1.introduce();
player1.introduce();
wizard1.play();
