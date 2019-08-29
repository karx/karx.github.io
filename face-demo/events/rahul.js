var firestore = firebase.firestore();
console.log('starting');

var face_id_list = [];
var last_face_guy_unsub = null;

var each_booth_faces = {
  "booth_id_1": {
    name: 'Most popular booth',
    entries: {
      "face_id_1" :{
        info: "here"
      },
      "OSUM_demo" :{
        info: "here"
      }

    },
  },
  "booth_id_2": {
    name: 'Most popular booth',
    entries: {},
  },
  "default" : {}

};

firestore.collection("users-face")
  .onSnapshot(function (querySnapshot) {
    console.log(querySnapshot);
    var faces = [];
    querySnapshot.forEach(function (doc) {
      faces.push({
        face_id: doc.data().FaceId,
        image_byte: doc.data().ImageByte,
        timestamp: doc.data().Timestamp
      });
    });
    console.log(faces.length);
    var html_to_push = "";

    faces.forEach((contestant) => {
      var cst = contestant;
      console.log(cst);
      if (!cst.face_id) {
        ;
      } else {
        html_to_push += `<div onclick="get_face_instances('${cst.face_id}')" class="each_face"> <div class="id">${cst.face_id}</div> <img id="profileImage" src="data:image/jpg;base64, ${cst.image_byte.toBase64()}"> </div>`;
      }
    });
    $('#registered').html(html_to_push);
  });


function get_face_instances(face_id) {
  if (last_face_guy_unsub) {
    last_face_guy_unsub();
  }
  last_face_guy_unsub = firestore.collection(`face-instances`).where("FaceId", "==", face_id).orderBy("Timestamp", "desc")
    .onSnapshot(function (querySnapshot) {
      console.log(querySnapshot);
      var instances = [];
      querySnapshot.forEach(function (doc) {
        instances.push({
          face_id: doc.data().FaceId,
          image_byte: doc.data().ImageByte,
          timestamp: doc.data().Timestamp
        });
      });
      console.log(instances.length);
      var html_to_push = `<h4>${instances.length}</h4>`;
      instances.forEach((contestant) => {
        var cst = contestant;
        console.log(cst);
        if (!cst.face_id) {
          ;
        } else {entries
          html_to_push += `<div class="each_face each_instance"> <div class="time">${cst.timestamp.toDate()}</div> <img id="profileImage" src="data:image/jpg;base64, ${cst.image_byte.toBase64()}"> </div>`;
        }
      });
      $('#entries').html(html_to_push);
    });

}

firestore.collection(`face-instances`)
  .onSnapshot( (snap) => {
    snap.forEach((each_guy) => {
      var booth_id = each_guy.data().BoothId;
      var face_id = each_guy.data().FaceId;
      if (!booth_id) {
        booth_id = "default"
      }

      if (!each_booth_faces[booth_id]) {
        each_booth_faces[booth_id] = new Object();
      }

      if (!each_booth_faces[booth_id][face_id]) {
        each_booth_faces[booth_id][face_id] = {
          image_byte: each_guy.data().ImageByte
        };

      }
    });
    console.log(each_booth_faces);
    refreshBoothUI();
  });

  // firestore.collection(`event-booths`).orderBy("name", "desc")
  // .onSnapshot( (querySnapshot) => {
  //   console.log(querySnapshot);
  //   var booths = [];
  //   querySnapshot.forEach(function (doc) {
  //     booths.push({
  //       name: doc.data().name,
  //       message: doc.data().message,
  //       when_to_send: doc.data().when_to_send
  //     });
  //   });
  //   console.log(booths.length);
  //   var html_to_push = "";

  //   booths.forEach((each_booth) => {
  //     var cst = each_booth;
  //     console.log(cst);
  //     if (!cst.name) {
  //       ;
  //     } else {
  //       html_to_push += `<div class="each_booth"> <div class="name">${cst.name}</div>  </div>`;
  //     }
  //   });
  //   $('#booth-entries').html(html_to_push);
  // });


$(".each_face").click((e) => {
  console.log(e);
})

function addNewBooth() {
  firestore.collection(`event-booths`).add({
    name: 'New Booth',
    message: 'Unique message for customers',
    when_to_send: 'On first visit'
  });
}

function refreshBoothUI() {
  var html_to_push = "";

  var allBoothsKeys = Object.keys(each_booth_faces);
  allBoothsKeys.forEach( (booth_id) => {
    html_to_push += `<div class="each_booth"> <div class="name">${booth_id}</div> <div class="face_entries"> `;

    var allFaceKeys = Object.keys(each_booth_faces[booth_id]);
    allFaceKeys.forEach( (face_id) => {
      
      var image_byte = each_booth_faces[booth_id][face_id].image_byte;
      if (image_byte) {
        html_to_push += `<div class="each_face_entry"> <img id="profileImage" src="data:image/jpg;base64, ${image_byte.toBase64()}"> </div> `;        
      }
    
    });

    html_to_push += `</div> </div>`
  });
  $('#booth-entries').html(html_to_push);

}