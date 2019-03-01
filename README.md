# DocFetcher
Reddit bot that, when asked for a method or class information, scrapes programming language documentation APIs and returns the values requested.

Reddit bot works in /r/learnjava and /r/javahelp at the moment. In the very near future, DocFetcher will be included in /r/learnpython and /r/learnprogramming.
DocFetcher works when called by users in the aforementioned subreddits. Simply leave a comment like so:

"!DocFetcher java Integer"

DocFetcher will leave a reply with infromation about the Integer class from the java 8 JDK documentation along with a link.

You can also use macros such as !df or !DF instead of !DocFetcher and j7, j8, j11 for the java version.
The bot currently supports java7, 8, and 11 and will support Python 2 and 3 in the near future.
You can also search for java methods like so:

"!df j8 Integer::toString"

or

"!df j8 Integer.toString"
