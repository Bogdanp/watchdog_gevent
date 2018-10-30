# watchdog_gevent

[![Build Status](https://travis-ci.org/Bogdanp/watchdog_gevent.svg?branch=master)](https://travis-ci.org/Bogdanp/watchdog_gevent)
[![PyPI version](https://badge.fury.io/py/watchdog-gevent.svg)](https://badge.fury.io/py/watchdog-gevent)

**watchdog_gevent** is a [gevent]-based observer for [watchdog].


## Requirements

* [gevent] 1.1+
* [watchdog] 0.8+


## Setup

    pip install watchdog_gevent


## Usage

Just import and use its observer:

``` python
from watchdog_gevent import Observer
```

This will automatically import the best observer for the current
platform, preferring a [gevent]-based observer if gevent is installed
and the `threading` module has been monkeypatched.  This library
*only* works if the threading module has been monkeypatched.


## Limitations

The package only works if you use gevent to monkeypatch the threading
module.  Additionally, file and directory events are not emitted.


## License

watchdog_event is licensed under Apache 2.0.  Please see [license] for
licensing details.


[gevent]: http://www.gevent.org/
[watchdog]: http://pythonhosted.org/watchdog/
[pipenv]: https://docs.pipenv.org
[license]: https://github.com/Bogdanp/watchdog_gevent/blob/master/LICENSE
