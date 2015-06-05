Indentation for Facebook
=======================

You probably want to know what this fuss is about; that's why you're here,
in the about page. Right?  
Well, this is about replacing your source code indentation with a special
character that doesn't get eaten up by Facebook. That means it's also about
pasting source code on Facebook. That's it.  
So, when should you use this instead of Pastebin, Gist, et cetera? Most of the
times you'll *want* and *need* to use Pastebin and Gist. But there are
times you want to post a tiny piece of code, only to show something - it can be
a doubt, or an answer to one. The problem arises when your code has indentation:
Facebook will strip them out. This is when this website comes into action.  
I recently discovered* a unicode character that doesn't get stripped out
by Facebook and is whitespace. I've been using this character ever since
to post small snippets without losing indentation.  
Since I wanted people to know about this, I decided to build this simple,
small site to present and automate the process of replacing space and tab
characters with this one special character, called
<a href="http://www.fileformat.info/info/unicode/char/3000/index.htm">Ideographic Space</a>.  
By the way, you don't really need to use the browser to achieve the
functionality provided by this site. I've made another option available: if you
send a request with an `Accept: text/plain`
header, the response will contain *only* the replaced text. No HTML,
no need to parse anything; just get it and use it. All you have to do is, define a
`content`, an `indent-char` and an `indent-level` in your `POST` request and
you're good to go.

Check it out <a href="http://fawers.pythonanywhere.com/">here</a>
