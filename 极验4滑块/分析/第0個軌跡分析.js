 //  t[$_GDEDU(1970)] = new XXX
 // 這裡總共會push兩個軌跡：
 // 0：[X,X,X] 按某算法生成的,也是我需要的
 // 1: [0,0,0] 固定的, 然後之間會有一些操作？變成奇怪的值 (經過軌跡的加密函數)
 t[$_GDEDU(1970)] = new l[($_GDEDU(22))]([Math[$_GDEDU(670)]((s - t[$_GDEDU(1976)]) / t[$_GDECK(1905)]), Math[$_GDEDU(670)]((r - t[$_GDECK(1940)]) / t[$_GDEDU(1905)]), 0])[$_GDECK(1915)]([0, 0, 0]),
	t[$_GDECK(460)] = t[$_GDECK(1951)],
	t[$_GDEDU(1981)][$_GDEDU(1909)](),
	t[$_GDECK(1995)] = {
		"\u0078": 0,
		"\u0079": 0
	},
	!0;
	
/*** 逐個分析 ***/

/*   1. s   */

// s , then 要跟i
var r, s, o = n($_GDEDU(1965) + i)[$_GDEDU(1975)](),

// i = t['options']['hash']
// 搵唔到,但dom元素中有呢個值,或許可以
// 吾知會唔會校驗呢個hash值,有待嘗試
, i = t[$_GDECK(467)][$_GDECK(657)];


/*   2. t[$_GDEDU(1976)]   */

// t[$_GDEDU(1976)] = t['$_BIGV']
t[$_GDEDU(1976)] = e[$_GDECK(1956)]()

// e[$_GDECK(1956)]是下面這個函數
// 簡單來說就是返回鼠標的ClientX ( 或許可以固定？可能是弱校驗？ )
"\u0024\u005f\u0044\u0047\u004b": function() {
	var $_EJCt = oTEDG.$_CO
	  , $_EJBh = ['$_EJFA'].concat($_EJCt)
	  , $_EJDe = $_EJBh[1];
	$_EJBh.shift();
	var $_EJEp = $_EJBh[0];
	var e = this[$_EJCt(191)]; // 返回鼠標的一些信息
	// o[$_EJDe(17)] = o['isNumber']  判斷是否數字
	if ((0,
	o[$_EJDe(17)])(e[$_EJDe(153)])) // e[$_EJDe(153)] = e['clientX']
		return e[$_EJCt(153)]; // 基本上一定會走這裡,後面不用看
	var t = e[$_EJDe(180)] && e[$_EJDe(180)][0];
	return t ? t[$_EJCt(153)] : -1;
}

// 3. 固定值：1.0059466666666665 == t[$_GDECK(1905)]


/* 4. r  */

// r = o[$_GDECK(664)] + t[$_GDEDU(467)][$_GDEDU(1848)]
// 3目運算應該必然走上面這個分支
return s = $_GDEDU(1901) === e[$_GDECK(110)][$_GDECK(110)][$_GDECK(253)] ? (r = a[$_GDECK(664)],
                    a[$_GDEDU(848)]) : (r = o[$_GDECK(664)] + t[$_GDEDU(467)][$_GDEDU(1848)],

// 先分析o是怎樣計算出來的
 var r, s, o = n($_GDEDU(1965) + i)[$_GDEDU(1975)](),
 
 
 // o 由 return this[$_FGDj(110)][$_FGDj(203)]()
 // this[$_FGDj(110)]返回驗證碼背景圖片所在的div元素
 // $_FGDj(203) = 'getBoundingClientRect' 
 // 用來獲取頁面中某個元素的左、上、右、下分別相對瀏覽器視窗的位置，
 // 返回的是一個矩形對象，包括四個屬性，分別是left 、top、right、bottom。
 // 分別表示元素各邊與頁面上邊和左邊的距離。
  "\u0024\u005f\u0046\u0041\u0064": function() {
                    var $_FGCg = oTEDG.$_CO
                      , $_FGBG = ['$_FGFr'].concat($_FGCg)
                      , $_FGDj = $_FGBG[1];
                    $_FGBG.shift();
                    var $_FGEI = $_FGBG[0];
                    return this[$_FGDj(110)][$_FGDj(203)]();
                }
// o返回的東西大致如下：
// 應該可以直接固定
{
    "x": 890.0125122070312,
    "y": -39.75625228881836,
    "width": 300.375,
    "height": 200.35000610351562,
    "top": -39.75625228881836,
    "right": 1190.3875122070312,
    "bottom": 160.59375381469727,
    "left": 890.0125122070312
}

//再分析t
// 目標：t[$_GDEDU(467)][$_GDEDU(1848)] =>  t['options']['ypos']
// 由https://gcaptcha4.geetest.com/load?callback=geetest_XXX 這個接口返回


/* 5. t[$_GDECK(1940)] */
t[$_GDECK(1940)] = e[$_GDEDU(1902)]();

// e[$_GDEDU(1902)]是下面這個函數
// 返回ClientY
"\u0024\u005f\u0044\u0048\u0049": function() {
                    var $_EJHG = oTEDG.$_CO
                      , $_EJGk = ['$_FAAJ'].concat($_EJHG)
                      , $_EJIq = $_EJGk[1];
                    $_EJGk.shift();
                    var $_EJJg = $_EJGk[0];
                    var e = this[$_EJHG(191)];
                    if ((0,
                    o[$_EJIq(17)])(e[$_EJHG(150)]))
                        return e[$_EJIq(150)];
                    var t = e[$_EJHG(180)] && e[$_EJIq(180)][0];
                    return t ? t[$_EJHG(150)] : -1;
                },

// 6.  1.0059466666666665 == t[$_GDEDU(1905)]