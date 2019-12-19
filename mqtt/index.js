var mqtt = require('mqtt')
var client = mqtt.connect('http://api.akriya.co.in');



client.on('connect', function () {
    
    // client.publish('HS/303385001/status','11110000');
    // client.publish('homeSwitch/ready/2761046813','sReady!');
    console.log("published");
    start();
    client.subscribe('HS/#', function (err) {
        if (!err) {
            client.publish('HS/presence', 'Connected')
        } else {
            console.error(err);
        }
    });
    client.subscribe('homeSwitch/#', function (err) {
        if (!err) {
            client.publish('homeSwitch/presence', 'Connected')
        } else {
            console.error(err);
        }
    });
    client.subscribe('Kento/#');
    client.subscribe('digitalicon/#');
    
});


client.on('message', function (topic, message) {
    // message is Buffer
    console.log(`${topic}: ${message.toString()}`);
});


function turnOn() {
    let statusString = '';
    for (let i=0;i<8;i++) {
        let bit = Math.floor((Math.random() * 1000000) + 1)%2; 
        statusString += bit;    
    }
    
    client.publish('HS/303385001/status',statusString);
}

function turnOff() {
    client.publish('HS/303385001/status','00000000');
}
function timeout(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
async function sleep(fn, ...args) {
    await timeout(3000);
    return fn(...args);
}
async function start() {
    
    for(let i=0;i<100;i++) {
        console.log(i);
        turnOn();
        await timeout(1750);
    }
}


