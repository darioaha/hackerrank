
### Regex excercises

* Exercise 1: Matching Characters
```
Match	abcdefg	
Match	abcde
Match	abc
```

```
\w{3,7}
```

* Exercise 1½: Matching Digits
```
Match	abc123xyz	To be completed
Match	define "123"	To be completed
Match	var g = 123;
```

```
123
```


* Exercise 2: Matching With Wildcards
```
Match	cat.
Match	896.
Match	?=+.
Skip	abc1

```

```
(\w{3}|\?=\+)\.
```

* Exercise 3: Matching Characters

```
Match	can	
Match	man	
Match	fan	
Skip	dan	
Skip	ran	
Skip	pan
```

```
[cmf]an
```

* Exercise 4: Excluding specific characters (^)

```
Match	hog	Success
Match	dog	Success
Skip	bog
```

```
[^b]og
```


* Exercise 5: Character ranges ([a-b])
```
Match	Ana	To be completed
Match	Bob	To be completed
Match	Cpc	To be completed
Skip	aax	To be completed
Skip	bby	To be completed
Skip	ccz
```

```
[A-C]\w{2}
```

* Exercise 6: Catching some zzz's ({})
```
Match	wazzzzzup	To be completed
Match	wazzzup	To be completed
Skip	wazup
```

```
waz{3,5}up
```

* Exercise 7: Matching Repeated Characters (kleene => `+*`)

```
Match	aaaabcc	To be completed
Match	aabbbbc	To be completed
Match	aacc	To be completed
Skip	a	To be completed

```

```
a+ab*c*
```

* Exercise 8: Matching Optional Characters (?)
```
Match	1 file found?	To be completed
Match	2 files found?	To be completed
Match	24 files found?	To be completed
Skip	No files found.
```

```
\d* files? found\?
```

* Exercise 9: Matching Whitespaces (\s)
```
Match	1.   abc	To be completed
Match	2.	abc	To be completed
Match	3.           abc	To be completed
Skip	4.abc
```

```
[1-3]\.\s*abc
\d\.\s+abc
# el segundo es mas correcto porque obliga agregar al menos un espacio
```

* Exercise 10: Matching Lines (^ $)
```
Match	Mission: successful
Skip	Last Mission: unsuccessful
Skip	Next Mission: successful upon capture of target
```

```
^Mission: successful$

```

* Exercise 11: Matching Groups (Capturing "()")

```
Capture	file_record_transcript.pdf	file_record_transcript	To be completed
Capture	file_07241999.pdf	file_07241999	To be completed
Skip	testfile_fake.pdf.tmp

```

```
^(\w+)\.pdf$

```

* Exercise 12: Matching Nested Groups ("()")
```
						Capture
Capture	Jan 1987		"Jan 1987" and "1987"
Capture	May 1969		"May 1969" and "1969"
Capture	Aug 2011		"Aug 2011" and "2011"
```

```
^(\w+\s(\d{4}))$
```

* Exercise 13: Matching Nested Groups (capture "()")
```
						Capture
Capture	1280x720		1280 720
Capture	1920x1600		1920 1600
Capture	1024x768		1024 768
```

```
(\d{4})x(\d*)
```

* Exercise 14: Matching Conditional Text (or |)
```
Match	I love cats
Match	I love dogs
Skip	I love logs
Skip	I love cogs
```

```
I love (dogs|cats)
```

* Exercise 15: Matching Other Special Characters
```
Match	The quick brown fox jumps over the lazy dog.	To be completed
Match	There were 614 instances of students getting 90.0% or above.	To be completed
Match	The FCC had to censor the network for saying &$#*@!.
```
```
.*
```


-------------------------Aditional

* Exercise 1: Matching Numbers
```
Match	3.14529
Match	-255.34
Match	128
Match	1.9e10
Match	123,340.00
Skip	720p
```

```
^-?\d*.*\d*[^a-z]$
^-?\d+(,\d+)*(\.\d+(e\d+)?)?$
```

* Exercise 2: Matching Phone Numbers
```
Capture	415-555-1234	415
Capture	650-555-2345	650
Capture	(416)555-3456	416
Capture	202 555 4567	202
Capture	4035555678	403
Capture	1 416 555 9292	416
```

```
(\d{3})
```


* Exercise 3: Matching Emails
Extract names
```
Capture	tom@hogwarts.com	tom
Capture	tom.riddle@hogwarts.com	tom.riddle
Capture	tom.riddle+regexone@hogwarts.com	tom.riddle
Capture	tom@hogwarts.eu.com	tom
Capture	potter@hogwarts.com	potter
Capture	harry@hogwarts.com	harry
Capture	hermione+regexone@hogwarts.com	hermione
```

```
^([\w\.]*)
```


* Exercise 4: Capturing HTML Tags
```
Capture	<a>This is a link</a>					a
Capture	<a href='https://regexone.com'>Link</a>	a
Capture	<div class='test_style'>Test</div>		div
Capture	<div>Hello <span>world</span></div>		div
```

```
<(\w*)
```

!! Capture tag contents `>([\w\s]*)<`

* Exercise 5: Capturing Filename Data
```
Skip	.bash_profile
Skip	workspace.doc
Capture	img0912.jpg	img0912 	jpg
Capture	updated_img0912.png		updated_img0912 png
Skip	documentation.html
Capture	favicon.gif	favicon 	gif
Skip	img0912.jpg.tmp
Skip	access.lock
```

```
^(\w*)\.(jpg|gif|png)$
```
$ symbol is used to exception "img0912.jpg.tmp"


* Exercise 6: Trimming whitespace from start and end of line
```
								Capture
    The quick brown fox...		The quick brown fox...
jumps over the lazy dog.		jumps over the lazy dog.
```

```
\s*([\w\s\.]*)
```

* Exercise 7: Extracting Data From Log Entries
# https://regexone.com/problem/extracting_log_data?

```
(\w+)\((\w+\.java):(\d+)\)
```


* Exercise 8: Extracting Data From URLs
# https://regexone.com/problem/extracting_url_data?

```
(\w+)://([\w\-\.]+):?(\d+)?
```

