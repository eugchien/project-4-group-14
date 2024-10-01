$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        makePredictions();
    });
});


// call Flask API endpoint
function makePredictions() {
    var sex = $("#sex").val();
    var age = $("#age").val();
    var height = $("#height").val();
    var weight = $("#weight").val();
    var name_of_country = $("#NOC").val();
    var year = $("#year").val();
    var season = $("#season").val();
    var sport = $("#sport").val();


    // check if inputs are valid

    // create the payload
    var payload = {
        "sex": sex,
        "age": age,
        "height": height,
        "weight": weight,
        "name_of_country": name_of_country,
        "year": year,
        "season": season,
        "sport": sport
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);
            var prob = parseFloat(returnedData["prediction"]);

            if (prob > 0.5) {
                $("#output").text(`You Survived with probability ${prob}!`);
            } else {
                $("#output").text(`You did not survive with probability ${prob}, sorry. :(`);
            }

        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}