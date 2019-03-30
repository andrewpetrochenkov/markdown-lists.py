#!/usr/bin/env python
# -*- coding: utf-8 -*-
import public
import re


def indent(depth,string):
    return re.sub('^','    '*depth, string ,flags=re.MULTILINE )

@public.add
def render(lists,depth=1):
    """return a string with markdown nested lists"""
    items = []
    for l in lists:
        if isinstance(l,(list,set,tuple)):
            string = render(l,depth+1)
            items.append(indent(depth,string))
        else:
            items.append("+   %s" % str(l))
    return "\n".join(items)
