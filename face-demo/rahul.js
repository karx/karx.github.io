var firestore = firebase.firestore();
console.log('starting');

var face_id_list = [];
var last_face_guy_unsub = null;

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

firestore.collection(`face-instances`).orderBy("Timestamp", "desc").limit(1)
  .onSnapshot( (snap) => {
    snap.forEach((last_guy) => {
      $("#latest").html(`<div> <div class="time">${last_guy.data().Timestamp.toDate()}</div> <img id="profileImage" src="data:image/jpg;base64, ${last_guy.data().ImageByte.toBase64()}"> </div>`);
    });
  });


$(".each_face").click((e) => {
  console.log(e);
})