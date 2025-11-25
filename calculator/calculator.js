

const buttons = document.querySelectorAll(".buttons button");
const display = document.getElementById("display");
const clearBtn = document.getElementById("clear");
const equalBtn = document.getElementById("equals");


let currentExpression = "";





buttons.forEach(button => {
    button.addEventListener("click", () => {
        const value = button.dataset.value;   


    if (!value) return;


    currentExpression += value;


    display.textContent = currentExpression;
});
 });


clearBtn.addEventListener("click", () => {
    currentExpression = "";
    display.textContent = "0";
});



equalBtn.addEventListener("click", () => {
    try {

        const result = eval(currentExpression);


        display.textContent = result;
        currentExpression = result.toString();
    } catch (error) {

        display.textContent = "Error";
        currentExpression = "";
    };
});