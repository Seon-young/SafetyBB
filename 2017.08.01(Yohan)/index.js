
var userInfo,database, auth;
var address = document.getElementById("address");
var submitBtn = document.getElementById("submitBtn");
var Customertype = document.getElementById("Customertype");
var authProvider = new firebase.auth.GoogleAuthProvider();

auth = firebase.auth();
database = firebase.database(); // DB 초기화

auth.onAuthStateChanged(function(user)
{
  if(user) {
    // 인증 성공시
    console.log("success");
    console.log(user);
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

  console.log(userInfo.uid);

  firebaseRef.child(userInfo.uid).child("address").set(messageText);
  firebaseRef.child(userInfo.uid).child("Customertype").set(CustypeText);

}
