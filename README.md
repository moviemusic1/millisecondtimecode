# decitime

This tiny, lightweight project lets you copy the unix timestamp of the current moment, also converting a timestamp back to a date is possible too.


You can use this e.g. to still know later, when you were done with a project.

Currently, there is a [version right in/for your browser](https://lymnyx.github.io/decitime/) (written in JavaScript) and one for your terminal (written in Python).


### decitime-cli
`python3 decitime.py [(Null/get)/give x]`


Examples for getting the timestamp:

`python3 decitime.py`

`python3 decitime.py get`

Example for converting a timestamp back to a date:

`python3 decitime.py give 9466848000`


### plans for this project

- giving 'decitime-cli' its command (`decitime`) (workaround for the moment: using my project [pthdrp](https://github.com/lymnyx/pthdrp) for this)

- making web version responsive

### license

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).
