<script>
	import Timer from "$lib/components/Timer.svelte"
	import Upgrade from "$lib/components/Upgrade.svelte"
    import { shared } from "$lib/shared.svelte";
    import Autoclicker from "$lib/components/Autoclicker.svelte";
    import Emoji from "$lib/components/Emoji.svelte";

    let animPop = $state()
    let animShrink = $state()

    let colors = [
        "Cornsilk", "DeepSkyBlue", "Plum", "PaleVioletRed",  "MistyRose"
    ]
    let selectedColor = $state(colors[3])

    function increment(){
        shared.count = shared.count + shared.multiplier
        animShrink = "anim-shrink"

        setTimeout(() => {
            animShrink = ""
        }, 100)
    }

    $effect(() => {
        if (shared.count > 0){
            animPop = "anim-pop"
        }
        setTimeout(() => {
            animPop = ""
        }, 100)
    })
</script>

<Timer />
<Autoclicker/>
<Emoji/>
<Upgrade upgradeLevel={1}/>
<Upgrade upgradeLevel={2}/>
<Upgrade upgradeLevel={3}/>

{#each colors as color}
<button class="circle" onclick={() => selectedColor = color} aria-label={color} style ="--color:{color}"></button>
{/each}

<div class="wrapper">
    <p class={animPop}>{shared.count}</p>
    <button class="btn {animShrink}" onclick={increment} style="--color:{selectedColor}">Click me!</button>
</div>

<style>
    .btn {
        --color:"lime";
        border: 2px solid black;
        padding: 1em 2em;
        border-radius: 5000px;
        background-color: var(--color);
        color: black;
    }

    .wrapper{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        min-height: 100vh;
        gap: 1em;
    }

    .anim-pop {
        animation: popout 0.1s;
    }
    .anim-shrink {
        animation: shrink 0.1s;
    }

    .circle {
        --color:"lime";
        aspect-ratio: 1/1;
        height: 50px;
        border-radius: 50%;
        background-color: var(--color);
    }

    @keyframes popout {
        50% {
            scale: 2;
        }

        100% {
            scale: 1;
        }
    }
    @keyframes shrink {
        100% {
            scale: 1;
        }

        50% {
            scale: 0.9;
        }
    }
</style>
