let tlacitko = document.querySelector("#tlacitko")
let nadpis = document.getElementById("nadpis")

let input = document.querySelector("#input")


tlacitko.addEventListener("click", zmenNadpis)



function zmenNadpis() {
    let textInputu = input.value
    nadpis.style.fontSize = "150px"


    // if (textInputu === "otázka"){
    // nadpis.innerText = "42"
    // }else {
    // nadpis.innerText = textInputu
    // }

}


