var isIE = navigator.appVersion.indexOf("MSIE") != -1;

var preview, preview_img;

function show_preview(url) {
	preview.style.display = "block";
	preview_img.style.backgroundImage = "url("+this.href+")";
	return false;
}

function hide_preview() {
	preview.style.display = "none";
}

function fix_preview() {
	var e = document.documentElement ? document.documentElement : document.body;
	preview.style.top = e.scrollTop + "px";
	preview.style.height = e.clientHeight;
	preview.style.width  = e.clientWidth;
}

function nice_preview() {
	// attach
	var links = document.getElementsByTagName("A");
	for (var i in links) {
		if (/(.jpg|.png|.gif)$/.test(links[i])) {
			links[i].onclick = show_preview;
		}
	}
	// create divs
	preview = document.createElement("div");
	var bg  = document.createElement("div");
	var img = document.createElement("div");
	preview.id = "preview";
	bg.id      = "preview-bg";
	img.id     = "preview-img";
	hide_preview();
	preview.onclick = bg.onclick = img.onclick = hide_preview;
	preview.appendChild(bg);
	preview.appendChild(img);
	document.body.appendChild(preview);
	preview_img = img;
	if (isIE) {
		window.onscroll = fix_preview;
		fix_preview();
	}
}

var dir;
function fix_img() {
	if (this.currentStyle.width == 'auto' && this.currentStyle.height == 'auto') {
		this.style.width  = this.offsetWidth  + 'px';
		this.style.height = this.offsetHeight + 'px';
	}
	this.onload = null;
	this.style.filter = 'progid:DXImageTransform.Microsoft.AlphaImageLoader(src="'+this.src+'",sizingMethod="scale")';
	this.src = dir + "blank.gif";
}
function fix_png_alpha() {
	if (!/MSIE (5\.5|6\.)/.test(navigator.userAgent)) return; // only in ie 5.5 and 6
	dir = document.getElementsByTagName("SCRIPT")[0].src.replace(/[^\/]*$/,''); // dir for blank image
	var imgs = document.getElementsByTagName("IMG");
	for (var i in imgs) {
		var img = imgs[i];
		if ((/\.png$/i).test(img.src)) {
			img.onload = fix_img;
		}
	}
}

function init() {
	fix_png_alpha();
	nice_preview();
}
