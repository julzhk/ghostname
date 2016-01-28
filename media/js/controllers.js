'user strict';

var helloWorldControllers = angular.module('hellowWorldControllers', []);

helloWorldControllers.controller('MainCtrl', ['$scope',
function MainCtrl($scope){
    $scope.message = 'Hello World!';
}]);

helloWorldControllers.controller('ShowCtrl', ['$scope',
function ShowCtrl($scope){
    $scope.message = 'show the world!';
}]);