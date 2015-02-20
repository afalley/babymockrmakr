'use strict';

/**
 * @ngdoc function
 * @name babymockrApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the babymockrApp
 */
angular.module('babymockrApp')
  .controller('AboutCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
