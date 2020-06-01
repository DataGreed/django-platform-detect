=============
django-detect
=============

Installation
============

::

    pip install django-platform-detect


Usage
=====

::

    # ####### Device、OS #######
    # Windows
    request.windows
    # Linux
    request.linux
    # macOS/iPhone/iPad/iPod
    request.imac
    request.iphone
    request.ipad
    request.ipod
    # desktop
    request.desktop = request.Windows or request.Linux or request.iMac
    # iOS
    request.iOS = request.iPhone or request.iPad or request.iMac or request.iPod
    # Android and Version
    request.android
    request.android.version




Settings.py
===========

::
    # Add to `settings.MIDDLEWARE`
    MIDDLEWARE = (
        ...
        'detect.middleware.UserAgentDetectionMiddleware',
        ...
    )


Thanks
===========
Based on https://github.com/django-xxx/django-detect
