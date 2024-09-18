let myName: string = "Alice";


let myName1 = "Alice";

//
function greet(name: string) {
    console.log("Hello, " + name.toUpperCase() + "!!");
  }


  function getFavoriteNumber(): number {
    return 26;
  }

  async function getFavoriteNumber2(): Promise<number> {
    return 26;
  }

  const names = ["Alice", "Bob", "Eve"];
 
  // Contextual typing for function - parameter s inferred to have type string
  names.forEach(function (s) {
    console.log(s.toUpperCase());
  });
   
  // Contextual typing also applies to arrow functions
  names.forEach((s) => {
    console.log(s.toUpperCase());
  });


