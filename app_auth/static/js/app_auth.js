// Post profile_id ke backend
function loadDoc(profile_id, first_name, last_name, email, status) {
  $.ajax({
    type: 'POST',
    url: "/login/login/",
    data: {
      profile_id : profile_id,
      email : email,
      first_name : first_name,
      last_name : last_name,
      status : status,
    },
    success: function(data){
      console.log("berhasil masuk");
      alert(data)
      if (data == "employer baru") {
        window.open("http://localhost:8000/employer/edit_employer_profile/", '_self');
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
  var first_name = profile.getGivenName();
  var last_name = profile.getFamilyName();
  var email = profile.getEmail();
  // The ID token you need to pass to your backend:
  var id_token = googleUser.getAuthResponse().id_token;
  console.log("Employer");
  signOut();
  loadDoc(profile_id, first_name, last_name, email, "employer");
};

function onSignIn_job_seeker(googleUser) {
  // Useful data for your client-side scripts:
  var profile = googleUser.getBasicProfile();
  var profile_id = profile.getId();
  var first_name = profile.getGivenName();
  var last_name = profile.getFamilyName();
  var email = profile.getEmail();
  // The ID token you need to pass to your backend:
  var id_token = googleUser.getAuthResponse().id_token;
  console.log("Flag job_seeker");
  signOut();
  loadDoc(profile_id, first_name, last_name, email, "job_seeker");
};

function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut();
}
console.log("hi");
