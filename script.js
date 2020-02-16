document.querySelector('.time').innerHTML = Date.now();
setInterval(function() {document.querySelector('.time').innerHTML = Date.now();},10);
document.querySelector('.copybtn').addEventListener('click', function() {
document.querySelector('#copyinput').value = Date.now();
});
