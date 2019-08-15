var finalTranscripts = "";
console.log(firebase);
var firestore = firebase.firestore();
function start() {
  if ("webkitSpeechRecognition" in window) {
    var speechRecognizer = new webkitSpeechRecognition();
    speechRecognizer.continuous = true;
    speechRecognizer.interimResults = true;
    speechRecognizer.lang = "en-US";
    speechRecognizer.start();
    var r = document.getElementById("result");

    speechRecognizer.onresult = function(event) {
      var interimTranscripts = "";
      for (var i = event.resultIndex; i < event.results.length; i++) {
        var transcript = event.results[i][0].transcript;
        transcript.replace("\n", "<br>");
        if (event.results[i].isFinal) {
          finalTranscripts += transcript;
        } else {
          interimTranscripts += transcript;
        }
        r.innerHTML =
          finalTranscripts +
          '<span style="color: #999;">' +
          interimTranscripts +
          "</span>";
      }
    };
    speechRecognizer.onerror = function(event) {};
  } else {
    r.innerHTML = "Your browser does not support that.";
  }
}

function sendCurrent() {
    firestore.collection("recordings").add ( {
        time: Date.now(),
        transcript: finalTranscripts,
        sent_by: window.navigator.userAgent
    }).then( (docRef) => {
        var r = document.getElementById("result");

        finalTranscripts = '';
        r.innerHTML = '<span style="color: green;">' +
        'Sent to kaaro' + 
        "</span>";
        console.log("@" , docRef.id);
    })
    .catch( (error) => {
        console.error(error);
    })
}
