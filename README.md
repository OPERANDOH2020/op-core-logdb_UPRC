#LogDB implementation
It turns out that we have two implementations of LogDB...
The UPRC version has the following twists:
* Uses MongoDB for storage. This enables us to have huge amounts of logs that can be easily stored.
* Uses hashed macs for integrity.
* Uses tornado for performance so it's multithreaded.

The server currently listens to port 8888. A dummy test script has been appended.
