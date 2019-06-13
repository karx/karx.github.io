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
        this.canvas = document.getElementById(this.data);
        this.ctx = canvas.getContext('2d');

        this.canvas.width = innerWidth;
        this.canvas.height = innerHeight;

        var imageData = this.ctx.createImageData(this.canvas.width, this.canvas.height);
        document.body.appendChild(this.canvas);

        (function loop() {

            for (var i = 0, a = imageData.data.length; i < a; i++) {
                imageData.data[i] = (Math.random() * 255) | 0;
            }

            this.ctx.putImageData(imageData, 0, 0);
            requestAnimationFrame(loop);

        })();
    }
});