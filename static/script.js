function valfname()
{
    var inputtext=document.getElementById('fname');
    var alphaExp = /^[a-zA-Z]+$/;
    var error=document.getElementById('fnameerror');
    if(inputtext.value.match(alphaExp))
    {
        error.innerHTML="";
    }
    else
    {
        error.innerHTML="Enter only alphabets";
    }
}
function vallname()
{
    var inputtext=document.getElementById('lname');
    var alphaExp = /^[a-zA-Z]+$/;
    var error=document.getElementById('lnameerror');
    if(inputtext.value.match(alphaExp))
    {
        error.innerHTML="";
    }
    else
    {
        error.innerHTML="Enter only alphabets";
    }
}
function valmob()
{
    var input=document.getElementById('mobile');
    var email=document.getElementById('email');
    var exp=/^[0-9]+$/;
    var error=document.getElementById('mobileerror');
    console.log(input.value);
    if(input.value.length==10 && input.value.match(exp))
    {
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/checkmob', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send('mobile=' + input.value+'&email='+email.value);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                if (response.exists) {
                    error.innerHTML = "Mobile number already exists";
                } else {
                    error.innerHTML = "";
                }
            }
        };
        error.innerHTML=""
    }
    else 
    {
        // console.log(input.value);
        error.innerHTML="Enter valid mobile number";
    }
}
function valemail()
{
    var input=document.getElementById('email');
    var exp=/^[a-zA-Z0-9_]+@[a-zA-Z0-9.]+\.[a-zA-Z0-9]{2,4}$/;
    var error=document.getElementById('emailerror');
    var email=input.value;
    if(input.value.match(exp))
    {
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/check', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send('email=' + email);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                if (response.exists) {
                    error.innerHTML = "Email already exists";
                } else {
                    error.innerHTML = "";
                }
            }
        };
        
    }
    else
    {
        error.innerHTML="Enter valid email ID";
    }
}
function valemailedit()
{
    var input=document.getElementById('email');
    var mobile=document.getElementById('mobile').value;
    var exp=/^[a-zA-Z0-9_]+@[a-zA-Z0-9.]+\.[a-zA-Z0-9]{2,4}$/;
    var error=document.getElementById('emailerror');
    var email=input.value;
    if(input.value.match(exp))
    {
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/checkedit', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send('email=' + email+'&mobile='+mobile);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                if (response.exists) {
                    error.innerHTML = "Email already exists";
                } else {
                    error.innerHTML = "";
                }
            }
        };
        
    }
    else
    {
        error.innerHTML="Enter valid email ID";
    }
}
function valdate()
{
    var input=document.getElementById('dob');
    var inputdate=new Date(input.value);
    var current=new Date();
    var error=document.getElementById('doberror');
    if(inputdate>current)
    {
        error.innerHTML="Enter valid date";
    }
    else
    {
        error.innerHTML='';
    }

}
function check()
{
    var email=document.getElementById('emailerror').innerHTML;
    var fname=document.getElementById('fnameerror').innerHTML;
    var lname=document.getElementById('lnameerror').innerHTML;
    var mobile=document.getElementById('mobileerror').innerHTML;
    var dob=document.getElementById('doberror').innerHTML;

    if(!(email==='' && fname==='' && lname==='' && mobile===''  && dob===''))
    {
        event.preventDefault();
    }

}

