const fs = require('fs');
const path = require('path');

const appDir = path.dirname(require.main.filename);
const dataPath = path.join(appDir, 'data.txt');
const data = fs.readFileSync(dataPath, { encoding: 'utf8', flag: 'r' }).split('\n');

const allEqual = (arr) => arr.every((v) => v === arr[0]);

const addAll = (arr) =>
  arr.reduce((acc, val) => {
    return acc + parseInt(val);
  }, 0);

const multiplyAll = (arr) =>
  arr.reduce((acc, val) => {
    return acc * parseInt(val);
  }, 1);

function partOne(data) {
  data.some((num1, index1) => {
    if (
      data.some((num2, index2) => {
        if ((index1 !== index2 && parseInt(num1) + parseInt(num2)) === 2020) {
          const res = parseInt(num1) * parseInt(num2);
          console.log(`${parseInt(num1)} + ${parseInt(num2)} === 2020`);
          console.log(`${parseInt(num1)} * ${parseInt(num2)} === ${res}`);
          return res;
        }
      })
    )
      return true;
  });
}

function partTwo(data) {
  data.some((num1, index1) => {
    if (
      data.some((num2, index2) => {
        if (
          data.some((num3, index3) => {
            if (!allEqual([index1, index2, index3]) && addAll([num1, num2, num3]) === 2020) {
              const res = multiplyAll([num1, num2, num3]);
              console.log(`${parseInt(num1)} + ${parseInt(num2)} + ${parseInt(num3)} === 2020`);
              console.log(`${parseInt(num1)} * ${parseInt(num2)} * ${parseInt(num3)} === ${res}`);
              return res;
            }
          })
        )
          return true;
      })
    )
      return true;
  });
}

partOne(data);
partTwo(data);
