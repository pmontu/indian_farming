var app = angular.module("indian_farming", ['ngRoute'])

app.controller("loginController", function($scope, $http){
	$scope.user = {
		username: "",
		password: "",
		grant_type: "password"
	}
	$scope.submit = function(){
		console.log($scope.user)
		$http.post("http://127.0.0.1:8000/o/token/", data=$scope.user).then(function(res){
			console.log(res)
		}, function(res){
			console.log(res.data.error, res.status, res.statusText)
		})
	}
})


app.config(function($routeProvider,$httpProvider){
	
	$routeProvider.when('/',{
			controller: "loginController",
			templateUrl: "login.html"
		
		});
});