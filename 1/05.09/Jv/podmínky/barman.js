alert ("How old are you?")

let input = prompt(prompt=("give number"))
input = parseInt(input)

if (input >= 18) {
    console.log("you can have a beer")
} else {
    console.log ("you cannot have a beer")
}