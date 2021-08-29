# Plover RTF/CRE transcript support

> very WIP and idea-based at the moment

Add in support for creating job files within plover that are written out in RTF/CRE format, joining the steno and text used for writing. 

## ideas 

it's really easy to do in a basic sense. 
fill in loads of information at the start.
write the text as is, but before every entry add in a `cxs` field showing the steno that was used. 
and timestamp it (condensed) with `cxt` fields. 
for example:

`{\*\cxt 12:00:00}{\*\cxs H-L}hello {\*\cxt 01}{\*\cxt THR}there `

you can also add in plover specific stuff with maybe a `cxpl` string, for __C__R E__X__tensions __Pl__over ...

potential additional fields:
- when an orthograpy field was used, indicating that a specific dictionary entry does not exist : `cxplorth`
- when a stroke was undone (stenograph has a specific extension for this) : `cxplundo`
- when modifier strokes were sent, hidden in text but still shown for completeness : `cxplmodi`
- plover specific formatting, for stuff like attachment or newlines when not supported in CRE/RTF : `crplform`
