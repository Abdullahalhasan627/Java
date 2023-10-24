// console.log(100..toString());
// console.log((100).toString());

// var x = 10.2222222;
// var y = 10.2222222;
// var z = x + y;
// console.log(x, y, z);
// var b = x.toString();
// console.log(b);
// console.log(z.toFixed(2))
// var i = z.toFixed(2);
// console.log(i);   
// console.log(+i + 10);
// console.log(Number(z.toFixed(2)));


// console.log(100..toString());
// console.log((100).toString());
// console.log(100.555555.toFixed(2));
// console.log(parseInt("100 Aboud"));
// console.log(parseFloat("100.4444 Aboud"));

// -------------------------------------

// console.log(Math.round(99.6));   // 100
// console.log(Math.round(99.5));   // 100
// console.log(Math.round(99.4));   // 99

// console.log(Math.ceil(99.1));  // 100
// console.log(Math.floor(99.9));  //99

// console.log(Math.min(10, 20, 5, 100, 95, 70));
// console.log(Math.max(10, 20, 5, 100, 95, 70));

// console.log(Math.pow(2, 4));  //2 ** 4 = 16

// var NumberRandom = Math.floor(Math.random() * 100) + 1;
// console.log(NumberRandom);

// console.log(Math.trunc(100.77772))

// ----------------------------------------


// let Me = "Ahmed"
// let Name = "Omer";
// let Nname = "   ABOUD    ";
// console.log(Name[4]);  // O
// console.log(Name.charAt(0));  // 0
// console.log(Nname.trim());

// console.log(Name.toUpperCase());
// console.log(Nname.toLowerCase());

// console.log(Me.trim().charAt(2).toUpperCase());

// console.log("Ah" + Me.charAt(2).toUpperCase() + "ed")

// let text = "Abdullah web programming";

// console.log(text.indexOf("web"));
// console.log(text.lastIndexOf("a"));
console.log(text.slice(8)); 
console.log(text.slice(2, 8));
console.log(text.slice(-5, -1))

let name = "Abdullah and alhasan ";
let num1 = "100 Abdullah";
let num2 = "100.11 Alhasan";
let number = 1000;
let number2 = 100.33333333;

// console.log(Math.round(99));  //  99.4=> 99 and 99.5=> 100
// console.log(Math.floor(99.9));   //  99.9 => 99
// console.log(Math.ceil(99.1));   //  99.1 => 100
// console.log(Math.max(99, 100, 102, 66, 75, 19));   //  max => 102
// console.log(Math.min(99, 100, 102, 66, 75, 19));  // min => 19
// console.log(Math.abs(-2));  // -2 => 2
// console.log(name.charAt(2).toUpperCase()); //
// console.log(name.charAt(0).toLowerCase()); //
// console.log(number.toString()); //
// console.log(number2.toFixed(2)); //

// console.log(name.indexOf("a"));  // 6
// console.log(name.lastIndexOf("a"));  // 18
// console.log(name.repeat(4));
// console.log(name.split(" "));


// console.log(name.length);
// console.log(name.substring(0, 6));   // and alhasan
// console.log(name.substr(0, 6))
// console.log(name.includes("and")); // True
// console.log(name.includes("10"));   // False
// console.log(name.startsWith("A", 0)); //
// console.log(name.startsWith("Abd", 0))   //  True
// console.log(name.endsWith("h", 8));   //  True
// console.log(name.endsWith("ah", 8));  // True

// console.log(10 == "10"); // True
// console.log("10" == "10");
// console.log(10 === "10");  // |Type and Value| => type: false, value: true; => False
// console.log("10" === "10");  // |Type and value| => type: true, value: false => True
// console.log(typeof "Addullha" === typeof "abdullha");  //  |Type and Value| => type: true, value: true => True
// console.log("Abdullah" === "Abdullah");

// console.log(true);
// console.log(!true);
// console.log(!(10 == 10));
// console.log(10 > 9 || 10 > 11);  // True
// console.log(10 > 9 && 10 >= 10 && 10 < 100);  // True

let x = 10;
let y = 0;
let z = 10;

// if (x == y || x == z) {
//     console.log(true);
// }

// else if (x > y && z > y) {
//     console.log(true);
// }

// else {
//     console.log(false);
// }

// let nam = "abdullha";
// if (x == 10) {
//     if (nam[0].toUpperCase()) {
//         console.log("Hello", nam);
//     } else {
//         console.log("The first letter");
//     }
// }

let num3 = 10;
let num4 = "10";

// num3 === num4 ? console.log("Hello", name1, "and", name2) : console.log("The not found");


// let result = num3 === num4 ? "Hello": "The first letter";

// console.log(num3 === num4 ? "Hello" : "The not found");

// console.log("Hello", `${result}`);

// console.log("Hello", `${num3 === num4 ? "Hello" : "The not found"}`);


// let result1 = num3 > num4 ? console.log("The num3 > num4") : num3 < num4 ? console.log("The num3 < num4") : console.log("The num3 == num4");


// switch (num3) {
//     case 18:
//         console.log("Hello");
//         break;
//     case 13:
//         console.log("your are smail");
//         break;
//     case 43:
//         console.log("You are old");
//         break;
//     default:
//         console.log("Enter your old");
// };

var array = ["Abdullha", "Omer", "Ahmad"];

// console.log("Char: " + array[0][0]);

let array_array = ["A", "B", "C", ["M", "N", "X", ["Y", "Z", ["H"]]]];

// console.log("Char:", array_array[3][3][2][0]);
// console.log(array_array);

// array_array[3][0] = "U";
// console.log(array_array);

// console.log(Array.isArray(array_array));  // True
// console.logD(Array.isArray(num1));  // False

// array[3] = "Ali";

// console.log(array.length)

// console.log(array)

// console.log(array[3]);


// array.length = 2;

// array[array.length - 1] = "Osama";

// console.log(array);



// // اضافه عنصر لل array في الاول
// array.unshift("abuod", "ali")
// console.log(array);

// // اضافه عنصر لل array في الاخر
// array.push("Osama")
// console.log(array);

// // حذا عنصر من ال array في الاول
// array.shift()
// console.log(array);

// // حذا عنصر من ال array في الاخر
// array.pop()
// console.log(array);


console.log(array.indexOf("Ahmad"));



