import urllib2
import os

def get(upstream, downstream=None, proxy=None):
    if downstream and os.path.exists(downstream):
        return downstream
    else:
        return upstream
