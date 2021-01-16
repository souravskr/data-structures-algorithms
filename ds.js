const findCommon = (arr1, arr2) => {
  let arrToObject = {};

  for (let i = 0; i < arr1.length; i++) {
    if (!arrToObject[i]) {
      let item = arr1[i];
      arrToObject[item] = true;
    }
  }

  for (let j = 0; j < arr2.length; j++) {
    if (arrToObject[arr2[j]]) {
      return true;
    }
  }
  return false;
};

const array1 = ["a", "b", "c", "x"];
const array2 = ["z", "c", "l"];

// createObject(array1, array2);

console.log(findCommon(array1, array2));

// Another way--> with Builtin function

const findCommon1 = (arr1, arr2) => {
  return arr1.some((item) => arr2.includes(item));
};

console.log(findCommon1(array1, array2));
