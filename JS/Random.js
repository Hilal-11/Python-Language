
const hex = document.getElementById("hex");
const rgb = document.getElementById("rgb");
const hsl = document.getElementById("hsl");


const Hex = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8', '9' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F'];

function GenerateHexadecimalColorCode () {
    let randomHexColor = "#";
    for(let i = 1; i <= 6; i++) {
        let randomNumber = Math.floor(Math.random() * Hex.length);
        randomHexColor += Hex[randomNumber]
    }
    return randomHexColor;
}
const randomColor = GenerateHexadecimalColorCode();
hex.addEventListener("click" , () => {
    const randomColor = GenerateHexadecimalColorCode();
    console.log(randomColor)
    document.body.style.background = randomColor;
})

// Generate RGB
function RGB_Color_Code() {
    const red = Math.floor(Math.random() * 255);
    const green = Math.floor(Math.random() * 255);
    const blue = Math.floor(Math.random() * 255);
    const alpha = Math.random() * 1;
    const rgb_color = `rgb(${red},${green},${blue}, ${alpha.toFixed(2)})`;
    console.log(rgb_color)
    return rgb_color;
}

rgb.addEventListener("click" , () => {
    const rgb = RGB_Color_Code();
    document.body.style.background = rgb;
})

// HSL

function HSL() {
    const green = Math.floor(Math.random() * 100);
    const blue = Math.floor(Math.random() * 100);

    const HSL_color = `hsl(${0} , ${green}% ,${blue}%)`;

    return HSL_color;
}

hsl.addEventListener("click" , () => {
    const hsl_color = HSL();
    console.log(hsl_color);
    document.body.style.background = hsl_color;
})