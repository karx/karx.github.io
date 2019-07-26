const  ctx = document.getElementById("canvas").getContext("2d")

  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

const draw = () => {
  
  updateBubbles();
  
  const width = ctx.canvas.width;
  const height = ctx.canvas.height;
  addBubbles(width, height);
  
  ctx.save();
  ctx.clearRect(0, 0, width, height);
  const grd=ctx.createLinearGradient(0, 0,width, height);
      grd.addColorStop(0,"#d2c200");
      grd.addColorStop(1,"#b55c00");
  ctx.fillStyle=grd;
  ctx.fillRect(0, 0, width, height);
  bubbles.map(v => {
    ctx.beginPath();
    ctx.arc(v.x, v.y, v.r, 0, 2 * Math.PI);
    ctx.strokeStyle = "#ffffff";
    ctx.globalAlpha = 0.8;
    ctx.lineWidth = 0.5;
    ctx.stroke();
    ctx.closePath();
    return v;
  });

  window.requestAnimationFrame(draw)
}

const bubbles = [];

const updateBubbles = () => {
  for (let i = bubbles.length - 1; i >= 0; i--) {
    if (bubbles[i].y < 120) {
      if (bubbles.length > 400) {
        bubbles.splice(0, 1)
      }
    } else {
      bubbles[i].y -= bubbles[i].s
    }
  }
};

class Bubble {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.r = [3, 4, 5][Math.floor(Math.random() * 3)];
    this.s = this.r === 5 ? 1 : this.r === 4 ? 1.2 : 1.4
  }
}

const addBubbles = (width, height) => {
  const x = Math.floor(Math.random() * width);
  const y = height;
  const bubble = new Bubble(x, y);
  if (Math.random() < 0.5) {
    bubbles.push(bubble);
  }
};


draw()
      

$(".panel").click(function() {
    if (!$(this).hasClass("active")) {
      var index = $(this).index();
      $("#order").removeClass();
      $("#order").addClass("opt" + (index + 1));
      $("#choice").get(0).selectedIndex = index;
      $(this)
        .siblings()
        .addClass("hidden");
      $(this).addClass("active");
      $("#order")
        .delay(800)
        .slideToggle(400);
    }
  });
  
  $("#back").click(function(e) {
    $("#order").slideToggle(400);
    var self = this;
    setTimeout(function() {
      $(".panel").removeClass("hidden active");
    }, 400);
    e.preventDefault();
  });
  
  $("#submit").click(function(e) {
    e.preventDefault();
  });
  
  $("#quantity").on("input change", function() {
    var qv = $("#quantity").val();
    if (qv % 1 != 0) {
      qv = parseInt(qv, 10);
      if (qv == 0) qv = "";
      qv += "½";
    }
    $('label[for="quantity"]').text(qv);
    // TODO: update the price as well
  });
  

  var firestore = firebase.firestore();
    firestore.collection("drinko").where("isProd", "==", true)
    .onSnapshot(function(querySnapshot) {
        var contestants = [];
        querySnapshot.forEach(function(doc) {
            contestants.push( {
                name: doc.data().nameOfUser,
                time: doc.data().beer_time
            });
        });
        console.log(contestants.length);
        contestants.sort((a, b) => (a.time > b.time) ? 1 : (a.time === b.time) ? 0 : -1 );
        if (contestants.length > 10) {
            contestants = contestants.slice(0, 10);
        }
        var html_to_push = "";
        contestants.forEach((contestant) => {
            var cst = contestant;
            console.log(cst);
            if (!cst.name) {
                ;
            } else {
                html_to_push += `<li> ${cst.name} <span> in ${cst.time} seconds</span></li>`;
            }
        });
        $('#leaderboard').html(html_to_push);
    });
