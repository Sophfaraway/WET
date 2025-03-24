<script>
    import { shared } from "$lib/shared.svelte";
    function clicker(){
        setInterval(() => {shared.count++}, 1000)
    }
   
</script>

<button class="autoClickButton" onclick={clicker} >Auto Clicker</button>

<style>
    .autoClickButton {
        border: 2px solid black;
        padding: 1em 2em;
        border-radius: 5000px;
        color: black;
        background-color: pink;
    }
</style>
