let fortune = document.getElementById("fortune")
let image = document.getElementById("image")

let button = document.querySelector("#button")
button.addEventListener("click", addFortune)

function addFortune() {
    let cislo = Math.floor(Math.random() * 6)

    if (cislo === 1) {
        fortune.innerText =
            "Your future will be like unicorns and rainbows. Bright and colorful"
    } else if (cislo === 2) {
        fortune.innerText = "Your future isn't looking so good."
    } else if (cislo === 3) {
        fortune.innerText = "You will find the love of your life very soon."
    } else if (cislo === 4) {
        fortune.innerText = "Good things are coming your way."
    } else if (cislo === 5) {
        fortune.innerText = "You will be pretty unlucky in the next few days."
    }
}
