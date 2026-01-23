# weighted-word
This tool analyzes the thematic distribution of Bible passages and compares it with sermon or verse selections. By mapping texts to established topical bibles, it reveals over- and underemphasized themes relative to the biblical canon.

## Project Description

"The bible talks about money way more than we do today." This tool tries to empirically quantify such statements.
It is intended for churches or pastors to perform topical analysis for sermons or quoted bible verses.
With it, shortcomings or overused topics in comparision to the emphases of the bilical canon can be brought to light.

## Underlying Mechanism

To determine the topic of individual bible verses and therefore the topic distribution of the biblical corpus we use 
`Nave's Topical Bible`, `Torrey's Topical Textbook` and biblehub.com's `Topical Bible Verses`.
Combined they have XXXXX topics and XXXXXX entries

Quoting the whole bible would result in perfect topic distribution, so inputting a subset of all bible verses into the tool 
results in a suboptimal topic distribution.
The input verses are first converted into their topics and counts given the meantioned topical encyclopedias. 
This step can be skipped if raw topics and their duration in church sermons are inputted.
The now obtained topic distribution can then be compared to the topic distribution of the bible to find outliars.

