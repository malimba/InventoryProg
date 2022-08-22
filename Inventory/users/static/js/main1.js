$(document).ready(function(){
const form = document.getElementById('loginform');
    form.addEventListener('submit', function(e){
        //prevent default action of submit
        e.preventDefault();
        //start checks
        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value.trim();

        let anyErrors = false;
        setErrorFor('usernamesmall', '');
        setErrorFor('passwordsmall', '');
       if (username === '' || username === null)
    {
        setErrorFor('usernamesmall', 'Username cannot be blank');
        annyErrors = true;
    }
     //check whether password field is empty
    if (password === ''||password === null)
    {
        setErrorFor('passwordsmall', 'Password field cannot be blank');
        anyErrors = true;
    }


    if(!anyErrors){
        sendData(username, password);
    }

    })
})


function setErrorFor(input, message) {
    const small = document.getElementById(input);
    small.textContext = '';
    small.textContent = message;
}
function setSuccessFor(){
        document.getElementById('username').style = 'border: 2px solid green';
        document.getElementById('password').style = 'border: 2px solid green';
}

//sending data via ajax
function sendData(username, password){
    $.ajax({
        url: "",
        type: "POST",
         headers: {
            "X-CSRFToken" : $("input[name=csrfmiddlewaretoken]").val()
        },
        data: {
            'username': username,
            'password': password,
        },
        success: function(result){
            response = JSON.parse(result);
            if(response.value){
                if(response.value == 'pass'){
                    setErrorFor('passwordsmall', 'Password incorrect!')
                }
                if(response.value == 'username'){
                    setErrorFor('usernamesmall', 'Username incorrect!')
                }
                if(response.value == 'both'){
                    setErrorFor('usernamesmall', 'Username does not exists!')
                    setErrorFor('passwordsmall', 'Password does not exists!')
                }
                if(response.value == true){

                   setSuccessFor();

                    window.location.replace('/')
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
