# tw-wikitags-hook
_on-add or on-mod, :tag-one:tag-two: format, in task description, generates +tag-one +tag-two_

Vimwiki, *ledger and several other projects, use a tag format that looks like :tag1:tag2:. 
There has been some discussion and a PoC implementation (https://gist.github.com/wbsch/164757889ba4554df359) of "in-line" tags.  Entered as description text, generating regular (non-in-line) +tags.

In this variation the P.O.C. hook script, the :tag:format: is @different, and the surrounding colons are not removed after tag is generated. 

(more long-winded description of intent can be found in the script comments.)

