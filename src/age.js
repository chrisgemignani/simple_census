var stateData = {
  "Alabama": {
    10: {
      "male": 100,
      "female": 200
    },
    20: {
      "male": 150,
      "female": 250
    },
    30: {
      "male": 200,
      "female": 300
    }
  },

  "Alaska": {
    10: {
      "male": 150,
      "female": 250
    },
    20: {
      "male": 200,
      "female": 300
    },
    30: {
      "male": 250,
      "female": 350
    }
  }

};


var state = "Alabama";

var data = stateData[state];

var mData = [],
    fData = [];

var maxBarWidth = 200,
    min = d3.min([d3.min(mData), d3.min(fData)]) ,
    max = d3.max([d3.max(mData), d3.max(fData)]),
    scale = d3.scale.linear().range([10, maxBarWidth]).domain([min, max]),
    classes = ['male', 'female'],
    barHeight = 10;



var chart = tornado();

function renderViz(container, chart) {
    var vis = d3.select(container);
    vis.datum([mData, fData]);
    //var t = d3.select(container).transition().duration(500);
    //t.call(chart);
    vis.call(chart);
}

function update(state) {
  data = stateData[state];
  _.each(data, function(v, k) {
    mData.push(v.male);
    fData.push(v.female);
  });
  renderViz('#viz', chart);
}

d3.select('select').on('change', function() {
    var state = this.value;
    update(state);
});


update(state);


