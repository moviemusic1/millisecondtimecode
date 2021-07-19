/*
Copyright (C) 2021  lymnyx

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

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
