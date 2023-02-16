function sumSalaries(obj){
    let sum = 0;
    for (let x of Object.values(obj)){
        sum += x;
    }
    return sum;
}

let salaries = {
    "John": 100,
    "Pete": 300,
    "Mary": 250
  };
  
  alert( sumSalaries(salaries) ); // 650