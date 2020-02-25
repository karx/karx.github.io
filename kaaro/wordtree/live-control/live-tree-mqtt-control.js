
let dev_id = '1111';
document.getElementById('btn-click').onclick =  () => {
    dev_id = document.getElementById('connection_code').value;
    sendConformationToMobile(dev_id);
    console.log(`Device Id set to ${dev_id}`);
};
var ID = function() {
    // Math.random should be unique because of its seeding algorithm.
    // Convert it to base 36 (numbers + letters), and grab the first 9 characters
    // after the decimal.
    return (
      "_" +
      Math.random()
        .toString(36)
        .substr(2, 9)
    );
  };
var client = new Paho.Client(
    "wss://api.akriya.co.in:8084/mqtt",
    `clientId-wordtree-Ctrl-${ID()}`
);

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({ onSuccess: onConnect });

// called when the client connects
function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("onConnect");
    client.subscribe("wordtree/Ctrl");
    let message = new Paho.Message("Hello");
    message.destinationName = "wordtree/Ctrl/presence";
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
    console.log("onMessageArrived:" + message.payloadString);
}

function sendConformationToMobile(message_in) {
    let message = new Paho.Message('Connected to Device ID');
    message.destinationName = `wordtree/${message_in}/connected`;
    client.send(message);
}
function sendPhrase(msg) {
    let message = new Paho.Message(msg);
    message.destinationName = `wordtree/${dev_id}/phrase`;
    client.send(message);
}

function parseAndActOnText(txt) {
    if (txt.length > 0) {
        console.log(txt);
        console.log(txt.length);
        sendPhrase(txt);
    }
   
}

var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition
var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent
var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList

async function listenForAllTheThingsTheUserSaysMostlyEntities() {
    // var colors = [ 'aqua' , 'azure' , 'beige', 'bisque', 'black', 'blue', 'brown', 'chocolate', 'coral' ... ];
    // var grammar = '#JSGF V1.0; grammar colors; public <color> = ' + colors.join(' | ') + ' ;'
    var recognizing;
    var recognition = new SpeechRecognition();
    // reset();
    // recognition.onend = reset;

    // var speechRecognitionList = new SpeechGrammarList();
    // speechRecognitionList.addFromString(grammar, 1);

    // recognition.grammars = speechRecognitionList;
    recognition.continuous = true;
    recognition.lang = 'en-US';
    recognition.interimResults = true;
    // recognition.maxAlternatives = 1;
    recognition.start();

    recognition.onresult = function (event) {
        let value_to_send = '';
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                value_to_send += event.results[i][0].transcript;
            }
          }
        parseAndActOnText(value_to_send);
    }

    recognition.onaudiostart = (event) => {
        console.log("Mic is On");
        document.getElementById('connection_code').style.backgroundColor ='#FF0000';

    }

    recognition.onend = (event) => {
        console.log("Ended");
        document.getElementById('connection_code').style.backgroundColor ='#00FF00';

        setTimeout(() => {
            recognition.start();
        },1000);
    }

    recognition.error = (event) => {
        console.log("Ended", event);
        document.getElementById('connection_code').style.backgroundColor ='#FF00FF';
    }

    
}

listenForAllTheThingsTheUserSaysMostlyEntities();
