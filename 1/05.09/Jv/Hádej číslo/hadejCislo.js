let tlacitko = document.querySelector("#tlacitko")
let nadpis = document.getElementById("nadpis")

let input = document.querySelector("#input")

let cislo = 7

tlacitko.addEventListener("click", zmenNadpis)

function zmenNadpis() {

    let cisloInputu = parseInt(input.value)
    console.log(cisloInputu)

    if (cisloInputu === cislo ) {
        nadpis.innerText = "Správně"
    }else if (cisloInputu < cislo) {
        nadpis.innerText = "Zkus vyšší číslo"
    }else if  (cisloInputu > cislo) {
        nadpis.innerText = "Zkus menší číslo"
    } else {
        nadpis.innerText = "Zadej číslo"
    }

}
