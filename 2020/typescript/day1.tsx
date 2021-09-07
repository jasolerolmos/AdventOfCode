import * as fs from 'fs';
import text from './day1.module'

fs.readFileSync('foo.txt','utf8');

console.log(text)

const Day1 = () => {
    return "Hola"
}

console.log("Test TSX")
console.log(Day1())