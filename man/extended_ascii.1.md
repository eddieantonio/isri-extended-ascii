% EXTENDED_ASCII(1) Extended ASCII
% Eddie Antonio Santos
% October 30, 2015

# NAME

extended_ascii - convert UTF-8 to ISRI Extended ASCII

# SYNOPSIS

extended_ascii [*input-file*]

to_utf8 [*input-file*]

# DESCRIPTION

`extended_ascii` converts from UTF-8 to extended ASCII format, for use
with the ISRI Analytical Tools. Use this executable as a simple filter:

    extended_ascii < utf8-file > extended-ascii-file

`to_utf8` reverses this `extended_ascii`, converting to UTF-8:

    < original-file extended_ascii | to_utf8 > utf8-file

`extended_ascii` only knows UTF-8. If your files are in another
encoding, use a tool like iconv(1) to convert the file to UTF-8, and
then pipe it through extended_ascii:

    iconv -t utf-8 input.txt | extended_ascii > output.txt

# LICENSE

MIT licensed.
