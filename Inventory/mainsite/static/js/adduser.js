$(document).ready(function(){
const form = document.getElementById('addusrfrm');
form.addEventListener('submit', function(e){
    e.preventDefault();
     const firstname = document.getElementById('fname').value.trim();
     const lastname = document.getElementById('lname').value.trim();
     const phone = document.getElementById('phone').value.trim();
     const username = document.getElementById('username').value.trim();
     const email = document.getElementById('email').value.trim();
     const password = document.getElementById('password').value.trim();
     const cpassword = document.getElementById('cpassword').value.trim();
     const selgroup = document.getElementById('groups').value;
     const gender = $("input:radio.gendRadio:checked").val();
     let anyErrors = false;
     setErrorFor('fnamesmall', '');
     setErrorFor('lnamesmall', '');
     setErrorFor('username', '');
     setErrorFor('password', '');
     setErrorFor('phone', '');
     setErrorFor('cpassword', '');
     setErrorFor('emailsmall', '');
     setErrorFor('groupssmall', '');
     if(selgroup== 'null'){
        setErrorFor('groupssmall', 'Name cannot be blank');
        annyErrors = true;
     }
      if (firstname === '' || firstname === null)
    {
        setErrorFor('fnamsmall', 'Name cannot be blank');
        annyErrors = true;
    }
    if (lastname === '' || lastname === null)
    {
        setErrorFor('lnamesmall', 'Name cannot be blank');
        annyErrors = true;
    }
    //check phone number length
    if(phone.length <=8){
        setErrorFor('phonesmall', 'Phone number cannot be less than 8 characters');
        anyErrors = true;
    }
    if(phone.length > 15){
        setErrorFor('phonesmall', 'Phone number cannot be greater than 15 characters');
        anyErrors = true;
    }
     //check whether password field is empty
    if (password === ''||password === null)
    {
        setErrorFor('passwordsmall', 'Password field cannot be blank');
        anyErrors = true;
    }

    //check whether password character length is less than or equal to 8 characters
    else if (password.length <= 8)
    {
        setErrorFor('passwordsmall', 'Password must be longer than 8 characters');
        anyErrors = true;
    }

    //check whether password length is greater than or equal to 50 characters
    else if (password.length >= 50)
    {
        setErrorFor('passwordsmall', 'Password length must be less than 50 characters');
        anyErrors = true;
    }

    //check whether confirm password field is null
    if (cpassword === ''||cpassword === null)
    {
        setErrorFor('cpasswordsmall', 'This field cannot be empty');
        anyErrors = true;
    }

    //check whether password and cpassword are equal
    if(cpassword !== password)
    {
        //set error
        setErrorFor('passwordsmall', 'Passwords do not match');
        setErrorFor('cpasswordsmall', 'Passwords do not match');
        anyErrors = true;
    }

    //check whether email field is null
    if (email === '' || email === null)
    {
        //err
        setErrorFor('emailsmall', 'Email cannot be blank')
        anyErrors = true;
    }

    //if email is not valid email set error
    else if (!isEmail(email)){
        setErrorFor('emailsmall', 'That is not a valid email')
        anyErrors = true;
    }
    if (!anyErrors){
        sendData(fname, lname, username, email, password, phone, selgroup, gender);
    }
})
})
function isEmail(email) {
    let re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}

function setErrorFor(input, message) {
    const small = document.getElementById(input);
    small.textContext = '';
    small.textContent = message;
}
function setSuccessFor(){
        document.getElementById('fname').style = 'border: 2px solid green';
        document.getElementById('lname').style = 'border: 2px solid green';
        document.getElementById('username').style = 'border: 2px solid green';
        document.getElementById('email').style = 'border: 2px solid green';
        document.getElementById('password').style = 'border: 2px solid green';
        document.getElementById('phone').style = 'border: 2px solid green';
        document.getElementById('cpassword').style = 'border: 2px solid green';

}

//sending data via ajax
function sendData(fname, lname, username, email, password, phone, selgroup, gender){
    $.ajax({
        url: "",
        type: "POST",
         headers: {
            "X-CSRFToken" : $("input[name=csrfmiddlewaretoken]").val()
        },
        data: {
            'fullname': fname,
            'lastname': lname,
            'username': username,
            'email': email,
            'phone': phone,
            'group': selgroup,
            'gender': gender,
            'password': password,
        },
        success: function(result){
            response = JSON.parse(result);
            if(response.value){
                if(response.value == true){

                   setSuccessFor();

                    window.location.replace('/accounts/login/')
                }
            }
            else{
                console.log('Server error');
            }
        },
        error: function(result){
            console.log(result);
        }
    })
}