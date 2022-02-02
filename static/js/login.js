$(document).ready(function(){
    $('#btn1').on('click',function(){
        $.load('登陆中……')
        $.ajax({
            url:'/login',
            dataType:'json',
            type:'POST',
            data:{
                zh:$('#zh').val(),
                pass:$('#pass').val()
            },
        success:
        function(results){
            var flag=true
            if (results.success==404){
                $.loaded();
                $.confirm('登陆失败！'+results.dljg,function(e){
                    e||window.location.replace("/register")
                }).cancel('前往').ok('取消')
            }
            else if(results.success==500){
                $.loaded();
                $.alert(results.dljg)
            }
            else if(results.success==406){
                $.loaded();
                $.alert('登陆失败！'+results.dljg)
            }
            else if(results.success==200){
                $.loaded();
                document.cookie="weiyiyzm="+results.weiyiyzm+"; expires="+results.time;
                document.cookie="account="+results.account+"; expires="+results.time;
                $.alert('登陆成功！',function(){
                    window.location.replace("/")
                })
            }
        },
        error:
        function(err){
            $.loaded();
            $.alert('请求失败！'+err.status + '(' + err.statusText + ')') 
        }
        })
    })
})