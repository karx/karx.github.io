
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
    "Andhra Pradesh": {
        "id": "IN-AP",
        "indian_national_confirmed_case": 19,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 1,
        "deaths": 1
    },
    "Andaman and Nicobar Islands": {
        "id": "IN-AN",
        "indian_national_confirmed_case": 9,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 0
    },
    "Chandigarh": {
        "id": "IN-CH",
        "indian_national_confirmed_case": 8,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 0
    },
    "Bihar": {
        "id": "IN-BR",
        "indian_national_confirmed_case": 11,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 1
    },
    "Delhi": {
        "id": "IN-DL",
        "indian_national_confirmed_case": 49,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 6,
        "deaths": 2
    },
    "Goa": {
        "id": "IN-DL",
        "indian_national_confirmed_case": 5,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 0
    },
    "Gujarat": {
        "id": "IN-GJ",
        "indian_national_confirmed_case": 58,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 1,
        "deaths": 5
    },
    "Haryana": {
        "id": "IN-HR",
        "indian_national_confirmed_case": 33,
        "foreign_national_confirmed_case": 14,
        "cured_discharged": 17,
        "deaths": 0
    },
    "Himachal Pradesh": {
        "id": "IN-HP",
        "indian_national_confirmed_case": 3,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 1
    },
    "Union Territory of Jammu and Kashmir": {
        "id": "IN-JK",
        "indian_national_confirmed_case": 31,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 1,
        "deaths": 2
    },
    "Karnataka": {
        "id": "IN-KA",
        "indian_national_confirmed_case": 76,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 5,
        "deaths": 3
    },
    "Kerala": {
        "id": "IN-KL",
        "indian_national_confirmed_case": 182,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 15,
        "deaths": 1
    },
    "Union Territory of Ladakh": {
        "id": "IN-LD",
        "indian_national_confirmed_case": 13,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 3,
        "deaths": 0
    },
    "Madhya Pradesh": {
        "id": "IN-MP",
        "indian_national_confirmed_case": 30,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 2
    },
    "Maharashtra": {
        "id": "IN-MH",
        "indian_national_confirmed_case": 186,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 25,
        "deaths": 6
    },
    "Manipur": {
        "id": "IN-MN",
        "indian_national_confirmed_case": 1,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 6
    },
    
    "Mizoram": {
        "id": "IN-MZ",
        "indian_national_confirmed_case": 1,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 6
    },
    
    "Odisha": {
        "id": "IN-OR",
        "indian_national_confirmed_case": 3,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 6
    },
    
    "Puducherry": {
        "id": "IN-PY",
        "indian_national_confirmed_case": 1,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 6
    },
    
    "Punjab": {
        "id": "IN-PB",
        "indian_national_confirmed_case": 38,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 1,
        "deaths": 1
    },
    
    "Rajasthan": {
        "id": "IN-RJ",
        "indian_national_confirmed_case": 55,
        "foreign_national_confirmed_case": 2,
        "cured_discharged": 3,
        "deaths": 0
    },

    "Tamil Nadu": {
        "id": "IN-TN",
        "indian_national_confirmed_case": 49,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 4,
        "deaths": 1
    },
    
    "Telangana": {
        "id": "IN-TG",
        "indian_national_confirmed_case": 66,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 1,
        "deaths": 1
    },

    "Uttarakhand": {
        "id": "IN-UT",
        "indian_national_confirmed_case": 7,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 2,
        "deaths": 0
    },
    
    "Uttar Pradesh": {
        "id": "IN-UP",
        "indian_national_confirmed_case": 65,
        "foreign_national_confirmed_case": 1,
        "cured_discharged": 11,
        "deaths": 0
    },
   
    "West Bengal": {
        "id": "IN-WB",
        "indian_national_confirmed_case": 18,
        "foreign_national_confirmed_case": 0,
        "cured_discharged": 0,
        "deaths": 1
    },
   
    
    "default": {
        "id": "NA",
        "indian_national_confirmed_case": "NA",
        "foreign_national_confirmed_case": "NA",
        "cured_discharged": "NA",
        "deaths": "NA"
    }
}

let max_color_val = 200;
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
