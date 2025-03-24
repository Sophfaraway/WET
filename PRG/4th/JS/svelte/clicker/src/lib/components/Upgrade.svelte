<script>
    import { shared } from "$lib/shared.svelte";

    let shopClicked = $state(false)

    let { upgradeLevel } = $props()

    function upCount() {
        let upgrade = 1

        shopClicked = true

        if (upgradeLevel === 1) {
            upgrade = 2
        }else if (upgradeLevel === 2){
            upgrade = 5
        }else if (upgradeLevel === 3){
            upgrade = 10
        }
        shared.multiplier = upgrade
    }
    
        
</script>

<div>
    {#if shopClicked}
        <p>Shop upgraded</p>
    {:else}
        <p>Upgrade to level {upgradeLevel}</p>
    {/if}

    <button class="btn2" onclick={upCount}>Upgrade {upgradeLevel}</button>
</div>



<style>
    .btn2 {
        background-color: pink;
        border-radius: 5000px;
        border: 2px solid black;
        padding: 5px;
    }

    div{
        border: 2px solid black;
        padding: 0.5em 0.5em;
        margin: 5px;
        width: fit-content;
    }
</style>