document.querySelector('.time').innerHTML = (Date.now() / 100);

setInterval(() => {
	if(!(document.activeElement === document.querySelector('.time'))) {
		document.querySelector('.time').value = (Date.now() / 100);
		timecode = new Date(Number(document.querySelector('.time').value) * 100);
		document.querySelector('#converttimeh4').innerHTML = timecode.toUTCString();
	}
}, 20);

document.querySelector('.time').addEventListener('keydown', e => {
	if(e.keyCode == 13) {
		timecode = new Date(Number(document.querySelector('.time').value) * 100);
		document.querySelector('#converttimeh4').innerHTML = timecode.toUTCString();
	}
});
