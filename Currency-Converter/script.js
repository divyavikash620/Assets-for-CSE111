// API url
var url = "https://open.er-api.com/v6/latest/USD";
var data; // save data here

// fetching data when page loads
fetch(url)
    .then(function (response) {
        return response.json();
    })
    .then(function (json) {
        console.log(json); // checking if it works
        data = json.rates;

        var currencies = Object.keys(data);

        // loop to add options
        for (var i = 0; i < currencies.length; i++) {
            var currency = currencies[i];

            var option1 = document.createElement("option");
            option1.text = currency;
            option1.value = currency;

            var option2 = document.createElement("option");
            option2.text = currency;
            option2.value = currency;

            document.getElementById("fromCur").add(option1);
            document.getElementById("toCur").add(option2);
        }

        // set defaults
        document.getElementById("fromCur").value = "USD";
        document.getElementById("toCur").value = "EUR";
    })
    .catch(function (err) {
        alert("Something went wrong with the API!");
        console.log(err);
    });

function convertMoney() {
    var amount = document.getElementById("amount").value;
    var from = document.getElementById("fromCur").value;
    var to = document.getElementById("toCur").value;

    // check if empty
    if (amount === "") {
        alert("Please put a number");
        return;
    }

    // math logic
    var fromRate = data[from];
    var toRate = data[to];

    var conversion = (amount / fromRate) * toRate;

    // rounding to 2 decimals
    var final = Math.round(conversion * 100) / 100;

    document.getElementById("result").innerHTML = final + " " + to;
}