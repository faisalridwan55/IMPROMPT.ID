// Post profile_id ke backend
function loadDoc(profile_id, full_name, email, status) {
  // var xhttp = new XMLHttpRequest();
  // xhttp.onreadystatechange = function() {
  //   if (this.readyState == 4 && this.status == 200) {
  //     // document.getElementById("demo").innerHTML = this.responseText;
  //   }
  // };
  // xhttp.open("POST", "/public_home/login/", true);
  // xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  // xhttp.send("profile_id=" + profile_id + "&full_name=" + full_name + "&email=" + email + "&status=" + status + "");
  // // refresh();
  $.ajax({
    type: 'POST',
    url: "/public_home/login/",
    data: {
      profile_id : profile_id,
      email : email,
      full_name : full_name,
      status : status,
    },
    success: function(data){
      alert(data)
      if (data == "employer baru") {
        window.open("http://localhost:8000/employer/edit_company_profile/", '_self');
      } else if (data == "employer lama") {
        window.open("http://localhost:8000/employer/home/", '_self');
      } else if (data == "job_seeker baru") {
        window.open("http://localhost:8000/job_seeker/edit_profile/", '_self');
      } else if (true) {
        window.open("http://localhost:8000/job_seeker/home/", '_self');
      }
    },
    error: function(){
      alert("Failed");
      window.location.reload();
    }
  })
}
// Untuk sign-in
function onSignIn_employer(googleUser) {
  // Useful data for your client-side scripts:
  var profile = googleUser.getBasicProfile();
  var profile_id = profile.getId();
  var full_name = profile.getName();
  var email = profile.getEmail();
  // The ID token you need to pass to your backend:
  var id_token = googleUser.getAuthResponse().id_token;
  console.log("ID Token: " + id_token);
  signOut();
  loadDoc(profile_id, full_name, email, "employer");
  // refresh("employer");
};
function onSignIn_job_seeker(googleUser) {
  // Useful data for your client-side scripts:
  var profile = googleUser.getBasicProfile();
  var profile_id = profile.getId();
  var full_name = profile.getName();
  var email = profile.getEmail();
  // The ID token you need to pass to your backend:
  var id_token = googleUser.getAuthResponse().id_token;
  console.log("ID Token: " + id_token);
  signOut();
  loadDoc(profile_id, full_name, email, "job_seeker");
  // refresh("job_seeker");
};
// function refresh(status){
//   window.open("test/"+status+"/", '_self');
// }
function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut();
}
