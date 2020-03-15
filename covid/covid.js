
const resultDivTop = document.getElementById("results-top");
const resultDivBottom = document.getElementById("results-bottom");

function showStatus(pathElement) {
    console.log(pathElement);
    var containerTitle = pathElement.attributes["title"].value;
    // console.log(locationTitle);

    var covid_data_for_location = covid_data[containerTitle] ? covid_data[containerTitle] : covid_data["default"];

    var toAppend = `
        <div class="location">
         
        </div>
        <div class="container">
        ${containerTitle} 
        </div>
        <div class="covid-data">
        <table>
            <tr>
                <th>NC</th>
                <th>FC</th>
                <th>Cured</th>
                <th>Death</th>
            </tr>
            <tr>
                <td>${covid_data_for_location["indian_national_confirmed_case"]}</td>
                <td>${covid_data_for_location["foreign_national_confirmed_case"]}</td>
                <td>${covid_data_for_location["cured_discharged"]}</td>
                <td>${covid_data_for_location["deaths"]}</td>

            </tr>
        </table>
        </div>
        `;
    resultDivTop.innerHTML = toAppend;
    resultDivBottom.innerHTML = toAppend;

}


let covid_data = {
    "Delhi": {
        "id": "IN-DL",
        "indian_national_confirmed_case": 7,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 2,
        "deaths": 1
    },
    "Haryana": {
        "id": "IN-HR",
        "indian_national_confirmed_case": 0,
        "foreign_national_confirmed_case": 14,
        "cured_discharged": 0,
        "deaths": 0
    },
    "Kerala": {
        "id": "IN-KL",
        "indian_national_confirmed_case": 22,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 3,
        "deaths": 0
    },
    "Rajasthan": {
        "id": "IN-RJ",
        "indian_national_confirmed_case": 2,
        "foreign_national_confirmed_case": 2,
        "cured_discharged": 0,
        "deaths": 0
    },
    "Telangana": {
        "id": "IN-TG",
        "indian_national_confirmed_case": 3,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 1,
        "deaths": 0
    },
    "Uttar Pradesh": {
        "id": "IN-UP",
        "indian_national_confirmed_case": 11,
        "foreign_national_confirmed_case": 1,
        "cured_discharged": 4,
        "deaths": 0
    },
    "Union Territory of Ladakh": {
        "id": "IN-LD",
        "indian_national_confirmed_case": 3,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 0
    },
    "Tamil Nadu": {
        "id": "IN-TN",
        "indian_national_confirmed_case": 1,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 0
    },
    "Union Territory of Jammu and Kashmir": {
        "id": "IN-JK",
        "indian_national_confirmed_case": 2,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 0
    },
    "Punjab": {
        "id": "IN-PB",
        "indian_national_confirmed_case": 1,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 0
    },
    "Karnataka": {
        "id": "IN-KA",
        "indian_national_confirmed_case": 6,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 1
    },
    "Maharashtra": {
        "id": "IN-MH",
        "indian_national_confirmed_case": 14,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 0
    },
    "Andhra Pradesh": {
        "id": "IN-AP",
        "indian_national_confirmed_case": 1,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 0
    }, 
    "default": {
        "id": "NA",
        "indian_national_confirmed_case": "NA",
        "foreign_national_confirmed_case": "NA",
        "cured_discharged": "NA",
        "deaths": "NA"
    }
}

let max_color_val = 20;
function colorThePaths() {
    let allStates = Object.keys(covid_data).filter(s => s !== "default");
    max_color_max = Math.max( allStates.map((e) => covid_data[e]["indian_national_confirmed_case"]) );
    allStates.forEach(state => {
        console.log(state);
        let el = document.getElementById(covid_data[state]["id"]);
        let color_ratio = covid_data[state]["indian_national_confirmed_case"]/max_color_val;
        let color_for_tr = `rgb(${20 + (Math.sin(color_ratio * Math.PI/2 ) * 235)}, 125,125)`;
        el.style.fill = color_for_tr;
    });
}
document.addEventListener('DOMContentLoaded', function(){ 
    // pushThePlayButton();
    setTimeout(colorThePaths, 600);  
}, false)
