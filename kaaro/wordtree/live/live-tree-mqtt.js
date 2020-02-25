google.charts.load("current", { packages: ["wordtree"] });
google.charts.setOnLoadCallback(initChart);

var globalChartHandle;
var options = {
  wordtree: {
    format: "implicit",
    word: "started",
    type: "double"
  }
};
var g_phrases_array = ["Let's get started shall we"];

function initChart() {
  var data = google.visualization.arrayToDataTable([
    ["Phrases"],
    ["We are now live, time to get started"]
  ]);

  var chart = new google.visualization.WordTree(
    document.getElementById("wordtree_basic")
  );
  globalChartHandle = chart;
  chart.draw(data, options);
}

async function updateChartWithStrings(phrase_array) {
  console.log(`changing data of the graph`);
  let chart = globalChartHandle;
  let data_array = [["Phrases"]];
  g_phrases_array = [...g_phrases_array, ...phrase_array];

  g_phrases_array.forEach(str => {
    data_array.push([str]);
  });

  console.log(data_array);
  var data = google.visualization.arrayToDataTable(data_array);
  chart.draw(data, options);
}


document.addEventListener('DOMContentLoaded', function(){ 
    // pushThePlayButton();
    setTimeout(test, 2600);  
}, false)


async function test() {
    updateChartWithStrings(['Getting started is 50% of the job done']);

}


var number = Math.floor(Math.random() * 8888) + 1111;

function beginTheThing() {
    init();
}
function init() {
    document.getElementById('connection_code').innerHTML = number;
    document.getElementById('connection_code').setAttribute('aria-label', `Connection Code is ${number}`);
    let btn = document.getElementById('init-btn');
    // var pointer = document.getElementById('the-pointer-to-show');
    btn.style.display = "none";
};

// init();
function perform_vibration(type = 1) {
    try {
        if (type == 0) {
            window.navigator.vibrate(300);
        } else if (type == 1) {
            window.navigator.vibrate([20, 30, 20,30,20]);
        } else if (type == 2) {
            window.navigator.vibrate([20]);
        }
    } catch (error) {
        console.log(error);
    }
   
}

var ID = function () {
    
    return (
        "_" +
        Math.random()
            .toString(36)
            .substr(2, 9)
    );
};
var client = new Paho.Client("wss://api.akriya.co.in:8084/mqtt",
    `clientId-wordtree-Viz-${ID()}`
);

// var client = new Paho.Client(
//     "api.akriya.co.in",
//     8083,
//     `clientId-91springboard_${ID}`
//   );


// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({ onSuccess: onConnect });

// called when the client connects
function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("onConnect");
    client.subscribe(`wordtree/${number}/connected`);
    client.subscribe(`wordtree/${number}/detected`);
    client.subscribe(`wordtree/${number}/phrase`);
    let message = new Paho.Message("Hello");
    message.destinationName = `adEngine/${number}/detected`;
    client.send(message);
    
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
        console.log("onConnectionLost:" + responseObject.errorMessage);
    }
}

// called when a message arrives
function onMessageArrived(message) {
    if (message.topic === `wordtree/${number}/detected`) {
        perform_vibration(0);
    } else if (message.topic === `wordtree/${number}/connected`){
        // show_options();
    } else if (message.topic === `wordtree/${number}/phrase`) {
        let phrase = message.payloadString;
        
        updateChartWithStrings([phrase]);
    }
    
    console.log(message);
    console.log("onMessageArrived:" + message.payloadString);
}
