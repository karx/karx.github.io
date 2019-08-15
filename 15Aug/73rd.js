
const resultDivTop = document.getElementById("results-top");
const resultDivBottom = document.getElementById("results-bottom");

function showStatus(pathElement) {
    console.log(pathElement);
    var locationTitle = pathElement.attributes["title"].value;
    // console.log(locationTitle);
    var containerTitle;
    var containerTitleContainer = pathElement.parentElement.attributes["title"];
    if (containerTitleContainer) {
        containerTitle = containerTitleContainer.value;
    } else {
        containerTitle = 'NA';
    }

    var toAppend = `
        <div class="location">
         ${locationTitle} 
        </div>
        <div class="container">
        ${containerTitle} 
        </div>
        `;
    resultDivTop.innerHTML = toAppend;
    resultDivBottom.innerHTML = toAppend;

}