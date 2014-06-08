function tornado() {
  
  function chart(selection) {
 
    selection.each(function(data) {


    var mData = data[0],
        fData = data[1];
    
    var min = d3.min([d3.min(mData), d3.min(fData)]) ,
        max = d3.max([d3.max(mData), d3.max(fData)]),
        scale = d3.scale.linear().range([10, maxBarWidth]).domain([min, max]);
    
    var vis = d3.select(this);

    var containers = vis 
      .selectAll('.gender-container')
      .data(data)
      .enter()
        .append('div')
        .attr('class', 'gender-container');

    containers
      .selectAll('.age-bar')
      .data(function(d) { return d; })
      .enter()
        .append('div')
        .attr('class', function(d, i, j) {
          return classes[j] + " age-bar";
        })
        .style('width', function(d) { return scale(d) + "px"; })
        .style('top', function(d, i, j) { return i * barHeight + "px"; })
        .attr('title', function(d, i, j) { return classes[j] + ":" + d; });
  
  });

  }
  
  return chart;
}
