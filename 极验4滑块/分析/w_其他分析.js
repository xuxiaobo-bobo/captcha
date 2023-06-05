// 以下作為參數傳入加密函數 -> 得到w
{
    "setLeft": 207,
    "track": [],
    "passtime": 1455,
    "userresponse": 207.77631683588265,
    "device_id": "5d25317d91fd2c612ee3c2ec316f90b0",
    "lot_number": "d767f48ef29543b08e8d69384ad2f1e1",
    "pow_msg": "1|0|md5|2023-04-20T12:56:47.567957+08:00|24f56dc13c40dc4a02fd0318567caef5|d767f48ef29543b08e8d69384ad2f1e1||1abb42a231843c26",
    "pow_sign": "f99996094ea43d26a071a7822e038c4e",
    "geetest": "captcha",
    "lang": "zh",
    "ep": "123",
    "ak9j": "281841656",  //這個鍵&值都會變
    "em": {
        "ph": 0,
        "cp": 0,
        "ek": "11",
        "wd": 1,
        "nt": 0,
        "si": 0,
        "sc": 0
    }
}

// 1. (空

// 2: setLeft
缺口x座標

// 3: passtime
完成滑動的時間 

// 4: userresponse
// a / t[$_GDFDR(1905)] + 2
// a == setLeft , t[$_GDFDR(1905)] == 1.0059466666666665
var _ = {
	"\u0073\u0065\u0074\u004c\u0065\u0066\u0074": a,
	"\u0074\u0072\u0061\u0063\u006b": c,
	"\u0070\u0061\u0073\u0073\u0074\u0069\u006d\u0065": s,
	"\u0075\u0073\u0065\u0072\u0072\u0065\u0073\u0070\u006f\u006e\u0073\u0065": a / t[$_GDFDR(1905)] + 2
};

// 5. device_id
可能只是對同一個網站來說是定值, "5d25317d91fd2c612ee3c2ec316f90b0" 
因此要根據不同網站進行修改
關鍵字："\u0064\u0065\u0076\u0069\u0063\u0065\u005f\u0069\u0064":

// 6. lot_number
由這個接口返回 -> https://gcaptcha4.geetest.com/load?callback

// 7. pow_msg
// g = d[$_BJJCC(648)]
v[$_BJJCC(22)])(p, f, l[$_BJJCC(650)], l[$_BJJCC(647)], l[$_BJJCC(642)], l[$_BJJCC(688)], $_BJJDO(15))
		  , g = d[$_BJJCC(648)]
		  , m = d[$_BJJCC(620)];
		a[$_BJJDO(467)][$_BJJCC(609)] = g,
		a[$_BJJDO(467)][$_BJJDO(695)] = m,
		a[$_BJJCC(467)][$_BJJCC(673)] && b[$_BJJDO(22)][$_BJJCC(336)]({
			"\u0074\u0079\u0070\u0065": $_BJJCC(683)

// d內就有pow_msg、pow_sign等參數
d = (0,v[$_BJJCC(22)])(p, f, l[$_BJJCC(650)], l[$_BJJCC(647)], l[$_BJJCC(642)], l[$_BJJCC(688)], $_BJJDO(15))

==> 
d = v['default'](p, f,l['hashfunc'],l['version'],l['bits'],l['datetime'],'')

// l = h[$_BJJDO(615)]  ==>  l = h['powDetail']
h 由這個接口返回 -> https://gcaptcha4.geetest.com/load?callback

// f = captchaId
initGeetest4({
		captchaId: "24f56dc13c40dc4a02fd0318567caef5",
		product: e.state.currentType,
		btnWidth: "100%",
		language: e.state.currentLang,
		riskType: e.state.currentRisktype
	},
// p = h["lotNumber"]


// 生成d的函數(v['default'])
function i(e, t, n, i, r, s, o) {
		var $_HIHJs = oTEDG.$_DX()[6][10];
		for (; $_HIHJs !== oTEDG.$_DX()[2][8]; ) {
			switch ($_HIHJs) {
			case oTEDG.$_DX()[4][10]:
				var a = r % 4
				  , u = parseInt(r / 4, 10)
				  , c = function g(e, t) {
					var $_CEECW = oTEDG.$_CO
					  , $_CEEBs = ['$_CEEF_'].concat($_CEECW)
					  , $_CEEDN = $_CEEBs[1];
					$_CEEBs.shift();
					var $_CEEEr = $_CEEBs[0];
					return new Array(t + 1)[$_CEEDN(171)](e);
				}($_CEDDn(162), u)
				  , _ = i + $_CEDDn(108) + r + $_CEDCU(108) + n + $_CEDDn(108) + s + $_CEDDn(108) + t + $_CEDCU(108) + e + $_CEDDn(108) + o + $_CEDCU(108);
				$_HIHJs = oTEDG.$_DX()[2][9];
				break;

// 8:　pow_sign　　與 pow_msg一同生成

// 9: "ak9j": "281841656" ( 生成這個鍵值都會變的東西
// 執行完 -> n[$_CBHIu(738)](e) 就有了
 u[$_CBHIu(133)])(e, {
	"\u0064\u0065\u0076\u0069\u0063\u0065\u005f\u0069\u0064": i[$_CBHHo(699)],
	"\u006c\u006f\u0074\u005f\u006e\u0075\u006d\u0062\u0065\u0072": i[$_CBHIu(461)],
	"\u0070\u006f\u0077\u005f\u006d\u0073\u0067": n[$_CBHHo(467)][$_CBHIu(609)],
	"\u0070\u006f\u0077\u005f\u0073\u0069\u0067\u006e": n[$_CBHIu(467)][$_CBHHo(695)]
}),
n[$_CBHIu(738)](e);

// 執行完_gct(n)後就有我要的值了
 if (_gct) {
	var n = {
		"\u0067\u0065\u0065\u0074\u0065\u0073\u0074": $_BJIDo(483),
		"\u006c\u0061\u006e\u0067": $_BJIDo(181),
		"\u0065\u0070": $_BJIDo(676)
	};
	_gct(n),
	(0,
	u[$_BJICs(133)])(t, n);
// 先固定試試