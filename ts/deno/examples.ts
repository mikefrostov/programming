let name1: string;
name1 = 'luigi'

console.log(name1);


const decoder = new TextDecoder('utf-8');
const data1 = await Deno.readFile('readme.txt');
console.log(decoder.decode(data1));

const encoder = new TextEncoder();
const text = encoder.encode('somestring2');

await Deno.writeFile('readme.txt', text);

const response = await fetch('https://swapi.dev/api/films');
const data2 = await response.json();

console.log(data2);