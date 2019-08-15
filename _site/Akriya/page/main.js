AFRAME.registerComponent('kaaro-rotate', {
    schema: {

    },

    init: function () {
        var data = this.data;
        var el = this.el;

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

    },

});

AFRAME.registerComponent('draw-canvas', {
    schema: { default: '' },

    init: function () {
        var canvas = document.getElementById(this.data);
        ctx = canvas.getContext('2d');

        canvas.width = innerWidth;
        canvas.height = innerHeight;

        var imageData = ctx.createImageData(canvas.width, canvas.height);
        document.body.appendChild(canvas);

        (function loop() {

            for (var i = 0, a = imageData.data.length; i < a; i++) {
                imageData.data[i] = (Math.random() * 255) | 0;
            }

            ctx.putImageData(imageData, 0, 0);
            requestAnimationFrame(loop);

        })();
    }
});