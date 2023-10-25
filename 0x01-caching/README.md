					0x01. Caching
Learning Objectives

1. What a caching system is
2. What FIFO means
3. What LIFO means
4. What LRU means
5. What MRU means
6. What LFU means
7. What the purpose of a caching system
8. What limits a caching system have

					LRU Algorithm
LRU (Least Recently used) is a group of caching technique, which disposes of the
slightest as of late utilized item first. This algorithm requires monitoring when the thing was
utilized, which is costly in the event that one needs to ensure the algorithms dependably disposes
9

of the slightest as of late utilized thing. General usage of given method require that age bits will
be kept for cache lines and Slightest Recently Used cache line will be tracked taking into account
age-bits.

The key data structure of the algorithm is the mix combination of Doubly Linked List
and Hash Map. Doubly Linked List has been utilized in order to index the pairs in the order of
information age, and initialize a Hash Map in an already defined length to store pairs.
When the information with Key E is queried, the function get E is initially called. 

On the off chance that the information of E is in the cache, the information is just returned then by cache
and invigorate (Refresh) the information in the linked list. In order to invigorate information I in
the list, we move the item of information I at head. If that is not the case then, if the information I
of key E is not in the cache, then pair is needed to embed into the list. In the event that the cache
is not full, it is embedded into the hash map, and the item is added to the head. On the off chance
that the cache is as of now fully consumed, we get the tail of the list and update it with, then this
item is moved to the head of the list [6].


					FIFO algorithm
The low-overhead and least difficult replacement algorithm is the FIFO algorithm. FIFO
is otherwise called as a round robin. The way it works is when the cache is full it simply replaces
the first item that was placed in the cache with the item needed by processor at that time, and the
next replacement then will be the 2nd item placed in the cache and vice versa.

There is no single cache algorithm which will dependably perform well since that
requires impeccable learning of the future. The strength of LRU in VM cache design is the
aftereffect of a long history of measuring system behavior. Given genuine workloads, LRU
works quite well a substantial division of the time. Be that as it may, it is not hard to build a
reference string for which FIFO would have better execution performance over LRU.
13

We can create a FIFO queue to hold every item present in the main memory. At the head
of the queue we supplant (Replace) the item. We embed item at the tail of the queue when an
item is added in into the memory disk.


					 LIFO Algorithm
A real-world stack permits operations toward one side only. For instance, we can place or
expel a card or plate from top of the stack as it were. Moreover, Stack ADT (Abstract data type)
permits all information operations toward one side as it were. At any given time, we can just get
to the top component of a stack.
 
This feature makes it LIFO data structure. The element which is
placed (embedded or added) last, is accessed first. In stack terminology, embedded operation is
called PUSH and evacuation operation is called POP.

LIFO works just opposite to that of FIFO. The item that comes last in the cache memory
is eliminated first from it, regardless of the fact that it can be needed by processor in near future.
In this way, cache miss rate can be increased because items are evicted from the cache not on the
basis on their priority


					MRU Algorithm
MRU works totally inverse to that of LRU. The items which has been used most number
of times is removed from cache when cache memory is full and processor solicit for an item that
is not in cache. This approach has a major drawback that the item which has been called most
number of time has the highest probability to be called again. 

Therefore, that item must remain inthe cache for the longest timeframe. But despite of being inside the cache, those items are removed which results in the high cache miss rate.

MRU has the issue that in the event that we get a hit on a section that is frequently
utilized as a part of "normal" mode while doing MRU lookups, we wind up tossing out the entry.

Better other options to MRU for doing a scan without contaminating the cache are following:

• Bypass/Sidestep the cache totally,
• Test the cache without doing a read through/overhaul, and without changing the LRU
chains.


