AFRAME.registerComponent('smartcycle', {
    schema: {
        bikeNumber: { type: 'string', default: 'BK1001' },
        url: { type: 'string', default: 'bot.akriya.co.in' },
        degreeOffset: {type: 'number', default: 0},
        circleRadius: { type: 'number', default: 10}
    },

    init: function () {
        var data = this.data;
        var el = this.el;
        var position = el.object3D.position;
        this.bikeDegree = data.degreeOffset + (Math.random()%100);
        this.circleRadius = data.circleRadius + (10*((Math.random()%100)/100));
        this.bikeNumber = data.bikeNumber;
        this.rotateRate = 0.005 + (0.001*((Math.random()%100)/100));

        console.log(this.rotateRate);
        console.log(el);
        console.log(position);
        
        // Do something when component first attached.
        var client = new Paho.MQTT.Client(data.url, 8083, "clientId-webKaaroSim" + Math.random());
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
            console.log(message.destinationName);
        }

        // called when the client connects
        function onConnect() {
            // Once a connection has been made, make a subscription and send a message.
            console.log("onConnect");
            client.subscribe("World");
            message = new Paho.MQTT.Message("Hello");
            message.destinationName = "World";
            client.send(message);
            client.subscribe("kaaro/smartbike/#");

            client.subscribe("kaaro");

            

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
        this.bikeDegree += this.rotateRate;
        var position = el.object3D.position;
        el.object3D.position.set(
            this.circleRadius * Math.sin(this.bikeDegree), position.y ,this.circleRadius * Math.cos(this.bikeDegree)
        );
    },

});
