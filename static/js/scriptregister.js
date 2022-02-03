const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');
const yzm = document.getElementById('yzm');
var flag=false;

document.getElementById("btn1").addEventListener('click', e => {
	e.preventDefault();
	checkInputs();
});

document.getElementById("huoquyzm").addEventListener('click', e => {
	e.preventDefault();
	checkInputsVerificationCode();
});

function checkInputs() {
	// trim to remove the whitespaces
	const usernameValue = username.value.trim();
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();
	const yzmValue = yzm.value.trim();
	
	if(usernameValue === '') {
		setErrorFor(username, '用户名不能为空');
		flag=false
	} else {
		setSuccessFor(username);
		flag=true
	}
	
	if(emailValue === '') {
		setErrorFor(email, '邮箱不能为空');
		flag=false
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, '邮箱格式不正常');
		flag=false
	} else {
		setSuccessFor(email);
		var emailValue1=emailValue.toLowerCase()
		email.innerHTML=emailValue1;
		flag=true
	}
	
	if(passwordValue === '') {
		setErrorFor(password, '密码不能为空');
		flag=false
	} else {
		setSuccessFor(password);
		flag=true
	}
	
	if(password2Value === '') {
		setErrorFor(password2, '密码不能为空');
		flag=false
	} else if(passwordValue !== password2Value) {
		setErrorFor(password2, '两次密码不正确');
		flag=false
	} else{
		setSuccessFor(password2);
		flag=true
	}

	if(yzmValue === '') {
		setErrorFor(yzm, '请输入验证码！');
		flag=false
	} else {
		setSuccessFor(yzm);
		flag=true
	}
	if(flag==true){
		registerPost()
	}
}

function checkInputsVerificationCode() {
	// trim to remove the whitespaces
	const usernameValue = username.value.trim();
	var emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();
	
	if(usernameValue === '') {
		setErrorFor(username, '用户名不能为空');
		flag=false
	} else {
		setSuccessFor(username);
		flag=true
	}
	
	if(emailValue === '') {
		setErrorFor(email, '邮箱不能为空');
		flag=false
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, '邮箱格式不正常');
		flag=false
	} else {
		setSuccessFor(email);
		emailValue=emailValue.toLowerCase()
		email.value=emailValue
		flag=true
	}
	
	if(passwordValue === '') {
		setErrorFor(password, '密码不能为空');
		flag=false
	} else {
		setSuccessFor(password);
		flag=true
	}
	
	if(password2Value === '') {
		setErrorFor(password2, '密码不能为空');
		flag=false
	} else if(passwordValue !== password2Value) {
		setErrorFor(password2, '两次密码不一致');
		flag=false
	} else{
		setSuccessFor(password2);
		flag=true
	}
	
	if(flag==true){
		getVerificationCode()
	}
}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}
	
function isEmail(email) {
	return /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/.test(email);
}

function registerPost(){
	$.load('注册中……')
	$.ajax({
		url:'/register',
		dataType:'json',
		type:'POST',
		data:{
			id:$('#username').val(),
			pass:$('#password').val(),
			email:$('#email').val(),
			flagyzm:'False',
			yzm:$('#yzm').val(),
		},
		success:
		function(results){
			$.loaded();
			if (results.success==200){
				$.alert('注册成功！'+results.zcjg,function(){
				window.location.href="/login";
			})
			}
			else{
				$.alert('注册失败！'+results.zcjg)
			}
		},
		error:
		function(err){
			$.loaded();
			$.alert('请求失败！'+err.status + '(' + err.statusText + ')') 
		}
	})
}

function getVerificationCode(){
	$.load('获取验证码中……')
	$.ajax({
		url:'/register',
		dataType:'json',
		type:'POST',
		data:{
			id:$('#username').val(),
			pass:$('#password').val(),
			email:$('#email').val(),
			flagyzm:'True',
		},
		success:
		function(results){
			$.loaded();
			if (results.success==200){
				$.alert('获取验证码成功！'+results.yzmjg)
			}
			else{
				$.alert('获取验证码失败！'+results.zcjg)
			}
		},
		error:
		function(err){
			$.loaded();
			$.alert('请求失败！'+err.status + '(' + err.statusText + ')') 
		}
	})
}