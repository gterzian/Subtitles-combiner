Pinyin -- Chinese Characters
============================
###subtitles combiner


####script to combine Pinyin and character subtitles

#####Download and run as example:


```
$ python combine.py 
  --title 'Crouching Tiger Hidden Dragon' 
  --files 'CTHD.Simplified.srt' 'CTHD.Pinyin.srt' 
```

You can add as many filenames as you want, these will all be combined. 
The title argument is used for the name of the combined file.

Also an example of using generators for creating data processing pipelines. 

For more on this see: 

* [Coroutines and Generators, explained by David Beazley](http://www.dabeaz.com/coroutines/Coroutines.pdf)

Also make sure to check out recipe 4.13. Creating Data Processing Pipelines of the excellent [Python Cookbook](http://shop.oreilly.com/product/0636920027072.do)