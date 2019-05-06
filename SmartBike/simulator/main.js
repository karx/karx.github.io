AFRAME.registerComponent('smartcycle', {
    schema: {
        bikeNumber: { type: 'string', default: 'BK1001' },
        url: { type: 'string', default: 'bot.akriya.co.in' }

    },

    init: function () {
        var data = this.data;
        var el = this.el;
        var position = el.object3D.position;
        this.bikeNumber = data.bikeNumber;
        console.log(data);
        console.log(el);
        console.log(position);
        el.addEventListener('connectedMQTT', () => {
            console.log("in eventListener for connected");
            el.emit('connectToNewChannel', {
                topic: 'kaaro',
                callback: (data) => {
                    console.log("kaaro: ", data);
                }
            });
        })
        // Do something when component first attached.
        var client = new Paho.MQTT.Client(data.url, 8083, "clientId-webKaaroSim");
        client.onConnectionLost = onConnectionLost;
        client.onMessageArrived = onMessageArrived;
        client.connect({ onSuccess: onConnect });

        function onConnectionLost(responseObject) {
            if(responseObject.errorCode !== 0) {
        console.log("onConnectionLost:" + responseObject.errorMessage);
        }
            }
    
        function onMessageArrived(message) {
            console.log("onMessageArrived:" + message.payloadString);
        }

        // called when the client connects
        function onConnect() {
            // Once a connection has been made, make a subscription and send a message.
            console.log("onConnect");
            client.subscribe("World");
            message = new Paho.MQTT.Message("Hello");
            message.destinationName = "World";
            client.send(message);
            el.addEventListener('connectToNewChannel', (eventData) => {
                var details = eventData.detail;
                var topic = details.topic;
                console.log(eventData);
                console.log(details.topic);
                console.log(details.callback);
                client.subscribe(topic, {
                    onSuccess: details.callback
                });
            });
            el.emit('connectedMQTT', { connectedTo: data.url });

        }
    },

    update: function () {
        // Do something when component's data is updated.
    },

    remove: function () {
        // Do something the component or its entity is detached.
    },

    tick: function (time, timeDelta) {
        // Do something on every scene tick or frame.
        var el = this.el;
        var position = el.object3D.position;
        el.object3D.position.set(
            position.x + 0.001, position.y, position.z
        );
    },

});
