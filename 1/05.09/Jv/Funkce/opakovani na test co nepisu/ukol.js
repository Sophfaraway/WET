function plusminus(n) {
    if (n < 0) {
        console.log("mínus")
    } else if (n > 0) {
        console.log("plus")
    } else if (n === 0) {
        console.log("nic")
    }
}

plusminus(20)

function plusJedna(x) {
    let y = x + 1
    console.log("plus jedna je ", y)
}

plusJedna(20)

function person_info(name, height, money) {
    console.log(name)

    if (height < 150) {
        console.log("je maly")
    } else if (height < 150) {
        console.log(" je velky")
    }

    if (money < 1000) {
        console.log("a chudy")
    } else if (money > 1000) {
        console.log("a bohaty")
    }
}

person_info("Bob", 120, 2000)
