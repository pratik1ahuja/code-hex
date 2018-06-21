function validation()
	{
	var uname=document.getElementById("uname").value;
	var pass=document.getElementById("upass").value;
	if(uname == "")
		{	
			alert("please Enter a Username!");
			return false;
		}
		else if(!isNaN(uname))
		{
			alert("please enter only Alphabets.");
		return false;
		}
		if(pass == "")
		{
			alert("please Enter a password!");
			return false;
		}

		  if((pass.length<6)||(pass.length>16))
			  {
				  alert("Your password length must contain minimum 6 character and maximum 16 character.");
				  return false;
			  }
		if(uname!=="root"){
			alert(" Your Username is incorrect");
			return false;
		}
		if(pass!=="12345678"){
			alert("Your password is incorrect. ");
			return false;
		}
		return true;
	}