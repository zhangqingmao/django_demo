/*网页加载完执行定时器,每1秒执行一次,i+1
	
	当鼠标以上时清除定时器
	当鼠标移出执行定时器
	此时的定时器为i+1;
	如果i==4 i=0
*/


/*轮播图*/
var i = 1;
var timer;
window.onload = function(){
	timer = window.setInterval("start2()",2000);
}
function start2(){
	if(i==6){
		i=0;
	}
	i++;
	var imgObj = document.getElementById("img01");
	imgObj.src = "../../static/images/index/1."+i+".jpg";
}


/*鼠标移上显示隐藏菜单*/
function xianshi(){
	search_hot.style.display = "block";
}
function out(){
	search_hot.style.display = "none"
}
/*鼠标移上显示隐藏按钮*/
function xianshi1(){
	prev.style.display="block";
	next.style.display="block";
	clearInterval(timer);
}
function out1(){
	prev.style.display="none"
	next.style.display="none"
	timer = setInterval("start2()",2000)
}

/*下一张图片*/
function next1() {
	i++;
	if(i==7){
		i = 1;
	}
	var imgObj = document.getElementById("img01");
	imgObj.src = "../images/index/1."+i+".jpg";
}
/*上一张图片*/
function prev1() {
	
	if(i==1){
		i = 7;
	}
	i--;
	var imgObj = document.getElementById("img01");
	imgObj.src = "../images/index/1."+i+".jpg";
}
/*有格调切换列表*/
function quanbu() {
	ygd.style.visibility="visible"
	ygd_1.style.visibility="hidden"
	ygd_2.style.visibility="hidden"
	ygd_3.style.visibility="hidden"
	ygd_4.style.visibility="hidden"
}
function yuehui() {
	ygd_1.style.visibility="visible"
	ygd.style.visibility="hidden"
	ygd_2.style.visibility="hidden"
	ygd_3.style.visibility="hidden"
	ygd_4.style.visibility="hidden"
}
function spa() {
	ygd_2.style.visibility="visible"
	ygd_1.style.visibility="hidden"
	ygd.style.visibility="hidden"
	ygd_3.style.visibility="hidden"
	ygd_4.style.visibility="hidden"
}
function yanchu() {
	ygd_3.style.visibility="visible"
	ygd_1.style.visibility="hidden"
	ygd_2.style.visibility="hidden"
	ygd.style.visibility="hidden"
	ygd_4.style.visibility="hidden"
}
function chuyou() {
	ygd_4.style.visibility="visible"
	ygd_1.style.visibility="hidden"
	ygd_2.style.visibility="hidden"
	ygd_3.style.visibility="hidden"
	ygd.style.visibility="hidden"
}

// 很优惠切换菜单
function quanbu1() {
	hyh_1.style.visibility="visible"
	hyh_2.style.visibility="hidden"
	hyh_3.style.visibility="hidden"
	hyh_4.style.visibility="hidden"
}
function meishi() {
	hyh_1.style.visibility="hidden"
	hyh_2.style.visibility="visible"
	hyh_3.style.visibility="hidden"
	hyh_4.style.visibility="hidden"
}
function dianying() {
	hyh_2.style.visibility="hidden"
	hyh_1.style.visibility="hidden"
	hyh_3.style.visibility="visible"
	hyh_4.style.visibility="hidden"
}
function yule() {
	hyh_3.style.visibility="hidden"
	hyh_1.style.visibility="hidden"
	hyh_2.style.visibility="hidden"
	hyh_4.style.visibility="visible"
}
/*猫眼电影箭头*/
function xianshi2(){
	prev2.style.display="block";
	next2.style.display="block";
}
function out2(){
	prev2.style.display="none"
	next2.style.display="none"
}
function prev3() {
	mydy_1.style.display="block"
	mydy_2.style.display="none"
}
function next3() {
	mydy_1.style.display="none"
	mydy_2.style.display="block"
}