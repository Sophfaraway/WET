function converter(c) {
    let f = c * 1.8 + 32
    console.log(f)
}

converter(50)

function converter2(f2) {
    let c2 = (f2 - 32) / 1.8
    console.log(c2)
}

converter2(122)

let tlacitko = document.querySelector("#tlacitko")
let nadpis = document.getElementById("nadpis")
let input = document.getElementById("input")
let input2 = document.getElementById("input2")

tlacitko.addEventListener("click", convertInput)

function convertInput() {
    let cislo = parseInt(input2.value)
    let inputCF = input.value

    if (inputCF === "F") {
        let f3 = cislo * 1.8 + 32
        nadpis.innerText = f3
    } else if (inputCF === "C") {
        let c3 = (cislo - 32) / 1.8
        nadpis.innerText = c3
    } else {
        nadpis.innerText = "Please choose between F or C"
    }
}
