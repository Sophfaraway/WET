<script>
    import { shared} from "$lib/shared.svelte";

    let rndInt = 0
    let rndX = 0
    let rdnY = 0

    function addClick(){
        getRandomInt()
        getRandomPosition()
        shared.count = shared.count + rndInt
    }

    function getRandomInt() {
        rndInt = Math.floor(Math.random() * 50) + 1
    }

    function getRandomPosition() {
        rndX = Math.floor(Math.random() * vh) + 1
        rndY = Math.floor(Math.random() * vw) + 1
    }

</script>

<button class="emojiButton" onclick={addClick} style="x:{rndX}, y:{rndY}">🥺</button>

<style>
    .emojiButton {
        x: 0;
        y: 0;
        font-size: 50px;
        top:var(x);
        left:var(y);
    }
</style>