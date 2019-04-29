AFRAME.registerComponent('log', {
    schema: {type: 'string'},
  
    init: function () {
      var stringToLog = this.data;
      console.log(stringToLog);
    }
  });

  AFRAME.registerComponent('bird-listeners', {
    init: function () {
    //   var lastIndex = -1;
    //   var COLORS = ['red', 'green', 'blue'];
      this.el.addEventListener('click', function (evt) {
        // lastIndex = (lastIndex + 1) % COLORS.length;
        this.setAttribute('alongpath', 'curve: #track2; delay:2000; loop:true; dur:6000');
        this.setAttribute('animation', 'property: position; to: 0 10 -80; dur: 1500; easing: easeOutElastic');

        console.log('I was clicked at: ', evt.detail.intersection.point);
      });
    }
  });