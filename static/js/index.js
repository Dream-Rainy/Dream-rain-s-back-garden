var flagspecialSkin=[];
var rmc=[];
var srmc=[];
var ssrmc=[];
var spmc=[];
var specialSkinmc=[];
var flagupsp=false;
var flagupssr=false;
var flagupwsl=false;
var flagupspecial=false;
var flagpiece=false;
var ssrResultsspecialSkin='';
var resultspecialSkin='';
var temp='';
var glupss='';
var ssrinfo=[];
var spinfo=[];
var flagspecialup=false;
$(document).ready(function(){
  $.load();
  $.ajax({
    type: "get",
    url: "/chouka",
    dataType:"json",
    success: function (data) {
      flagspecialSkin=data.flagspecialSkin;
      console.log(flagspecialSkin);
      if(data.flagupsp==true){
        flagupsp=true;
      }else if(data.flagupssr==true){
        flagupssr=true;
      }else{
        flagupspecial=true;
      };
      flagpiece=data.flagpiece;
      rmc=data.rmc;
      console.log(rmc);
      specialSkinmc=data.specialSkinmc;
      console.log(specialSkinmc);
      spmc=data.spmc;
      console.log(spmc);
      srmc=data.srmc;
      console.log(srmc);
      ssrmc=data.ssrmc;
      console.log(ssrmc);
      if ($('input[name="upss"]:checked').val()=="无"){
        flagspecialup=true;
      }
      //获取未收录信息
      var ssrinfotemp=getCookie("ssrinfo");
      var spinfotemp=getCookie("spinfo");
      var flagssinfo=getCookie("flagssinfo")
      var x=0
      console.log(ssrinfotemp);
      console.log(spinfotemp);
      if (flagssinfo!='True'){
        $.alert("请先设置式神信息再使用抽卡模拟功能！（本信息15天重置一次）",function(){
          window.location.href="/#ssinfo"
          sleep(1000).then(()=>{
            $.loaded();
            $.tips('获取信息完成');
          });
        })
      }else{
        for (let i in ssrinfotemp) {
          if (ssrinfotemp[i]=="1"){
            ssrinfo[x]=ssrmc[x]
            x++
          };
        };
        x=0
        for (let i in spinfotemp) {
          if (spinfotemp[i]=="1"){
            spinfo[x]=spmc[x]
            x++
          };
        };
        console.log(spinfo);
        console.log(ssrinfo);
        setTimeout(() => console.log("Wait......"), 2000)
        $.loaded();
        $.tips('获取信息完成');
      }
    },
    error: function (err) {
      setTimeout(() => console.log("Wait......"), 2000)
      $.loaded();
      $.alert('请求式神信息失败！'+err.status + '(' + err.statusText + ')') 
    }
  });
    $('#btn1').on('click',function(){
      $('#spResults').text("");
      $('#ssrResults').text("");
      $('#srResults').text("");
      $('#result').text("");
      $('#ssupFrequency').text("概率up次数：0/3");
      $.load();
      glupss=$('input[name="upss"]:checked').val();
      var piecetemp=0;
      var baodi=0;
      var piecegl=0;
      var gl=0;
      var result=[];
      var spResults=[];
      var ssrResults=[];
      var srResults=[];
      var ssupFrequency=0;
      var dqssupFrequency=0;
      var spFrequency=0;
      var ssrFrequency=0;
      var zcs=$('#zcs').val();
      var flag25=$("#flag25").is(":checked");
      var flagqtj=$("#flagqtj").is(":checked");
      flagupwsl1=flagupwsl;
      for (var i=1;i<=zcs;i++){
        var x=Math.random();//总概率生成
        if(flagpiece){
          piecegl=Math.random();
          baodi++
          if(piecegl<=0.01){
            piecetemp++;
            dqssupFrequency++;
            baodi=0;
          };
        };
        if(flagpiece==false){
          var cz=probabilityGrow(i,flagqtj);
        };
        if (ssupFrequency==3&&flag25){//三次up用尽
          flag25=false;
        };
        if (i==600&&flagqtj&&flagspecialup==false&&flagupspecial==false&&flagpiece==false){//600保底判定
          dqssupFrequency++;
          flagspecialup=true;
          flagqtj=true;
          if (flagupsp==true){
            spFrequency++;
            spResults.push(glupss+'['+String(i)+']');
          }else{
            ssrFrequency++;
            ssrResults.push(glupss+'['+String(i)+']');
          };
          result.push('恭喜抽出当期概率up式神'+glupss);
        }else if(flag25==true&&flagspecialup==false){//双up
          if (x<=(0.0125*2.5)){//SSR/SP式神
            if (flagupwsl&&flagupwsl1){
              flagupwsl1=false;
              ssupFrequency++;
              var temp1=getArrDifference(ssrinfo,ssrmc);
              var temp2=getArrDifference(spinfo,spmc);
              temp1.concat(temp2);
              parseInt(Math.random()*(temp1.length),10);
              gl=Math.floor(Math.random()*(temp1.length));
              result.push('恭喜获得未收录式神，是'+temp1[gl]);
              for (const value of ssrmc) {
                if (value==temp1[gl]){
                  ssrResults.push(temp1[gl]+'['+String(i)+']'+'(未收录)');
                };
              };
              for (const value of spmc) {
                if (value==temp1[gl]){
                  spResults.push(temp1[gl]+'['+String(i)+']'+'(未收录)');
                };
              };
            }else{
              ssupFrequency++;
              var ssupgl=Math.random();
              if (ssupgl<=cz&&flagupspecial==false&&flagpiece==false){
                flagspecialup=true;
                dqssupFrequency++;
                if (flagupsp==true){
                  spFrequency++;
                  spResults.push(glupss+'['+String(i)+']');
                }else if(flagupssr==true){
                  ssrFrequency++;
                  ssrResults.push(glupss+'['+String(i)+']');
                };
                result.push('恭喜抽出当期概率up式神'+glupss);
              }else{
                cgl=Math.random();
                if (cgl<=0.2){
                  parseInt(Math.random()*(spmc.length),10);
                  gl=Math.floor(Math.random()*(spmc.length));
                  while (spmc[gl]==glupss&&flagupsp==true){
                    parseInt(Math.random()*(spmc.length),10);
                    gl=Math.floor(Math.random()*(spmc.length));
                  };
                  spFrequency++;
                  spResults.push(spmc[gl]+'['+String(i)+']');
                  result.push('恭喜抽出SP式神，是'+spmc[gl]);
                  if (flagupspecial&&special(cz)&&flagpiece==false){
                    result.push('恭喜抽出当期概率up物品'+glupss);
                    spResults.push(glupss+'['+String(i)+']');
                    dqssupFrequency++;
                    flagspecialup=true;
                    flagqtj=true;
                  };
                };
                if (cgl>0.2){
                  parseInt(Math.random()*(ssrmc.length),10);
                  gl=Math.floor(Math.random()*(ssrmc.length));
                  while (ssrmc[gl]==glupss&&flagupssr==true){
                    parseInt(Math.random()*(ssrmc.length),10);
                    gl=Math.floor(Math.random()*(ssrmc.length));
                  };
                  ssrFrequency++;
                  specialSkin(gl,i);
                  result.push(resultspecialSkin);
                  ssrResults.push(ssrResultsspecialSkin);
                  if (flagupspecial&&special(cz)&&flagpiece==false){
                    result.push('恭喜抽出当期概率up物品'+glupss);
                    ssrResults.push(glupss+'['+String(i)+']');
                    dqssupFrequency++;
                    flagspecialup=true;
                    flagqtj=true;
                  };
                };
              };
            };
          }else if(0.0125*2.5<x&&x<=0.2/0.9875*0.96875){//SR式神
            parseInt(Math.random()*(srmc.length),10);
            gl=Math.floor(Math.random()*(srmc.length));
            srResults.push(srmc[gl]+'['+String(i)+']');
            result.push('恭喜抽出SR式神，是'+srmc[gl]);
          }else{//R式神
            parseInt(Math.random()*(rmc.length),10);
            gl=Math.floor(Math.random()*(rmc.length));
            result.push('恭喜抽出R式神，是'+rmc[gl]);
          };
        }else if(flag25==true&&flagspecialup||flag25==true&&flagspecialup){ //单up
          if(flagspecialup==false){//只有式神定向up
            if(x<=0.0125){
              ssupgl=Math.random();
              if(ssupgl<=cz&&flagupspecial==false&&flagpiece==false){//出了当期概率up式神
                flagspecialup=true;
                dqssupFrequency++;
                if(flagupsp==true){
                  spFrequency++;
                  spResults.push(glupss+'['+String(i)+']');
                }else{
                  ssrFrequency++;
                  ssrResults.push(glupss+'['+String(i)+']');
                };
                result.push('恭喜抽出当期概率up式神'+glupss);
              }else{//没出当期概率up式神
                cgl=Math.random();
                if(cgl<=0.2){
                  spFrequency++;
                  parseInt(Math.random()*(spmc.length),10);
                  gl=Math.floor(Math.random()*(spmc.length));
                  while(spmc[gl]==glupss&&flagupsp==true){
                    parseInt(Math.random()*(spmc.length),10);
                    gl=Math.floor(Math.random()*(spmc.length));
                  }
                  spResults.push(spmc[gl]+'['+String(i)+']');
                  result.push('恭喜抽出SP式神，是'+spmc[gl]);
                  if (flagupspecial&&special(cz)&&flagpiece==false){
                    result.push('恭喜抽出当期概率up物品'+glupss);
                    spResults.push(glupss+'['+String(i)+']');
                    dqssupFrequency++;
                    flagspecialup=true;
                    flagqtj=true;
                  };
                }else if(cgl>0.2){
                  ssrFrequency++;
                  parseInt(Math.random()*(ssrmc.length),10);
                  gl=Math.floor(Math.random()*(ssrmc.length));
                  while(ssrmc[gl]==glupss&&flagupsp==true){
                  parseInt(Math.random()*(ssrmc.length),10);
                  gl=Math.floor(Math.random()*(ssrmc.length));
                  };
                  ssrResults.push(ssrmc[gl]+'['+String(i)+']');
                  result.push('恭喜抽出SSR式神，是'+ssrmc[gl]);
                  if (flagupspecial&&special(cz)&&flagpiece==false){
                    result.push('恭喜抽出当期概率up物品'+glupss);
                    ssrResults.push(glupss+'['+String(i)+']');
                    dqssupFrequency++;
                    flagspecialup=true;
                    flagqtj=true;
                  };
                };
              };
            }else if(0.0125<x&&x<=0.2){//SR式神
              parseInt(Math.random()*(srmc.length),10);
              gl=Math.floor(Math.random()*(srmc.length));
              srResults.push(srmc[gl]+'['+String(i)+']');
              result.push('恭喜抽出SR式神，是'+srmc[gl]);
            }else{//R式神
              parseInt(Math.random()*(rmc.length),10);
              gl=Math.floor(Math.random()*(rmc.length));
              result.push('恭喜抽出R式神，是'+rmc[gl]);
            };
          }else{//只有三次概率up无式神定向up
            if(x<=0.0125*2.5){ //SSR/SP式神
              ssupFrequency++;
              cgl=Math.random();
              if (cgl<=0.2){
                  spFrequency++;
                  parseInt(Math.random()*(spmc.length),10);
                  gl=Math.floor(Math.random()*(spmc.length));
                  spResults.push(spmc[gl]+'['+String(i)+']');
                  result.push('恭喜抽出SP式神，是'+spmc[gl]);
              }else{
                  ssrFrequency++;
                  parseInt(Math.random()*(ssrmc.length),10);
                  gl=Math.floor(Math.random()*(ssrmc.length));
                  specialSkin(gl,i);
                  result.push(resultspecialSkin);
                  ssrResults.push(ssrResultsspecialSkin);
              };
            }else if(0.0125*2.5<x&&x<=0.2/0.9875*0.96875){//SR式神
              parseInt(Math.random()*(srmc.length),10);
              gl=Math.floor(Math.random()*(srmc.length));
              srResults.push(srmc[gl]+'['+String(i)+']');
              result.push('恭喜抽出SR式神，是'+srmc[gl]);
            }else{//R式神
              parseInt(Math.random()*(rmc.length),10);
              gl=Math.floor(Math.random()*(rmc.length));
              result.push('恭喜抽出R式神，是'+rmc[gl]);
            };
          };
        }else{//没有任何概率up
          if (x<=0.0025){//SP式神
            parseInt(Math.random()*(spmc.length),10);
            gl=Math.floor(Math.random()*(spmc.length));
            spFrequency++;
            if (spmc[gl]==glupss){
              dqssupFrequency++;
              spResults.push(glupss+'['+String(i)+']');
              result.push('当期概率up式神'+glupss);
            }else{
              spResults.push(spmc[gl]+'['+String(i)+']');
              result.push('恭喜抽出SP式神，是'+spmc[gl]);
            };
          }else if(0.0025<x&&x<=0.01){//SSR式神
            ssrFrequency++;
            parseInt(Math.random()*(ssrmc.length),10);
            gl=Math.floor(Math.random()*(ssrmc.length));
            if (ssrmc[gl]==glupss){
              dqssupFrequency++;
              ssrResults.push(glupss+'['+String(i)+']');
              result.push('恭喜抽出当期概率up式神'+glupss);
            }else{
              specialSkin(gl,i);
              result.push(resultspecialSkin);
              ssrResults.push(ssrResultsspecialSkin);
            };
          }else if(0.01<x&&x<=0.2){//SR式神
            parseInt(Math.random()*(srmc.length),10);
            gl=Math.floor(Math.random()*(srmc.length));
            srResults.push(srmc[gl]+'['+String(i)+']');
            result.push('恭喜抽出SR式神，是'+srmc[gl]);
          }else{//R式神
            parseInt(Math.random()*(rmc.length),10);
            gl=Math.floor(Math.random()*(rmc.length));
            result.push('恭喜抽出R式神，是'+rmc[gl]);
          };
        };
        if(i==600&&flagqtj&&flagspecialup==false&&flagupspecial&&flagpiece==false){
          result.push('恭喜获得当期概率up物品'+glupss);
          flagspecialup=true;
          flagqtj=true;
          dqssupFrequency++;
          spResults.push(glupss+'['+String(i)+']');
        }
        if(baodi==40){
          piecetemp++;
          dqssupFrequency++;
          flagbaodi=false;
        }
        if(i%10==0){
          if(flagpiece){
            result.push("本次十连获得"+glupss+"的个数是："+piecetemp+"个");
            piecetemp=0;
          };
          result.push("—————————————————————————————————————");
        }
      }
      if(flagpiece&&zcs%10!=0){
        result.push("本次获得"+glupss+"的个数是："+piecetemp+"个");
      };
      for (const value of spResults) {
        $('#spResults').append(value+"<br>");
      };
      for (const value of ssrResults) {
        $('#ssrResults').append(value+"<br>");
      };
      for (const value of srResults) {
        $('#srResults').append(value+"<br>");
      };
      for (const value of result) {
        $('#result').append(value+"<br>")
      };
      $('#ssupFrequency').text("概率up次数："+ssupFrequency+"/3");
      $('#spFrequency').text("本次抽卡获得SP个数："+spFrequency);
      $('#ssrFrequency').text("本次抽卡获得SSR个数："+ssrFrequency);
      $('#dqssupFrequency').text("本次抽卡获得当期概率up式神（物品）的次数为："+dqssupFrequency);
      sleep(1000).then(()=>{
        $.loaded();
        $.tips('完成');
      });
    })
})
function probabilityGrow(x,flag){//计算概率up成长
  var cz=0
  if (flag){
    if (x<50){
      cz=0.15;
    }else if (x<100){
      cz=0.2;
    }else if (x<150){
      cz=0.25;
    }else if (x<200){
      cz=0.3;
    }else if (x<250){
      cz=0.35;
    }else if (x<300){
      cz=0.4;
    }else if (x<350){
      cz=0.45;
    }else if (x<400){
      cz=0.5;
    }else if (x<450){
      cz=0.6;
    }else if (x<500){
      cz=0.8;
    }else{
      cz=1;
    };
  }else{
    if (x<50){
      cz=0.04;
    }else if (x<100){
      cz=0.05;
    }else if (x<150){
      cz=0.06;
    }else if (x<200){
      cz=0.08;
    }else if (x<250){
      cz=0.1;
    }else if (x<300){
      cz=0.11;
    }else if (x<350){
      cz=0.12;
    }else if (x<400){
      cz=0.13;
    }else if (x<450){
      cz=0.14;
    }else if (x<500){
      cz=0.15;
    }else{
      cz=0.25;
    };
  };
return cz;
}
function specialSkin(gl1,i1){//sp皮肤结果输出
  if (specialSkinmc[gl1]=='无'){
    ssrResultsspecialSkin=ssrmc[gl1]+'['+String(i1)+']';
    resultspecialSkin='恭喜抽出SSR式神，是'+ssrmc[gl1];
  }else{
    if (specialSkinProbability()&&flagspecialSkin[gl1]=='true'){
      if (ssrmc[gl1]!='玉藻前'){
        ssrResultsspecialSkin=ssrmc[gl1]+'['+String(i1)+']'+specialSkinmc[gl1];
        resultspecialSkin='恭喜抽出SSR式神，是'+ssrmc[gl1]+',并获得其SP皮肤'+specialSkinmc[gl1];
        flagspecialSkin[gl1]='false';
    }else{
      if (flagspecialSkin[gl1]=='false'&&flagspecialSkin[flagspecialSkin.length-1]){
        ssrResultsspecialSkin=(ssrmc[gl1]+'['+String(i1)+']'+specialSkinmc[gl1]);
        resultspecialSkin=('恭喜抽出SSR式神，是'+ssrmc[gl1]+',并获得其SP皮肤'+specialSkinmc[specialSkinmc.length-1]);
        flagspecialSkin[flagspecialSkin.length-1]='false';
      };
    };
    }else{
      ssrResultsspecialSkin=ssrmc[gl1]+'['+String(i1)+']';
      resultspecialSkin='恭喜抽出SSR式神，是'+ssrmc[gl1];
      };
  };
};
function specialSkinProbability(){//sp皮肤概率输出
  if (Math.random()<0.1){
    return true;
  }else{
    return false;
  };
};
function getArrDifference(arr1, arr2) {//未收录判定
  return arr1.concat(arr2).filter(function(v, i, arr) {
      return arr.indexOf(v) === arr.lastIndexOf(v);
  });
};
function special(cz){//特殊物品获得输出
  var random=Math.random();
  if (cz>=random){
    return true;
  }else{
    return false;
  };
};
function getCookie(cname){//获取cookie
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i=0; i<ca.length; i++) 
  {
    var c = ca[i].trim();
    if (c.indexOf(name)==0) return c.substring(name.length,c.length);
  };
  return "";
};
//设置式神信息
var ssr = [];
var sp = [];
document.getElementById("ssmessagesubmit").addEventListener('click', e => {
  e.preventDefault();
  for (let i in ssrmc) {
    if (document.getElementById(ssrmc[i]).checked) {
      ssr[i]=1
    }else{
      ssr[i]=0
    };
  };
  for (let i in spmc) {
    if (document.getElementById(spmc[i]).checked) {
      sp[i]=1
    }else{
      sp[i]=0
    };
  };
console.log(ssr);
setCookie("ssrinfo",ssr,15);
setCookie("spinfo",sp,15);
setCookie("flagssinfo","True",15);
$.alert("提交成功，即将刷新页面");
sleep(1000).then(()=>{
  window.location.replace("/");
});
})
function setCookie(cname,cvalue,exdays){//设置cookie
  var d = new Date();
  d.setTime(d.getTime()+(exdays*24*60*60*1000));
  var expires = "expires="+d.toGMTString();
  document.cookie = cname+"="+cvalue+"; "+expires;
};
function time(){//设置时间
    var date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth()+1;
    var day = date.getDate();
    var week = date.getDay();
    week="星期"+"日一二三四五六".charAt(week);
    var hour =date.getHours();
    hour=hour<10?"0"+hour:hour;
    var minute =date.getMinutes();
    minute=minute<10?"0"+minute:minute;
    var second = date.getSeconds();
    second=second<10?"0"+second:second;
    var currentTime = year+"-"+month+"-"+day+"  "+week+"   "+hour+":"+minute+":"+second;
    document.getElementById("time").innerHTML=currentTime;
};
setInterval("time()",1000);
$("#button1").click(function(){
  $("#excel").fadeToggle("slow")
})
function sleep(ms) {
  return new Promise(resolve => 
      setTimeout(resolve, ms)
  )
};