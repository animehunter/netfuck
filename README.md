netfuck
=======

A multithreaded network enabled brainfuck

Usage: python netfuck.py program.bf

The width of a cell has a minimum of 32 bits signed value.

Commands
--------
* > Move cell pointer to the right
* < Move cell pointer to the left
* + Increment value at the current cell
* - Decrement value at the current cell
* , Input a character from stdin and store it in the current cell
* . Output a character to stdin using the current cell value
* [ Jump past the matching ] if the cell under the pointer is 0
* ] Jump back to the matching [ if the cell under the pointer is nonzero

Networking Commands
-------------------
All operations are asynchronous
* ` Set the port using the value from the current cell
* ~ Connect to an IP address specified in the current cell, the socket handle is stored in the current cell. The port must be set using ` otherwise an error will occur
* = Accept a connection and store the socket handle in the current cell. The port must be set using ` otherwise an error will occur.
* ! Close a connection using the socket handle from the current cell
* ^ Send the current cell value using the socket handle stored from the current cell
* v Receive a value using the socket handle from the current cell and store it in the current cell 

Threading Commands
------------------
A thread must be green.
All threads must run in one operating system thread.
* | Fork, if parent the current cell is 0, else the current cell is 1
* ~ Sleep for n milliseconds

Handling Error
--------------
All networking commands return a -1 on error

Endian
------
IP and port must be specified in network endian order. 

Synchronization issues
----------------------
It has no synchronization issues or whatsoever, since the 
threads are all executed in a single operating system thread.

TODO
----
`, ~, =, !, ^, v, |, ~
