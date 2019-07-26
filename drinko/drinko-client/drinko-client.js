var stop_btn = document.getElementById('stop-btn');
var start_btn = document.getElementById('start-btn');
var discard_btn = document.getElementById('discard-btn');
var results = document.getElementById('results');

var name_of_user = document.getElementById('name-of-user').getAttribute('value');

var firestore = firebase.firestore();
var refId = null;
var start_time = null;
stop_btn.style.display = 'none';
start_btn.style.display = 'none';
discard_btn.style.display = 'none';

start_btn.onclick = () => {
    startCounter();
};

stop_btn.onclick = () => {
 stopCounter();
};


function startCounter() {
    console.log(name_of_user);
    var timeAtStart = Date.now();
    start_time = timeAtStart;
// el.target.value

    var obj = {
        nameOfUser: name_of_user,
        start_time: timeAtStart,
        isProd: true
    };
    console.log('name pushed : ' + name_of_user);
    firestore.collection('drinko').add(obj).then( (docRef) => {
        refId = docRef;
        console.log(docRef);

        stop_btn.style.display = 'block';
        start_btn.style.display = 'none';

        results.innerHTML = `Clock is ticking ${name_of_user} ⏲` ;
    })
    .catch( (error) => {
        console.error(error);
    });
    
}

function stopCounter() {
    console.log(refId);
    var timeAtEnd = Date.now();
    var beer_time = (new Date(timeAtEnd).getTime() - new Date(start_time).getTime())/1000;
    refId
        .update({
            stop_time: Date.now(), 
            beer_time: beer_time
        }).then ((opt) => {
            console.log(opt);
            start_btn.style.display = 'block';
            start_btn.innerHTML = "Restart";
            stop_btn.style.display = 'none';

            results.innerHTML = `You took ${beer_time} s for 🍺`;

        }).catch( (error) => {
            console.log(error);
        })
}



var name_of_user_input = document.getElementById('name-of-user');
name_of_user_input.onchange = (el) => {
    console.log(el.target.value);
    name_of_user = el.target.value;
    
}
var save_name = document.getElementById('save-name')
save_name.onclick = (el) => {
    name_of_user = document.getElementById('name-of-user').value;

    console.log(name_of_user);
    console.log(name_of_user_input);
    start_btn.style.display = 'block';
    save_name.style.display = 'none';
    name_of_user_input.hidden = true;
    change_name_btn.hidden = false;

    results.innerHTML = `Ready to 🍻 are you, ${name_of_user}!`;
}

var change_name_btn = document.getElementById('change-name');
change_name_btn.hidden = true;
change_name_btn.onclick = (el) => {
    start_btn.style.display = 'none';
    stop_btn.style.display = 'none';
    save_name.style.display = 'block';
    name_of_user_input.hidden = false;
    change_name_btn.hidden = true;

    
}

