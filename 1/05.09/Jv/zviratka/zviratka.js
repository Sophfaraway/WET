let tlacitko = document.querySelector("#tlacitko")
let nadpis = document.getElementById("nadpis")
let nadpis2 = document.getElementById("nadpis2")
let input = document.querySelector("#input")

tlacitko.addEventListener("click", zmenNadpis)

function zmenNadpis() {

    let textInputu = input.value

    if (textInputu === "turtle" ) {
        nadpis2.innerText = "I like turtles"
        document.body.style.background = "cyan"
    }else if (textInputu === "flamingo") {
        nadpis2.innerText = "🦩"
        document.body.style.background = "pink"
    }else if  (textInputu === "fox") {
        nadpis2.innerText = "What does the fox say?"
        document.body.style.background = "orange"
    } else {
        nadpis2.innerText = "I don't know that animal :("
        document.body.style.background = "black"
        nadpis.style.color = "white"
        nadpis2.style.color = "white"
    }

}
