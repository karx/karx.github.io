const redditOverlayEl = document.querySelector('redditOverlay');

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
	
	AFRAME.registerComponent('detect-the-box', {
			
		init: function () {
			console.log('Hello, Mobe the box');
			this.directionVec3 = new THREE.Vector3();
			this.prevPosition = this.el.object3D.position;
	
		},
		tock: function (time, timeDelta) {
			
			var currentPosition = this.el.object3D.position;
			if (currentPosition.x === currentPosition.y && currentPosition.y === currentPosition.z && currentPosition.z === 0)
				return;
			console.log(currentPosition);
			var event = new CustomEvent("R-in-view", {
				detail: {
				  hazcheeseburger: true
				}
			  });
			  redditOverlayEl.dispatchEvent(event);
		}
	
		});

		redditOverlayEl.addEventListener('R-in-view', e=> {
			console.log(redditOverlayEl.style);
			redditOverlayEl.style.opacity = redditOverlayEl.style.opacity + 0.1;
		})