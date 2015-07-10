# Wordthing.

The idea behind this is to take various 'bad' word lists from writing guides and automatically process them against
something you've written.

# Usage

- Open textinput.py and replace "your story goes here" with your actual content.
- Look at wordlists.py, and change the various lists from True to False as you see fit. You can also clone the template
word list to create your own.
- run process.py, and in stdout you should get output like:

```
#0000| tag ) description
#0000| p ) Passive Word List
#0000| C ) Custom test word list, don't use this unless you know what you're doing.
#0000| T ) Showing vs Telling Words
#0000| n ) Words that can be safely be omitted
~0000|
~0001|
~0002|   It was well past the witching hour and a friend suggested we head to
#0002|      ^^^^                            ^^^^
#0002|      pT                               C
~0003| another bar. "It's a great joint, it's super chill" he says trying to
#0003|                                                 ^^^
#0003|                                                 C
~0004| convince me to brave the elements and have an adventure. A few more
#0004|                                   ^^^^^^^^^
#0004|                                   C   p
~0005| tries at random lies about this bar, I reluctantly agree to go even
#0005|                      ^^^^^^^^^^^
#0005|                      n     C
~0006| though it's freezing cold out and know it will most likely be filled
#0006|                          ^^^^^^^^        ^^^^^            ^^^
#0006|                          n   C           p                p
~0007| with annoying hipsters.
#0007|
#0007|
```

This isn't perfectly aligned, but you should get the idea of what needs fixing on a line.

# Warning

You can fix a line, but it must be kept as a single line. If you create new unmarked lines they won't be rejoined
properly

# To Do

- Probably lots.
- The alignment could be better and the tags below could be fixed better.
- Rejoin the content back into original format / paragraphs

# Also.
I do most of my writing on my ipad and just wanted this basic functionality. This is meant to be ran under pythonista on the ipad. I use Ulysses to edit text, then put it into this, then put it back into Ulysses to edit. Or, that's the theory. YMMV
