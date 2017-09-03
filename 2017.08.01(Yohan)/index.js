var userInfo, database, auth;
var address = document.getElementById("address");
var submitBtn = document.getElementById("submitBtn");
var Customertype = document.getElementById("Customertype");
var authProvider = new firebase.auth.GoogleAuthProvider();

  // Initialize Firebase
  var config = {
    apiKey: "AIzaSyAX3zsgsAVgY2FoikSWi8Ou130mPv2RrFA",
    authDomain: "testfirebase-88dad.firebaseapp.com",
    databaseURL: "https://testfirebase-88dad.firebaseio.com",
    projectId: "testfirebase-88dad",
    storageBucket: "testfirebase-88dad.appspot.com",
    messagingSenderId: "727840492650"
  };
  firebase.initializeApp(config);
  
auth = firebase.auth();
database = firebase.database(); // DB 초기화

auth.onAuthStateChanged(function(user) {
  if (user) {
    // 인증 성공시
    console.log("success");
    userInfo = user;
  } else {
    auth.signInWithPopup(authProvider);

  }
});


function submitClick() {
  var firebaseRef = firebase.database().ref();
  var messageText = address.value;
  var CustypeText = Customertype.value;
  firebaseRef.child("Users/" + userInfo.uid).child("address").set(messageText);
  firebaseRef.child("Users/" + userInfo.uid).child("Customertype").set(CustypeText);


}
