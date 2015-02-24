'use strict';

angular.module('myApp')

  .controller('DemoController', function ($scope, $http, DemoService, Tools) {

    $scope.babynames = [];

    var get_babynames = $http.get("http://127.0.0.1:8000/babynames/")
      .success(function(data){
        $scope.babynames = data;
      })
      .error(function(data){
        alert("Nope. Could not get teh babynames.");
      $scope.error = ["There was a problem retrieving the babynames."];
      })
    ;

    // $scope.add_babyname = function() {
    //   $scope.babynames.push({
    //     'name': $scope.new_babyname,
    //     'rank': 0,
    //     'mockr_user': 3
    //   });
    // }

    $scope.add_babyname = function(){
      $http.post(
        'http://127.0.0.1:8000/babynames/',
        {'name': $scope.new_babyname, 'rank': null, 'mockr_user': 1}
      )
        .success(function(data){
          $scope.babynames.push(data);
        })
        .error(function(data){
          alert("Babyname: "+$scope.new_babyname+"; post failed.");
        })
      ;
    };
  });

