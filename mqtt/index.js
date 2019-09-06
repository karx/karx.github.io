var mqtt = require('mqtt')
var client = mqtt.connect('http://api.akriya.co.in');



client.on('connect', function () {
    
    client.publish('homeSwitch/ready/kaaroo','iamon');
    client.publish('homeSwitch/ready/2761046813','Ready!');
    console.log("published");
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
});


client.on('message', function (topic, message) {
    // message is Buffer
    console.log(`${topic}: ${message.toString()}`);
});