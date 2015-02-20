'use strict';

/**
 * @ngdoc function
 * @name babymockrApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the babymockrApp
 */
angular.module('babymockrApp')
  .controller('MainCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
