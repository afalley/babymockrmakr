'use strict';
// Firstly, we need to wire this controller into the myApp module
angular.module('myApp')
  // Here we see the name of the controller defined.
  // Following the name, we see an anonymous function with two arguments.
  // These arguments are functionality being injected into the controller.
  // Think of this as being like including scripts in HTML. 
  // Unless they are referenced here, you cannot utilize them.
  .controller('DemoRouteController3', function ($scope, $http, Tools ) {
    // The rest of the function defines the behavior & data that the controller will manage.
    // In this instance, we are simply retri

    Tools.authGithub();
    var req = $http.get("https://api.github.com/orgs/twbs/repos");

    req.success(function(data){
      $scope.results = data;
      console.log(data);
    });
    req.error(function(data){
      $scope.error = ["there was a problem, houston"];
    });
    
  });