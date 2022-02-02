const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');
const yzm = document.getElementById('yzm');
var flag=false

var eye = document.getElementById("eye");
var pwd = document.getElementById("pwd");
function showhide(){

		if (pwd.type == "password") {
			pwd.type = "text";
				eye.className='fa fa-eye-slash'
		}else {
			pwd.type = "password";
			eye.className='fa fa-eye'
		}
}

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
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();
	const yzmValue = yzm.value.trim();
	
	if(emailValue === '') {
		setErrorFor(email, '邮箱不能为空');
		flag=false
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, '邮箱格式不正常');
		flag=false
	} else {
		setSuccessFor(email);
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
	if(flag===true){
		findPassWordBackPost()
	}
}

function checkInputsVerificationCode() {
	// trim to remove the whitespaces
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();
	
	if(emailValue === '') {
		setErrorFor(email, '邮箱不能为空');
		flag=false
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, '邮箱格式不正常');
		flag=false
	} else {
		setSuccessFor(email);
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
	if(flag===true){
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
function findPassWordBackPost(){
	$.load('操作进行中……')
	$.ajax({
		url:'/findpassword',
		dataType:'json',
		type:'POST',
		data:{
			pass:$('#password').val(),
			email:$('#email').val(),
			flagyzm:'False',
			yzm:$('#yzm').val(),
			pass2:$('#password2').val()
		},
		success:
		function(results){
			$.loaded();
			if (results.success==200){
				$.alert('重置成功！前往登陆'+results.zcjg,function(){
				window.location.href="/login";
			})
			}
			else if(results.success==404){
				$.confirm('重置失败！'+results.zcjg,function(e){
					e||window.location.replace("/register")
				}).cancel('前往').ok('取消')
			}
			else if(results.success==500){
				$.alert('重置失败！'+results.zcjg)
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
		url:'/findpassword',
		dataType:'json',
		type:'POST',
		data:{
			id:$('#username').val(),
			pass:$('#password').val(),
			email:$('#email').val(),
			flagyzm:'True',
			pass2:$('#password2').val()
		},
		success:
		function(results){
			$.loaded();
			if (results.success==200){
				$.alert('获取验证码成功！'+results.yzmjg)
			}
			else{
				$.confirm('获取验证码失败！'+results.zcjg,function(e){
					e||window.location.replace("/register")
				}).cancel('前往').ok('取消')
			}
		},
		error:
		function(err){
			$.loaded();
			$.alert('请求失败！'+err.status + '(' + err.statusText + ')') 
		}
	})
}
$(function() {
	var a = 0;
	$(".secreteyesk1").hide();
	$(".secreteyesk2").hide();
	$('.eyes1').click(function() {
		a += 1;
		if (a % 2 == 0) {
			$('.secreteyesk1').hide();
			$('.secreteyes1').show();
			$('.secret1').prop('type', 'password');
		} else if (a % 2 != 0) {
			$('.secreteyes1').hide();
			$('.secreteyesk1').show();
			$('.secret1').prop('type', 'text');
		}
	})
	a = 0;
	$('.eyes2').click(function() {
		a += 1;
		if (a % 2 == 0) {
			$('.secreteyesk2').hide();
			$('.secreteyes2').show();
			$('.secret2').prop('type', 'password');
		} else if (a % 2 != 0) {
			$('.secreteyes2').hide();
			$('.secreteyesk2').show();
			$('.secret2').prop('type', 'text');
		}
	})
})