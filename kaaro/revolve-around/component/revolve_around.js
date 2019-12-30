var countOfRotates = 0;
AFRAME.registerComponent('revolve-around', {
  schema: {
    radius: { type: 'number', default: 5 },
    speed: { type: 'number', default: 1 },
    axis: { type: 'string', default: '1 0 0' },
    offset: { type: 'string', default: '0 0 0' },
    random_offset: {type: 'boolean', default: true}
  },
  multiple: true,

  init: function () {
    console.log('Hello, World!');
    let overlap_offset = this.data.random_offset ? (Math.ceil(Math.random()*12)) : countOfRotates;
    this.current_angle = 0.0 + ( countOfRotates > 0 ? (Math.PI/12 * overlap_offset) : 0);
    console.log(this.data.offset);
    console.log(this.data.offset.x);
    console.log(`Count of Rotates ${++countOfRotates}`);
  },
  tick: function () {
    var data = this.data;  // Component property values.
    var el = this.el;  // Reference to the component's entity.
    var pos = el.getAttribute('position');
    var rot = el.getAttribute('rotation') || '0 0 0';
    var radius = data.radius;
    var angle = this.current_angle;

    var new_pos = `${radius * Math.sin(angle)}, 0, ${radius * Math.cos(angle)}`

    el.setAttribute('position', new_pos);
    // console.log(` delta = ${this.data.speed} | Angle = ${this.current_angle} rads`);
    this.current_angle += (this.data.speed / 100.0);
    // console.log(` ${new_pos} | Angle = ${this.current_angle} rads`);
  }
});