const allPaths = document.getElementsByTagName("path");
const resultDiv = document.getElementById("results");

function showStatus(pathElement) {
    console.log(pathElement);
    var locationTitle = pathElement.attributes["title"].value;
    console.log(locationTitle);
    var containerTitle;
    var containerTitleContainer = pathElement.parentElement.attributes["title"];
    if (containerTitleContainer) {
        containerTitle = containerTitleContainer.value;
    } else {
        containerTitle = 'NA';
    }

    resultDiv.innerHTML = `
        <div class="location">
        <h3> ${locationTitle} </h3>
        </div>
        <div class="container">
        <h4> ${containerTitle} </h4>
        </div>
        `;
}


// function main() {
//     console.log(allPaths.length);
//     for(i=0; i< allPaths.length; i++) {
//         var element = allPaths[i];
//         console.log(element);
//         element.addEventListener("mouseover", (e) => showStatus);
//     }
// }

// main();
