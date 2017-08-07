
var userInfo,database, auth;
var address = document.getElementById("address");
var submitBtn = document.getElementById("submitBtn");
var Customertype = document.getElementById("Customertype");
var authProvider = new firebase.auth.GoogleAuthProvider();

  // Initialize Firebase
  var config = {
    apiKey: "AIzaSyCWOhjgubSMNEavwmvC4QPNZOuzZ63Hyb4",
    authDomain: "safetybb-65f64.firebaseapp.com",
    databaseURL: "https://safetybb-65f64.firebaseio.com",
    projectId: "safetybb-65f64",
    storageBucket: "safetybb-65f64.appspot.com",
    messagingSenderId: "909521276736"
  };
  firebase.initializeApp(config);

auth = firebase.auth();
database = firebase.database(); // DB 초기화

auth.onAuthStateChanged(function(user)
{
  if(user) {
    // 인증 성공시
    console.log("success");
    userInfo = user;
  }
  else {
    auth.signInWithPopup(authProvider);
    auth.signInWithRedirect(authProvider);
  }
});


function submitClick() {
  var firebaseRef = firebase.database().ref();
  var messageText = address.value;
  var CustypeText = Customertype.value;
  firebaseRef.child("Users/" + userInfo.uid).child("address").set(messageText);
  firebaseRef.child("Users/" + userInfo.uid).child("Customertype").set(CustypeText);


}
