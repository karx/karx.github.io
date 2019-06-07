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
	init: function () {
		console.log('Hello, LoggerInit');
		this.directionVec3 = new THREE.Vector3();
		this.prevPosition = this.el.object3D.position;

	},
	tick: function (time, timeDelta) {
		var directionVec3 = this.directionVec3;
		var currentPosition = this.el.object3D.position;
		console.log(prevPosition);
		console.log(currentPosition);
		directionVec3.copy(prevPosition).sub(currentPosition);
		var distance = directionVec3.length();
		if (distance < 1) { return; }
		var factor = this.data.speed / distance;
		['x', 'y', 'z'].forEach(function (axis) {
		  directionVec3[axis] *= factor * (timeDelta / 1000);
		});
		console.log("Moved!! " + this.el.id);
		console.log(directionVec3);

	}

	});
