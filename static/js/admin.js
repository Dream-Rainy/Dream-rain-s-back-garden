document.getElementById("upload").addEventListener('click', e => {
    e.preventDefault();
    uploadnewssinfo()
})
function uploadnewssinfo(){
    $.load()
    $.ajax({
        url:'/admin',
        dataType:'json',
        type:'POST',
        data:{
            pj:$('#pj').val(),
            mc:$('#mc').val(),
            spflag:$('#spflag').val(),
            spmc1:$('#spmc1').val(),
            spmc2:$('#spmc2').val(),
            activityname:$('#activityname').val(),
            glupss:$('#glupss').val(),
            wslflag:$('#wslflag').val(),
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