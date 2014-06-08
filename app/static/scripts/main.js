require.config({
  shim: {
    'lodash': {
      exports: '_'
    },
    'backbone': {
      deps: [
        'lodash',
        'jquery'
      ],
      exports: 'Backbone'
    }
  },
  paths: {
    jquery   : '../lib/jquery',
    lodash   : '../lib/lodash',
    backbone : '../lib/backbone'
    d3       : '../lib/d3'
  }
});

require([
  './views/census',
], function(CensusView) {

  debugger;
  new CensusView();

});
