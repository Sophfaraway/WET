let gotoKNP = document.querySelector("#goto-knp");
let gotoHadej = document.querySelector("#goto-hadej");
let contKNP = document.querySelector("#knp");
let contHadej = document.querySelector("#hadej");

let textHadej = document.querySelector("#text-hadej");
let tlacitkoHadej = document.querySelector("#tlacitko-hadej");
let vstupHadej = document.querySelector("#input-hadej");
let textKNP = document.querySelector("#text-knp");
let tlacitkoKamen = document.querySelector("#tlacitko-kamen");
let tlacitkoNuzky = document.querySelector("#tlacitko-nuzky");
let tlacitkoPapir = document.querySelector("#tlacitko-papir");

console.log(localStorage.getItem("page"));
checkPage();

gotoKNP.addEventListener("click", function() {
    localStorage.setItem("page", 2)
    checkPage();
});

gotoHadej.addEventListener("click", function() {
    localStorage.setItem("page", 1)
    checkPage();
});


function checkPage() {
    if (localStorage.getItem("page") === "1") {
        contKNP.style.display = "none";
        contHadej.style.display = "flex";
    } else {
        contHadej.style.display = "none";
        contKNP.style.display = "flex";
    }
}


tlacitkoHadej.addEventListener("click", hadejCislo);
vstupHadej.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        tlacitkoHadej.click();
    }
});
tlacitkoKamen.addEventListener("click", zvolenKamen);
tlacitkoNuzky.addEventListener("click", zvolenyNuzky);
tlacitkoPapir.addEventListener("click", zvolenPapir);



// ---------------------------------------------------------------------------
// ---------------------------------------------------------------------------
// ---------------------------------------------------------------------------







// ############
// Hádej číslo 
// ############



// zvolím tajné, hádané číslo                                       pro náhodné číslo od 0 do 10: Math.floor(Math.random() * 11);
//                ↓
let tajneCislo = Math.floor(Math.random() * 101);
//                ↑


function hadejCislo() {
    let vysledek = "";
    let odpoved = parseInt(vstupHadej.value);
    console.log(tajneCislo)

    // ---------------------------------------
    // Zde upravujeme logiku hry Hádej číslo ↓

    if (odpoved === tajneCislo) {
        vysledek = "Gratuliji, you won";
    } else if (odpoved < tajneCislo && odpoved + 11 > tajneCislo) {
        vysledek = "Close. Try a higher number";
    } else if (odpoved < tajneCislo) {
        vysledek = "Bad luck. Try a higher number";
    } else if (odpoved > tajneCislo && odpoved - 11 < tajneCislo) {
        vysledek = "Close. Try a lower number";
    } else if (odpoved > tajneCislo) {
        vysledek = "Bad luck. Try a lower number";
    } else {
        vysledek = "Please be so kind and put an actual number in";
    } 

    // Zde upravujeme logiku hry Hádej číslo ↑
    // ---------------------------------------

    textHadej.innerHTML = vysledek;
    vstupHadej.value = "";
}






// ####################
// Kámen, nůžky, papír 
// ####################

function pocitaceVoliKNP() {
    let volbaPocitace = Math.floor(Math.random() * 2) + 1;
    if (volbaPocitace === 1) {
        volbaPocitace = "kámen";
    } else if (volbaPocitace === 2) {
        volbaPocitace = "nůžky";
    } else {
        volbaPocitace = "papír";
    }
    return volbaPocitace;
}



function zvolenKamen() {
    let vysledek = "";
    let volbaPocitace = pocitaceVoliKNP(); // počítač zvolí náhodně buď kámen, nůžky nebo papír

    
    // ----------------------------------------------
    // Zde upravujeme logiku, pokud je zvolen kámen ↓

    if (volbaPocitace === "kámen") {
        vysledek = "Tie" ;
    } else if (volbaPocitace === "nůžky") {
        vysledek = "You won";
    }else if (volbaPocitace === "papír") {
        vysledek = "You lost";
    }
    
    // Zde upravujeme logiku, pokud je zvolen kámen ↑
    // ----------------------------------------------


    textKNP.innerHTML = "Zvolil jsi: kámen" + "<br>" + "<br>" +"Počítač zvolil: "  + volbaPocitace  + "<br>" + "<br>" + "<strong>" + vysledek.toUpperCase() + "</strong>" + "<br>" + "<br>" + "Chceš hrát znovu?";
}   



function zvolenyNuzky() {
    let vysledek = "";
    let volbaPocitace = pocitaceVoliKNP(); // počítač zvolí náhodně buď kámen, nůžky nebo papír

    
    // -------------------------------------------------
    // Zde upravujeme logiku, pokud jsou zvoleny nůžky ↓

    if (volbaPocitace === "kámen") {
        vysledek = "You lost" ;
    } else if (volbaPocitace === "nůžky") {
        vysledek = "Tie";
    }else if (volbaPocitace === "papír") {
        vysledek = "You won";
    }


    // Zde upravujeme logiku, pokud jsou zvoleny nůžky ↑
    // -------------------------------------------------


    textKNP.innerHTML = "Zvolil jsi: nůžky" + "<br>" + "<br>" +"Počítač zvolil: "  + volbaPocitace  + "<br>" + "<br>" + "<strong>" + vysledek.toUpperCase() + "</strong>" + "<br>" + "<br>" + "Chceš hrát znovu?";
}   


function zvolenPapir() {
    let vysledek = "";
    let volbaPocitace = pocitaceVoliKNP(); // počítač zvolí náhodně buď kámen, nůžky nebo papír

    
    // ----------------------------------------------
    // Zde upravujeme logiku, pokud je zvolen papír ↓

    if (volbaPocitace === "kámen") {
        vysledek = "You won" ;
    } else if (volbaPocitace === "nůžky") {
        vysledek = "You lost";
    }else if (volbaPocitace === "papír") {
        vysledek = "Tie";
    }
    
    // Zde upravujeme logiku, pokud je zvolen papír ↑
    // ----------------------------------------------


    textKNP.innerHTML = "Zvolil jsi: papír" + "<br>" + "<br>" +"Počítač zvolil: "  + volbaPocitace  + "<br>" + "<br>" + "<strong>" + vysledek.toUpperCase() + "</strong>" + "<br>" + "<br>" + "Chceš hrát znovu?";
} 


















