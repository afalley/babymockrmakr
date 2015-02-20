'use strict';

/**
 * @ngdoc overview
 * @name babymockrApp
 * @description
 * # babymockrApp
 *
 * Main module of the application.
 */
angular
  .module('babymockrApp', [
    'ngRoute'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
