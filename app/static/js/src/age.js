/*
[
{
  "sex":"M",
  "age": 0,
  "pop2000": 30479,
  "pop2008": 32055
},
{
  "sex": "M",
  "age": 1,
  "pop2000": 29904,
  "pop2008": 32321
}
]
*/
var numAges = 85;

var data = createRandomData();

data = transformData(data);

var maxBarWidth = 200,
    m
    min = d3.min([d3.min(data[0]), d3.min(data[1])]) ,
    max = d3.max([d3.max(data[0]), d3.max(data[1])]),
    scale = d3.scale.linear().range([10, maxBarWidth]).domain([min, max]),
    classes = ['male', 'female'],
    barHeight = 10;



var chart = tornado();

function renderViz(container, chart) {
    var vis = d3.select(container);
    vis.datum(data);
    var t = d3.select(container).transition().duration(500);
    t.call(chart);
}


function update(state) {
  data = createRandomData();
  data = transformData(data);
  renderViz('#viz', chart);
}


d3.select('select').on('change', function() {
    var state = this.value;
    update(state);
});

function createRandomData() {
  var d = d3.range(numAges).map(function(age) {
    return [
      {
        sex: "M",
        age: age,
        pop2000: randomInRange(100, 5000),
        pop2008: randomInRange(100, 5000)
      },
      {
        sex: "F",
        age: age,
        pop2000: randomInRange(100, 5000),
        pop2008: randomInRange(100, 5000)
      }
    ];
  });

  d = _.flatten(d);
  
  return d;
}

function randomInRange(min, max) {
  if (arguments.length != 2) {
    min = 1, max = 10;
  }
  return parseInt(min + (Math.random() * ((max-min) + 1)), 10);
}

function transformData(_data) {
  var g1 = _.groupBy(_data, 'sex');
  
  _.each(g1, function(v, k) { g1[k] = _.groupBy(v, function(d){ return parseInt(d.age/11); }); });
  
  _.each(g1, function(v, k){ _.each(v, function(ages, a){ v[a] = _.reduce(ages, function(memo, d){ return memo + d.pop2000; }, 0); }); });
  
  var d = [];

  // Male data
  d[0] = [];
  for(var i=0; i < _.keys(g1.M).length; i++) {
    d[0].push(g1.M[i]);
  }

  
  // Female data
  d[1] = [];
  for(var i=0; i < _.keys(g1.F).length; i++) {
    d[1].push(g1.F[i]);
  }
  
  return d;
}

// Init
// ----

update();
