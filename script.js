document.querySelector('.time').innerHTML = (Date.now() / 100);

setInterval(function() {document.querySelector('.time').innerHTML = (Date.now() / 100);},10);

document.querySelector('.copybtn').addEventListener('click', function() {
	document.querySelector('#copyinput').value = Date.now();
});

document.querySelector('.timebtn').addEventListener('click', function() {
	timecode = new Date(Number(document.querySelector('.timeinput').value));
	document.querySelector('#converttimeh4').innerHTML = timecode.toUTCString();
});
