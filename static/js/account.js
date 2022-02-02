const cookiesName = document.getElementById('cookiesName');
const cookiesValue = document.getElementById('cookiesValue');
const password = document.getElementById('Password');
const password2 = document.getElementById('RepeatPassword');
var flag=false;
var r = new Array();
var sr = new Array();
var ssr = new Array();
var sp = new Array();

document.getElementById("setcookies").addEventListener('click', e => {
    const cname=cookiesName.value.trim();
    const cvalue=cookiesValue.value.trim();
    e.preventDefault();
	setCookie(cname,cvalue,255);
    $.alert('添加成功！') 
});

document.getElementById("loginout").addEventListener('click',e => {
    e.preventDefault();
    setCookie("account","",-1);
    setCookie("weiyiyzm","",-1);
    $.alert('退出登陆成功！',function(){
        window.location.href="/";
    }) 
});

document.getElementById("updatepass").addEventListener('click', e => {
    e.preventDefault();
    updatepassCheck();
})

document.getElementById("ssmessagesubmit").addEventListener('click', e => {
    e.preventDefault();
    $("input[name='r']:checked").each(function(i){//把所有被选中的复选框的值存入数组
        r[i] =$(this).val();
    }); 
    $("input[name='sr']:checked").each(function(i){//把所有被选中的复选框的值存入数组
        sr[i] =$(this).val();
    }); 
    $("input[name='ssr']:checked").each(function(i){//把所有被选中的复选框的值存入数组
        ssr[i] =$(this).val();
    }); 
    $("input[name='sp']:checked").each(function(i){//把所有被选中的复选框的值存入数组
        sp[i] =$(this).val();
    }); 
	console.log(r);
    uploadssinfo()
})

function setCookie(cname,cvalue,exdays){
    var d = new Date();
    d.setTime(d.getTime()+(exdays*24*60*60*1000));
    var expires = "expires="+d.toGMTString();
    document.cookie = cname+"="+cvalue+"; "+expires;
}

function updatepassCheck(){
    const passwordValue = password.value.trim();
    const password2Value = password2.value.trim();
    if (passwordValue === ''){
        $.alert('密码不能为空！')
        flag=false
    }else {
        flag=true
    }

    if(password2Value === '') {
		$.alert('重复密码不能为空！');
		flag=false
	} else if(passwordValue !== password2Value) {
		$.alert('两次密码不一致！');
		flag=false
	} else{
		flag=true
	}

    if(flag==true){
		updatepass()
	}
}

function updatepass(){
    $.load('修改中……')
    $.ajax({
        url:'/account',
        dataType:'json',
        type:'POST',
        data:{
            pass:$('#Password').val(),
            flag:'True',
        },
        success:
        function(results){
            $.loaded();
            if (results.success==200){
                $.alert('修改成功！')
            }
            else{
                $.alert('修改失败！'+results.changeResult)
            }
        },
        error:
        function(err){
            $.loaded();
            $.alert('请求失败！'+err.status + '(' + err.statusText + ')') 
        }
    })
}
function uploadssinfo(){
    $.load('提交中……')
    $.ajax({
        url:'/account',
        dataType:'json',
        type:'POST',
        data:{
            rinfo:r,
            srinfo:sr,
            ssrinfo:ssr,
            spinfo:sp,
            flag:'false',
        },
        success:
        function(results){
            $.loaded();
            if (results.success==200){
                $.alert('提交成功！')
            }
            else{
                $.alert('提交失败！'+results.changeResult)
            }
        },
        error:
        function(err){
            $.loaded();
            $.alert('请求失败！'+err.status + '(' + err.statusText + ')') 
        }
    })
}
