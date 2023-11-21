const wrapper = document.querySelector(".wrapper");

for (let i = 0; i < 6; i++) {
  let novyDiv = document.createElement("div");

  novyDiv.classList.add("square");

  wrapper.appendChild(novyDiv);

  let r = Math.floor(Math.random() * 255);
  let g = Math.floor(Math.random() * 255);
  let b = Math.floor(Math.random() * 255);

  novyDiv.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
}
