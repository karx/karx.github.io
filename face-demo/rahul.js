  var firestore = firebase.firestore();
  console.log('starting');

  var face_id_list = [];

  firestore.collection("users-face")
    .onSnapshot(function(querySnapshot) {
      console.log(querySnapshot);
        var faces = [];
        querySnapshot.forEach(function(doc) {
            faces.push( {
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
                html_to_push += `<div onclick="get_face_instances('${cst.face_id}')" class="each_face"> ${cst.face_id} <img id="profileImage" src="data:image/jpg;base64, ${cst.image_byte.toBase64()}"> </div>`;
            }
        });
        $('#registered').html(html_to_push);
    });


    function get_face_instances(face_id) {
      firestore.collection(`mange-users-face/${face_id}/attendance`)
      .onSnapshot(function(querySnapshot) {
        console.log(querySnapshot);
          var instances = [];
          querySnapshot.forEach(function(doc) {
              instances.push( {
                  face_id: doc.data().FaceId,
                  image_byte: doc.data().ImageByte,
                  timestamp: doc.data().Timestamp
              });
          });
          console.log(instances.length);
          var html_to_push = "";
          instances.forEach((contestant) => {
              var cst = contestant;
              console.log(cst);
              if (!cst.face_id) {
                  ;
              } else {
                  html_to_push += `<li> ${new Date(cst.timestamp)} <img id="profileImage" src="data:image/jpg;base64, ${cst.image_byte.toBase64()}"> </li>`;
              }
          });
          $('#entries').html(html_to_push);
      });
    
    }

$(".each_face").click( (e) => {
  console.log(e);
})