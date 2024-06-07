let speed = 10;
let x = 0;
let r = 255;
let g = 255;
let b = 255;

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(150, 0, 200);
  fill(r, g, b);
  noStroke();
  if (x > width || x < 0) {
    speed *= -1;
    r = random(0, 255);
    g = random(0, 255);
    b = random(0, 255);
  }
  x += speed;
  ellipse(x, height / 2, 50);
}
