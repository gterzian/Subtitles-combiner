Pinyin -- Chinese Characters
============================
###subtitles combiner


####script to combine Pinyin and character subtitles

#####Download and run as example:


```
$ python combine.py 
  --title 'Crouching Tiger Hidden Dragon' 
  --files 'Crouching Tiger Hidden Dragon.Simplified.srt' 'Crouching_Tiger_Hidden_Dragon.Pinyin.srt' 
```

you can add as many filenames as you want, these will all be combined. 

by the way also an example of usign generators for creating processing pipelines. 
For more on this see: 

* [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/)
* [Pipes and filters architectures with Python generators](http://www.stylight.com/Numbers/pipes-and-filters-architectures-with-python-generators/)

Also make sure to check out recipe 4.13. Creating Data Processing Pipelines of [The Python Cookbook](http://shop.oreilly.com/product/0636920027072.do)