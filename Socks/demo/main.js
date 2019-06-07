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
		
		var directionVec3 = this.directionVec3;
		var currentPosition = this.el.object3D.position;
		if (this.prevPosition)
		{
			directionVec3.copy(this.prevPosition).sub(currentPosition);
			var distance = directionVec3.length();
			if (distance < 1) { return; }
			var factor = this.data.speed / distance;
			['x', 'y', 'z'].forEach(function (axis) {
			  directionVec3[axis] *= factor * (timeDelta / 1000);
			});
			console.log("Moved!! " + this.el.id);
			console.log(directionVec3);
			this.prevPosition = currentPosition;
	
		} else {
			this.prevPosition = currentPosition;
		}
		// console.log(prevPosition);
		
	}

	});

	AFRAME.registerComponent('place-the-box', {
		
		init: function() {
			console.log('init the place the box box');

		}

		
	});
	
	AFRAME.registerComponent('move-the-box', {
			
		init: function () {
			console.log('Hello, Mobe the box');
			this.directionVec3 = new THREE.Vector3();
			this.prevPosition = this.el.object3D.position;
	
		},
		tock: function (time, timeDelta) {
			
			var currentPosition = this.el.object3D.position;
			if (this.prevPosition)
			{
				
				this.prevPosition = currentPosition;
				var box_to_move_el = document.querySelector("place-the-box");
				box_to_move_el.setAttribute('position', {currentPosition.x, currentPosition.y+ 1, currentPosition.z});
				
	
			} else {
				this.prevPosition = currentPosition;
			}
			
			
		}
	
		});