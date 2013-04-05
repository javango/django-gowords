==============
Go Words
==============

Go Words are slugs that are used to simplify urls for published links.

Example
======

Goword::

 - slug: google
 - url: http://www.google.com

http://example.com/go/google/ would result in the user being redirected to www.google.com

Usage
======

Add to INSTALLED_APPS in settings.py::
	
	'gowords',
	
Install database using south::
    
    ./manage.py migrate gowords
    
Install database without South::
    
    ./manage.py syncdb
    
project urls.py::

    (r'^go/', include('gowords.urls')),
    
TODO
======

Make saving a goword check existing urls to verify there is not a conflict.  
This would allow gowords to be mapped to the root.  ie as the last of url pattern (r'^', include('gowords.urls'))

Add url and view to display a search page when no goword is specified (?go=goword).  This would also allow sites
to put a 'keyword' box in their navigation to allow users to quickly jump to pages.
