AFRAME.registerComponent('registerevents', {
		init: function () {
			var marker = this.el;
			marker.addEventListener('markerFound', function() {
				var markerId = marker.id;
				console.log('markerFound', markerId);
				// TODO: Add your own code here to react to the marker being found.
			});
			marker.addEventListener('markerLost', function() {
				var markerId = marker.id;
				console.log('markerLost', markerId);
				// TODO: Add your own code here to react to the marker being lost.
			});
		}
	});


AFRAME.registerComponent('marker-logger', {
	multiple: true,

	init: function () {
		console.log('Hello, LoggerInit');
		this.directionVec3 = new THREE.Vector3();
		this.prevPosition = this.el.object3D.position;

	},
	tock: function (time, timeDelta) {
		
		var currentPosition = this.el.object3D.position;
		console.log(currentPosition);
		console.log(this.el.id);
		
	}
	

	});
