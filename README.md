# Google Interview University

This is my multi-month study plan for going from web developer (self-taught, no CS degree) to Google software engineer.

- [The Daily Plan](#the-daily-plan)
- [Algorithmic complexity / Big-O / Asymptotic analysis](#algorithmic-complexity--big-o--asymptotic-analysis)
- [Data Structures](#data-structures)
    - [Arrays](#arrays)
    - [Linked Lists](#linked-lists)
    - [Stack](#stack)
    - [Queue](#queue)
    - [Hash table](#hash-table)
- [More Knowledge](#more-knowledge)
    - [Endianness](#endianness)
    - [Binary search](#binary-search)
    - [Bitwise operations](#bitwise-operations)
- [Trees](#trees)
    - [Trees - Notes & Background](#trees---notes--background)
    - [Binary search trees: BSTs](#binary-search-trees-bsts)
    - [Heap / Priority Queue / Binary Heap](#heap--priority-queue--binary-heap)
    - [Tries](#tries)
    - [Balanced search trees](#balanced-search-trees)
    - [N-ary (K-ary, M-ary) trees](#n-ary-k-ary-m-ary-trees)
- [Sorting](#sorting)
- [Graphs](#graphs)
- [Even More Knowledge](#even-more-knowledge)
    - [Recursion](#recursion)
    - [Dynamic Programming](#dynamic-programming)
    - [Combinatorics (n choose k) & Probability](#combinatorics-n-choose-k--probability)
    - [NP, NP-Complete and Approximation Algorithms](#np-np-complete-and-approximation-algorithms)
    - [Garbage collection](#garbage-collection)
    - [Caches](#caches)
    - [Processes and Threads](#processes-and-threads)
    - [System Design, Scalability, Data Handling](#system-design-scalability-data-handling)
    - [Unicode](#unicode)
    - [Testing](#testing)
    - [Design patterns](#design-patterns)

- [Final Review](#final-review)
- [Books](#books)
- [Coding exercises/challenges](#coding-exerciseschallenges)


## Interview Process & General Interview Prep

- [ ] Articles:
    - [ ] http://www.google.com/about/careers/lifeatgoogle/hiringprocess/
    - [ ] http://steve-yegge.blogspot.com/2008/03/get-that-job-at-google.html
        - all the things he mentions that you need to know are listed below
    - [ ] (very dated) http://dondodge.typepad.com/the_next_big_thing/2010/09/how-to-get-a-job-at-google-interview-questions-hiring-process.html
    - [ ] http://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions

- [ ] Additional (not suggested by Google but I added):
    - [ ] https://medium.com/always-be-coding/abc-always-be-coding-d5f8051afce2#.4heg8zvm4
    - [ ] https://medium.com/always-be-coding/four-steps-to-google-without-a-degree-8f381aa6bd5e#.asalo1vfx
    - [ ] https://medium.com/@dpup/whiteboarding-4df873dbba2e#.hf6jn45g1
    - [ ] http://www.kpcb.com/blog/lessons-learned-how-google-thinks-about-hiring-management-and-culture
    - [ ] http://www.coderust.com/blog/2014/04/10/effective-whiteboarding-during-programming-interviews/
    - [ ] Cracking The Coding Interview Set 1:
        - [ ] https://www.youtube.com/watch?v=rEJzOhC5ZtQ
        - [ ] https://www.youtube.com/watch?v=aClxtDcdpsQ
    - [ ] How to Get a Job at the Big 4:
        - [ ] https://www.youtube.com/watch?v=YJZCUhxNCv8
    - [ ] http://alexbowe.com/failing-at-google-interviews/

- [ ] **Python**
    - [ ] [Python Cheat Sheet](https://github.com/jwasham/google-interview-university/blob/master/extras/cheat%20sheets/python-cheat-sheet-v1.pdf)
    - [ ] Python in One Video: https://www.youtube.com/watch?v=N4mEzFDjqtA
    - [ ] Series on 3.4: https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_
    - [ ] Zero to Hero: https://www.youtube.com/watch?v=emY34tSKXc4
    - [ ] Statistics for Hackers: https://www.youtube.com/watch?v=Iq9DzN6mvYA
    - [ ] Faster Python: https://www.youtube.com/watch?v=JDSGVvMwNM8
    - [ ] CPython Walk: https://www.youtube.com/watch?v=LhadeL7_EIU&list=PLzV58Zm8FuBL6OAv1Yu6AwXZrnsFbbR0S&index=6
    - [ ] 10 Tips for Pythonic Code: https://www.youtube.com/watch?v=_O23jIXsshs
    - [ ] Beyond PEP 8 -- Best practices for beautiful intelligible code: https://www.youtube.com/watch?v=wf-BqAjZb8M

## The Daily Plan

Rehearse previous topic via anki.
Study a topic.
Implement with basic code. 
Write automated tests, basic asserts will do.
Sometimes write it on paper.
After studying a topic make anki cards for all parts that need memorizing:
    - For algorithms: summary (1 sentence), big-oh complexity
    - For data structures: summary, retrieval/deletion/insertion complexity
    - For paradigms: summary, examples of use

## Algorithmic complexity / Big-O / Asymptotic analysis
- [x] A Gentle Introduction to Algorithm Complexity Analysis: http://discrete.gr/complexity/
- [x] TopCoder (includes recurrence relations and master theorem):
    - Computational Complexity: Section 2: https://www.topcoder.com/community/data-science/data-science-tutorials/computational-complexity-section-2/
- [x] Cheat sheet: http://bigocheatsheet.com/

### Additional knowledge
- [x] Logarithms: http://tutorial.math.lamar.edu/Classes/Alg/LogFunctions.aspx#ExpLog_Log_Ex1_a
- [х] Combinatorics: https://www.topcoder.com/community/data-science/data-science-tutorials/basics-of-combinatorics/
- [ ] Probability theory basics
	- [ ] Learn definitions https://arbital.com/p/probability/
	- [ ] 
- [ ] Statistics basics
- [ ] Linear algebra basics
- [ ] Trigonometry basics
- [ ] Calculus basics

## Data Structures
- Good info source: https://courses.cs.washington.edu/courses/cse326/00wi/handouts.html
- [ ] https://www.topcoder.com/community/data-science/data-science-tutorials/data-structures/
- ### Arrays
    - [x] Description:
        - Arrays: https://en.wikipedia.org/wiki/Array_data_structure


- ### Linked Lists
    - [x] Description: http://openbookproject.net/thinkcs/python/english3e/linked_lists.html


- ### Stack
    - [x] Description: http://openbookproject.net/thinkcs/python/english3e/stacks.html


- ### Queue
    - [x] Description: http://openbookproject.net/thinkcs/python/english3e/queues.html
    - [x] Write an implementation of the Priority Queue ADT using a linked list. You should keep the list sorted so that removal is a constant time operation. Compare the performance of this implementation with the Python list implementation.


- ### Hash table
    - [x] http://www.linuxjournal.com/content/hash-tables%E2%80%94theory-and-practice	
    - [x] https://www.cs.auckland.ac.nz/~jmor159/PLDS210/niemann/s_has.htm
    - [x] Implement stuff from here http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html
    - [x] implement with array using linear probing
        - hash(k, m) - m is size of hash table
        - add(key, value) - if key already exists, update value
        - exists(key)
        - get(key)
        - remove(key)

## More Knowledge
- Very good: http://interactivepython.org/runestone/static/pythonds/index.html
- Mandatory: http://openbookproject.net/thinkcs/python/english3e
- Tad bit more advanced http://interactivepython.org/runestone/static/pythonds/index.html


- ### Endianness
    - [x] https://www.cs.umd.edu/class/sum2003/cmsc311/Notes/Data/endian.html

- ### Binary search
    - [x] https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search
    - [x] Implement:
        - binary search (on sorted array of integers)
        - binary search using recursion


## Trees
- ### Trees - Notes & Background
    - [ ] http://interactivepython.org/runestone/static/pythonds/Trees/toctree.html
    - [x] basic tree construction
    - [x] traversal
    - manipulation algorithms
    - [ ] BFS (breadth-first search)
        - level order (BFS, using queue) Implement!
            time complexity: O(n)
            space complexity: best: O(1), worst: O(n/2)=O(n)

    - DFS (depth-first search)
        - notes:
            time complexity: O(n)
            space complexity:
                best: O(log n) - avg. height of tree
                worst: O(n)
        - [x] inorder (DFS: left, self, right)
        - [x] postorder (DFS: left, right, self)
        - [x] preorder (DFS: self, left, right)

==CURRENTLY HERE== 
- ### Binary search trees: BSTs
    - [ ] Implement:
        - [ ] insert    // insert value into tree
        - [ ] get_node_count // get count of values stored
        - [ ] print_values // prints the values in the tree, from min to max
        - [ ] delete_tree
        - [ ] is_in_tree // returns true if given value exists in the tree
        - [ ] get_height // returns the height in nodes (single node's height is 1)
        - [ ] get_min   // returns the minimum value stored in the tree
        - [ ] get_max   // returns the maximum value stored in the tree
        - [ ] is_binary_search_tree
        - [ ] delete_value
        - [ ] get_successor // returns next-highest value in tree after given value, -1 if none

- ### Heap / Priority Queue / Binary Heap
    - visualized as a tree, but is usually linear in storage (array, linked list)
    - [ ] https://en.wikipedia.org/wiki/Heap_(data_structure)
    - [ ] https://www.coursera.org/learn/data-structures/lecture/2OpTs/introduction
    - [ ] https://www.coursera.org/learn/data-structures/lecture/z3l9N/naive-implementations
    - [ ] https://www.coursera.org/learn/data-structures/lecture/GRV2q/binary-trees
    - [ ] https://www.coursera.org/learn/data-structures/supplement/S5xxz/tree-height-remark
    - [ ] https://www.coursera.org/learn/data-structures/lecture/GRV2q/binary-trees
    - [ ] https://www.coursera.org/learn/data-structures/lecture/0g1dl/basic-operations
    - [ ] https://www.coursera.org/learn/data-structures/lecture/gl5Ni/complete-binary-trees
    - [ ] https://www.coursera.org/learn/data-structures/lecture/HxQo9/pseudocode
    - [ ] Heap Sort - jumps to start: https://youtu.be/odNJmw5TOEE?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3291
    - [ ] Heap Sort: https://www.coursera.org/learn/data-structures/lecture/hSzMO/heap-sort
    - [ ] Building a heap: https://www.coursera.org/learn/data-structures/lecture/dwrOS/building-a-heap
    - [ ] MIT: Heaps and Heap Sort: https://www.youtube.com/watch?v=B7hVxCmfPtM&index=4&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb
    - [ ] CS 61B Lecture 24: Priority Queues: https://www.youtube.com/watch?v=yIUFT6AKBGE&index=24&list=PL4BBB74C7D2A1049C
    - [ ] Linear Time BuildHeap (max-heap): https://www.youtube.com/watch?v=MiyLo8adrWw
    - [ ] Implement a min-heap:
        - [ ] insert
        - [ ] sift_up - needed for insert
        - [ ] get_max - returns the min item, without removing it
        - [ ] get_size() - return number of elements stored
        - [ ] is_empty() - returns true if heap contains no elements
        - [ ] extract_max - returns the min item, removing it
        - [ ] sift_down - needed for extract_max
        - [ ] remove(i) - removes item at index x
        - [ ] heapify - create a heap from an array of elements, needed for heap_sort
        - [ ] heap_sort() - take an unsorted array and turn it into a sorted array in-place using a min heap
            - note: using a min heap instead would save operations, but double the space needed (cannot do in-place).
        - Test min-heap on large arrays of numbers, 10 million at least 
- ### Tries
    - Note there are different kinds of tries. Some have prefixes, some don't, and some use string instead of bits
        to track the path.
    - I read through code, but will not implement.
    - [ ] http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#Tries
    - [ ] Short course videos:
        - [ ] https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/08Xyf/core-introduction-to-tries
        - [ ] https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/PvlZW/core-performance-of-tries
        - [ ] https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/DFvd3/core-implementing-a-trie
    - [ ] The Trie: A Neglected Data Structure: https://www.toptal.com/java/the-trie-a-neglected-data-structure
    - [ ] TopCoder - Using Tries: https://www.topcoder.com/community/data-science/data-science-tutorials/using-tries/
    - [ ] Stanford Lecture (real world use case): https://www.youtube.com/watch?v=TJ8SkcUSdbU
    - [ ] MIT, Advanced Data Structures, Strings (can get pretty obscure about halfway through): https://www.youtube.com/watch?v=NinWEPPrkDQ&index=16&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf

- ### Balanced search trees
    - Know least one type of balanced binary tree (and know how it's implemented):
    - "Among balanced search trees, AVL and 2/3 trees are now passé, and red-black trees seem to be more popular.
        A particularly interesting self-organizing data structure is the splay tree, which uses rotations
        to move any accessed key to the root." - Skiena
    - Of these, I chose to implement a splay tree. From what I've read, you won't implement a
        balanced search tree in your interview. But I wanted exposure to coding one up
        and let's face it, splay trees are the bee's knees. I did read a lot of red-black tree code.
        - splay tree: insert, search, delete functions
        If you end up implementing red/black tree try just these:
        - search and insertion functions, skipping delete
    - I want to learn more about B-Tree since it's used so widely with very large data sets.
    - [ ] Self-balancing binary search tree: https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree


    - [ ] **Splay trees**
        - In practice:
            Splay trees are typically used in the implementation of caches, memory allocators, routers, garbage collectors,
            data compression, ropes (replacement of string used for long text strings), in Windows NT (in the virtual memory,
            networking, and file system code) etc.
        - [ ] CS 61B: Splay Trees: https://www.youtube.com/watch?v=Najzh1rYQTo&index=23&list=PL-XXv-cvA_iAlnI-BQr9hjqADPBtujFJd
        - [ ] MIT Lecture: Splay Trees:
                - Gets very mathy, but watch the last 10 minutes for sure.
                - https://www.youtube.com/watch?v=QnPl_Y6EqMo

    - [ ] **2-3-4 Trees (aka 2-4 trees)**
        - In practice:
            For every 2-4 tree, there are corresponding red–black trees with data elements in the same order. The insertion and deletion
            operations on 2-4 trees are also equivalent to color-flipping and rotations in red–black trees. This makes 2-4 trees an
            important tool for understanding the logic behind red–black trees, and this is why many introductory algorithm texts introduce
            2-4 trees just before red–black trees, even though **2-4 trees are not often used in practice**.
        - [ ] CS 61B Lecture 26: Balanced Search Trees: https://www.youtube.com/watch?v=zqrqYXkth6Q&index=26&list=PL4BBB74C7D2A1049C
        - [ ] Bottom Up 234-Trees: https://www.youtube.com/watch?v=DQdMYevEyE4&index=4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6
        - [ ] Top Down 234-Trees: https://www.youtube.com/watch?v=2679VQ26Fp4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=5

    - [ ] **B-Trees**
        - fun fact: it's a mystery, but the B could stand for Boeing, Balanced, or Bayer (co-inventor)
        - In Practice:
            B-Trees are widely used in databases. Most modern filesystems use B-trees (or Variants). In addition to
            its use in databases, the B-tree is also used in filesystems to allow quick random access to an arbitrary
            block in a particular file. The basic problem is turning the file block i address into a disk block
            (or perhaps to a cylinder-head-sector) address.
        - [ ] B-Tree: https://en.wikipedia.org/wiki/B-tree

    - [ ] **Red/black trees**
        - In practice:
            Red–black trees offer worst-case guarantees for insertion time, deletion time, and search time.
            Not only does this make them valuable in time-sensitive applications such as real-time applications,
            but it makes them valuable building blocks in other data structures which provide worst-case guarantees;
            for example, many data structures used in computational geometry can be based on red–black trees, and
            the Completely Fair Scheduler used in current Linux kernels uses red–black trees. In the version 8 of Java,
            the Collection HashMap has been modified such that instead of using a LinkedList to store identical elements with poor
            hashcodes, a Red-Black tree is used.
        - [ ] Aduni - Algorithms - Lecture 4
            link jumps to starting point:
            https://youtu.be/1W3x0f_RmUo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3871
        - [ ] Aduni - Algorithms - Lecture 5: https://www.youtube.com/watch?v=hm2GHwyKF1o&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=5
        - [ ] https://en.wikipedia.org/wiki/Red%E2%80%93black_tree
        - [ ] https://www.topcoder.com/community/data-science/data-science-tutorials/an-introduction-to-binary-search-and-red-black-trees/

- ### N-ary (K-ary, M-ary) trees
    - note: the N or K is the branching factor (max branches)
        - binary trees are a 2-ary tree, with branching factor = 2
        - 2-3 trees are 3-ary
    - [ ] https://en.wikipedia.org/wiki/K-ary_tree

## Sorting

- [ ] Notes:
    - Implement sorts & know best case/worst case, average complexity of each:
        - no bubble sort - it's terrible - O(n^2), except when n <= 16
    - [ ] stability in sorting algorithms ("Is Quicksort stable?")
        - https://en.wikipedia.org/wiki/Sorting_algorithm#Stability
        - http://stackoverflow.com/questions/1517793/stability-in-sorting-algorithms
        - http://www.geeksforgeeks.org/stability-in-sorting-algorithms/
        - http://homepages.math.uic.edu/~leon/cs-mcs401-s08/handouts/stability.pdf
    - [ ] Which algorithms can be used on linked lists? Which on arrays? Which on both?
        - I wouldn't recommend sorting a linked list, but merge sort is doable.
        - http://www.geeksforgeeks.org/merge-sort-for-linked-list/

- For heapsort, see Heap data structure above. Heap sort is great, but not stable.

- [ ] Bubble Sort: https://www.youtube.com/watch?v=P00xJgWzz2c&index=1&list=PL89B61F78B552C1AB
- [ ] Analyzing Bubble Sort: https://www.youtube.com/watch?v=ni_zk257Nqo&index=7&list=PL89B61F78B552C1AB
- [ ] Insertion Sort, Merge Sort: https://www.youtube.com/watch?v=Kg4bqzAqRBM&index=3&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb
- [ ] Insertion Sort: https://www.youtube.com/watch?v=c4BRHC7kTaQ&index=2&list=PL89B61F78B552C1AB
- [ ] Merge Sort: https://www.youtube.com/watch?v=GCae1WNvnZM&index=3&list=PL89B61F78B552C1AB
- [ ] Quicksort: https://www.youtube.com/watch?v=y_G9BkAm6B8&index=4&list=PL89B61F78B552C1AB
- [ ] Selection Sort: https://www.youtube.com/watch?v=6nDMgr0-Yyo&index=8&list=PL89B61F78B552C1AB

- [ ] Stanford lectures on sorting:
    - [ ] https://www.youtube.com/watch?v=ENp00xylP7c&index=15&list=PLFE6E58F856038C69
    - [ ] https://www.youtube.com/watch?v=y4M9IVgrVKo&index=16&list=PLFE6E58F856038C69

- [ ] Shai Simonson, [Aduni.org](http://www.aduni.org/):
    - [ ] https://www.youtube.com/watch?v=odNJmw5TOEE&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=2
    - [ ] https://www.youtube.com/watch?v=hj8YKFTFKEE&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=3

- [ ] Steven Skiena lectures on sorting:
    - [ ] lecture begins at 26:46: https://youtu.be/ute-pmMkyuk?list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&t=1600
    - [ ] lecture begins at 27:40: https://www.youtube.com/watch?v=yLvp-pB8mak&index=8&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b
    - [ ] lecture begins at 35:00: https://www.youtube.com/watch?v=q7K9otnzlfE&index=9&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b
    - [ ] lecture begins at 23:50: https://www.youtube.com/watch?v=TvqIGu9Iupw&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=10

- [ ] UC Berkeley:
    - [ ] CS 61B Lecture 29: Sorting I: https://www.youtube.com/watch?v=EiUvYS2DT6I&list=PL4BBB74C7D2A1049C&index=29
    - [ ] CS 61B Lecture 30: Sorting II: https://www.youtube.com/watch?v=2hTY3t80Qsk&list=PL4BBB74C7D2A1049C&index=30
    - [ ] CS 61B Lecture 32: Sorting III: https://www.youtube.com/watch?v=Y6LOLpxg6Dc&index=32&list=PL4BBB74C7D2A1049C
    - [ ] CS 61B Lecture 33: Sorting V: https://www.youtube.com/watch?v=qNMQ4ly43p4&index=33&list=PL4BBB74C7D2A1049C

- [ ] - Merge sort code:
    - [ ] Using output array: http://www.cs.yale.edu/homes/aspnes/classes/223/examples/sorting/mergesort.c
    - [ ] In-place: https://github.com/jwasham/practice-cpp/blob/master/merge_sort/merge_sort.cc
- [ ] - Quick sort code:
    - [ ] http://www.cs.yale.edu/homes/aspnes/classes/223/examples/randomization/quick.c
    - [ ] https://github.com/jwasham/practice-c/blob/master/quick_sort/quick_sort.c

- [ ] Implement:
    - [ ] Mergesort: O(n log n) average and worst case
    - [ ] Quicksort O(n log n) average case
    - Selection sort and insertion sort are both O(n^2) average and worst case
    - For heapsort, see Heap data structure above.

## Graphs

Graphs can be used to represent many problems in computer science, so this section is long, like trees and sorting were.

- Notes from Yegge:
    - There are three basic ways to represent a graph in memory:
        - objects and pointers
        - matrix
        - adjacency list
    - Familiarize yourself with each representation and its pros & cons
    - BFS and DFS - know their computational complexity, their tradeoffs, and how to implement them in real code
    - When asked a question, look for a graph-based solution first, then move on if none.

- [ ] Skiena Lectures - great intro:
    - [ ] CSE373 2012 - Lecture 11 - Graph Data Structures: https://www.youtube.com/watch?v=OiXxhDrFruw&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=11
    - [ ] CSE373 2012 - Lecture 12 - Breadth-First Search: https://www.youtube.com/watch?v=g5vF8jscteo&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=12
    - [ ] CSE373 2012 - Lecture 13 - Graph Algorithms: https://www.youtube.com/watch?v=S23W6eTcqdY&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=13
    - [ ] CSE373 2012 - Lecture 14 - Graph Algorithms (con't): https://www.youtube.com/watch?v=WitPBKGV0HY&index=14&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b
    - [ ] CSE373 2012 - Lecture 15 - Graph Algorithms (con't 2): https://www.youtube.com/watch?v=ia1L30l7OIg&index=15&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b
    - [ ] CSE373 2012 - Lecture 16 - Graph Algorithms (con't 3): https://www.youtube.com/watch?v=jgDOQq6iWy8&index=16&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b

- [ ] Graphs (review and more):

    - [ ] 6.006 Single-Source Shortest Paths Problem: https://www.youtube.com/watch?v=Aa2sqUhIn-E&index=15&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb
    - [ ] 6.006 Dijkstra: https://www.youtube.com/watch?v=2E7MmKv0Y24&index=16&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb
    - [ ] 6.006 Bellman-Ford: https://www.youtube.com/watch?v=ozsuci5pIso&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=17
    - [ ] 6.006 Speeding Up Dijkstra: https://www.youtube.com/watch?v=CHvQ3q_gJ7E&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=18
    - [ ] Aduni: Graph Algorithms I - Topological Sorting, Minimum Spanning Trees, Prim's Algorithm -  Lecture 6: https://www.youtube.com/watch?v=i_AQT_XfvD8&index=6&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm
    - [ ] Aduni: Graph Algorithms II - DFS, BFS, Kruskal's Algorithm, Union Find Data Structure - Lecture 7: https://www.youtube.com/watch?v=ufj5_bppBsA&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=7
    - [ ] Aduni: Graph Algorithms III: Shortest Path - Lecture 8: https://www.youtube.com/watch?v=DiedsPsMKXc&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=8
    - [ ] Aduni: Graph Alg. IV: Intro to geometric algorithms - Lecture 9: https://www.youtube.com/watch?v=XIAQRlNkJAw&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=9
    - [ ] CS 61B 2014 (starting at 58:09): https://youtu.be/dgjX4HdMI-Q?list=PL-XXv-cvA_iAlnI-BQr9hjqADPBtujFJd&t=3489
    - [ ] CS 61B 2014: Weighted graphs: https://www.youtube.com/watch?v=aJjlQCFwylA&list=PL-XXv-cvA_iAlnI-BQr9hjqADPBtujFJd&index=19
    - [ ] Greedy Algorithms: Minimum Spanning Tree: https://www.youtube.com/watch?v=tKwnms5iRBU&index=16&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp
    - [ ] Strongly Connected Components Kosaraju's Algorithm Graph Algorithm: https://www.youtube.com/watch?v=RpgcYiky7uw

- Yegge: If you get a chance, try to study up on fancier algorithms:
    - [ ] Dijkstra's algorithm - see above - 6.006
    - [ ] A*
        - [ ] https://en.wikipedia.org/wiki/A*_search_algorithm
        - [ ] A* Pathfinding Tutorial: https://www.youtube.com/watch?v=KNXfSOx4eEE
        - [ ] A* Pathfinding (E01: algorithm explanation): https://www.youtube.com/watch?v=-L-WgKMFuhE

- I'll implement:
    - [ ] DFS with adjacency list (recursive)
    - [ ] DFS with adjacency list (iterative with stack)
    - [ ] DFS with adjacency matrix (recursive)
    - [ ] DFS with adjacency matrix (iterative with stack)
    - [ ] BFS with adjacency list
    - [ ] BFS with adjacency matrix
    - [ ] single-source shortest path (Dijkstra)

You'll get more graph practice in Skiena's book (see Books section below) and the interview books

## Even More Knowledge

- ### Recursion
    - [ ] Stanford lectures on recursion & backtracking:
        - [ ] https://www.youtube.com/watch?v=gl3emqCuueQ&list=PLFE6E58F856038C69&index=8
        - [ ] https://www.youtube.com/watch?v=uFJhEPrbycQ&list=PLFE6E58F856038C69&index=9
        - [ ] https://www.youtube.com/watch?v=NdF1QDTRkck&index=10&list=PLFE6E58F856038C69
        - [ ] https://www.youtube.com/watch?v=p-gpaIGRCQI&list=PLFE6E58F856038C69&index=11
    - when it is appropriate to use it
    - how is tail recursion better than not?
        - [ ] https://www.quora.com/What-is-tail-recursion-Why-is-it-so-bad
        - [ ] https://www.youtube.com/watch?v=L1jjXGfxozc
 
- ### Dynamic Programming
    - This subject can be pretty difficult, as each DP soluble problem must be defined as a recursion relation, and coming up with it can be tricky.
    - I suggest looking at many examples of DP problems until you have a solid understanding of the pattern involved.
    - [ ] Videos:
        - the Skiena videos can be hard to follow since he sometimes uses the whiteboard, which is too small to see
        - [ ] Skiena: CSE373 2012 - Lecture 19 - Introduction to Dynamic Programming: https://youtu.be/Qc2ieXRgR0k?list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&t=1718
        - [ ] Skiena: CSE373 2012 - Lecture 20 - Edit Distance: https://youtu.be/IsmMhMdyeGY?list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&t=2749
        - [ ] Skiena: CSE373 2012 - Lecture 21 - Dynamic Programming Examples: https://youtu.be/o0V9eYF4UI8?list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&t=406
        - [ ] Skiena: CSE373 2012 - Lecture 22 - Applications of Dynamic Programming: https://www.youtube.com/watch?v=dRbMC1Ltl3A&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=22
        - [ ] Simonson: Dynamic Programming 0 (starts at 59:18): https://youtu.be/J5aJEcOr6Eo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3558
        - [ ] Simonson: Dynamic Programming I - Lecture 11: https://www.youtube.com/watch?v=0EzHjQ_SOeU&index=11&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm
        - [ ] Simonson: Dynamic programming II - Lecture 12: https://www.youtube.com/watch?v=v1qiRwuJU7g&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=12
        - [ ] List of individual DP problems (each is short):
            https://www.youtube.com/playlist?list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr
    - [ ] Yale Lecture notes: 
        - [ ] http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#dynamicProgramming
    - [ ] Coursera:
        - [ ] The RNA secondary structure problem: https://www.coursera.org/learn/algorithmic-thinking-2/lecture/80RrW/the-rna-secondary-structure-problem
        - [ ] A dynamic programming algorithm: https://www.coursera.org/learn/algorithmic-thinking-2/lecture/PSonq/a-dynamic-programming-algorithm
        - [ ] Illustrating the DP algorithm: https://www.coursera.org/learn/algorithmic-thinking-2/lecture/oUEK2/illustrating-the-dp-algorithm
        - [ ] Running time of the DP algorithm: https://www.coursera.org/learn/algorithmic-thinking-2/lecture/nfK2r/running-time-of-the-dp-algorithm
        - [ ] DP vs. recursive implementation: https://www.coursera.org/learn/algorithmic-thinking-2/lecture/M999a/dp-vs-recursive-implementation
        - [ ] Global pairwise sequence alignment: https://www.coursera.org/learn/algorithmic-thinking-2/lecture/UZ7o6/global-pairwise-sequence-alignment
        - [ ] Local pairwise sequence alignment: https://www.coursera.org/learn/algorithmic-thinking-2/lecture/WnNau/local-pairwise-sequence-alignment

- ### NP, NP-Complete and Approximation Algorithms
    - Know about the most famous classes of NP-complete problems, such as traveling salesman and the knapsack problem,
        and be able to recognize them when an interviewer asks you them in disguise.
    - Know what NP-complete means.
    - [ ] Computational Complexity: https://www.youtube.com/watch?v=moPtwq_cVH8&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=23
    - [ ] Simonson:
        - [ ] https://youtu.be/qcGnJ47Smlo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=2939
        - [ ] https://www.youtube.com/watch?v=e0tGC6ZQdQE&index=16&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm
        - [ ] https://www.youtube.com/watch?v=fCX1BGT3wjE&index=17&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm
        - [ ] https://www.youtube.com/watch?v=NKLDp3Rch3M&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=18
    - [ ] Skiena:
        - [ ] CSE373 2012 - Lecture 23 - Introduction to NP-Completeness: https://youtu.be/KiK5TVgXbFg?list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&t=1508
        - [ ] CSE373 2012 - Lecture 24 - NP-Completeness Proofs: https://www.youtube.com/watch?v=27Al52X3hd4&index=24&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b
        - [ ] CSE373 2012 - Lecture 25 - NP-Completeness Challenge: https://www.youtube.com/watch?v=xCPH4gwIIXM&index=25&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b
    - [ ] Complexity: P, NP, NP-completeness, Reductions: https://www.youtube.com/watch?v=eHZifpgyH_4&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=22
    - [ ] Complexity: Approximation Algorithms: https://www.youtube.com/watch?v=MEz1J9wY2iM&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=24
    - [ ] Complexity: Fixed-Parameter Algorithms: https://www.youtube.com/watch?v=4q-jmGrmxKs&index=25&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp
    - Peter Norvik discusses near-optimal solutions to traveling salesman problem:
        - http://nbviewer.jupyter.org/url/norvig.com/ipython/TSP.ipynb
    - Pages 1048 - 1140 in CLRS if you have it.

- ### Garbage collection
    - [ ] GC in Python: https://www.youtube.com/watch?v=iHVs_HkjdmI
    - [ ] Deep Dive Python: Garbage Collection in CPython: https://www.youtube.com/watch?v=P-8Z0-MhdQs&list=PLdzf4Clw0VbOEWOS_sLhT_9zaiQDrS5AR&index=3

- ### Processes and Threads
    - [ ] Computer Science 162 - Operating Systems (25 videos):
        - for precesses and threads see videos 1-11
        - https://www.youtube.com/playlist?list=PL-XXv-cvA_iBDyz-ba4yDskqMDY6A1w_c
    - https://www.quora.com/What-is-the-difference-between-a-process-and-a-thread
    - Covers:
        - Processes, Threads, Concurrency issues
            - difference between processes and threads
            - processes
            - threads
            - locks
            - mutexes
            - semaphores
            - monitors
            - how they work
            - deadlock
            - livelock
        - CPU activity, interrupts, context switching
        - Modern concurrency constructs with multicore processors
        - Process resource needs (memory: code, static storage, stack, heap, and also file descriptors, i/o)
        - Thread resource needs (shares above (minus stack) with other threads in same process but each has its own pc, stack counter, registers and stack)
        - Forking is really copy on write (read-only) until the new process writes to memory, then it does a full copy.
        - Context switching
            - How context switching is initiated by the operating system and underlying hardware
    - [ ] concurrency in Python:
        - [ ] Short series on threads: https://www.youtube.com/playlist?list=PL1H1sBF1VAKVMONJWJkmUh6_p8g4F2oy1
        - [ ] Python Threads: https://www.youtube.com/watch?v=Bs7vPNbB9JM
        - [ ] Understanding the Python GIL (2010): https://www.youtube.com/watch?v=Obt-vMVdM8s
            - reference: http://www.dabeaz.com/GIL
        - [ ] David Beazley - Python Concurrency From the Ground Up: LIVE! - PyCon 2015: https://www.youtube.com/watch?v=MCs5OvhV9S4
        - [ ] Keynote David Beazley - Topics of Interest (Python Asyncio): https://www.youtube.com/watch?v=ZzfHjytDceU
        - [ ] Mutex in Python: https://www.youtube.com/watch?v=0zaPs8OtyKY


    Scalability and System Design are very large topics with many topics and resources, since there is a lot to consider 
    when designing a software/hardware system that can scale. Expect to spend quite a bit of time on this.

- ### System Design, Scalability, Data Handling
    - Considerations from Yegge:
        - scalability
            - Distill large data sets to single values
            - Transform one data set to another
            - Handling obscenely large amounts of data
        - system design
            - features sets
            - interfaces
            - class hierarchies
            - designing a system under certain constraints
            - simplicity and robustness
            - tradeoffs
            - performance analysis and optimization
    - [ ] **START HERE**: System Design from HiredInTech: http://www.hiredintech.com/system-design/
    - [ ] https://www.quora.com/How-do-I-prepare-to-answer-design-questions-in-a-technical-interview?redirected_qid=1500023
    - [ ] 8 Things You Need to Know Before a System Design Interview: http://blog.gainlo.co/index.php/2015/10/22/8-things-you-need-to-know-before-system-design-interviews/
    - [ ] Algorithm design: http://www.hiredintech.com/algorithm-design/
    - [ ] Database Normalization - 1NF, 2NF, 3NF and 4NF: https://www.youtube.com/watch?v=UrYLYV7WSHM
    - [ ] https://github.com/checkcheckzz/system-design-interview - There are a lot of resources in this one. Look through the articles and examples. I put some of them below.
    - [ ] How to ace a systems design interview: http://www.palantir.com/2011/10/how-to-rock-a-systems-design-interview/
    - [ ] Numbers Everyone Should Know: http://everythingisdata.wordpress.com/2009/10/17/numbers-everyone-should-know/
    - [ ] How long does it take to make a context switch?: http://blog.tsunanet.net/2010/11/how-long-does-it-take-to-make-context.html
    - [ ] Transactions Across Datacenters: https://www.youtube.com/watch?v=srOgpXECblk
    - [ ] A plain english introduction to CAP Theorem: http://ksat.me/a-plain-english-introduction-to-cap-theorem/
    - [ ] Paxos Consensus algorithm: 
        - short video: https://www.youtube.com/watch?v=s8JqcZtvnsM
        - extended video with use case and multi-paxos: https://www.youtube.com/watch?v=JEpsBg0AO6o
        - paper: http://research.microsoft.com/en-us/um/people/lamport/pubs/paxos-simple.pdf
    - [ ] Consistent Hashing: http://www.tom-e-white.com/2007/11/consistent-hashing.html
    - [ ] NoSQL Patterns: http://horicky.blogspot.com/2009/11/nosql-patterns.html
    - [ ] Optional: UML 2.0 Series: https://www.youtube.com/watch?v=OkC7HKtiZC0&list=PLGLfVvz_LVvQ5G-LdJ8RLqe-ndo7QITYc
    - [ ] OOSE: Software Dev Using UML and Java (21 videos): 
        - Can skip this if you have a great grasp of OO and OO design practices.
        - https://www.youtube.com/playlist?list=PLJ9pm_Rc9HesnkwKlal_buSIHA-jTZMpO
    - [ ] SOLID OOP Principles:
        - [ ] Bob Martin SOLID Principles of Object Oriented and Agile Design: https://www.youtube.com/watch?v=TMuno5RZNeE
        - [ ] SOLID Design Patterns in C#: https://www.youtube.com/playlist?list=PL8m4NUhTQU48oiGCSgCP1FiJEcg_xJzyQ
        - [ ] SOLID Principles: https://www.youtube.com/playlist?list=PL4CE9F710017EA77A
        - [ ] S - Single Responsibility Principle | Single responsibility to each Object
            - http://www.oodesign.com/single-responsibility-principle.html
            - http://www.javacodegeeks.com/2011/11/solid-single-responsibility-principle.html
            - more flavor: https://docs.google.com/open?id=0ByOwmqah_nuGNHEtcU5OekdDMkk
        - [ ] O - Open/Closed Principal  | On production level Objects are ready for extension for not for modification
            - http://www.oodesign.com/open-close-principle.html
            - https://en.wikipedia.org/wiki/Open/closed_principle
            - more flavor: http://docs.google.com/a/cleancoder.com/viewer?a=v&pid=explorer&chrome=true&srcid=0BwhCYaYDn8EgN2M5MTkwM2EtNWFkZC00ZTI3LWFjZTUtNTFhZGZiYmUzODc1&hl=en
        - [ ] L - Liskov Substitution Principal | Base Class and Derived class follow ‘IS A’ principal
            - http://www.oodesign.com/liskov-s-substitution-principle.html
            - http://stackoverflow.com/questions/56860/what-is-the-liskov-substitution-principle
            - more flavor: http://docs.google.com/a/cleancoder.com/viewer?a=v&pid=explorer&chrome=true&srcid=0BwhCYaYDn8EgNzAzZjA5ZmItNjU3NS00MzQ5LTkwYjMtMDJhNDU5ZTM0MTlh&hl=en
        - [ ] I - Interface segregation principle | clients should not be forced to implement interfaces they don't use
            - http://www.oodesign.com/interface-segregation-principle.html
            - Interface Segregation Principle in 5 minutes: https://www.youtube.com/watch?v=3CtAfl7aXAQ
            - more flavor: http://docs.google.com/a/cleancoder.com/viewer?a=v&pid=explorer&chrome=true&srcid=0BwhCYaYDn8EgOTViYjJhYzMtMzYxMC00MzFjLWJjMzYtOGJiMDc5N2JkYmJi&hl=en
        - [ ] D - Dependency Inversion principle | Reduce the dependency In composition of objects.
            - http://www.oodesign.com/dependency-inversion-principle.html
            - http://stackoverflow.com/questions/62539/what-is-the-dependency-inversion-principle-and-why-is-it-important
            - more flavor: http://docs.google.com/a/cleancoder.com/viewer?a=v&pid=explorer&chrome=true&srcid=0BwhCYaYDn8EgMjdlMWIzNGUtZTQ0NC00ZjQ5LTkwYzQtZjRhMDRlNTQ3ZGMz&hl=en
    - [ ] Scalability:
        - [ ] Great overview: https://www.youtube.com/watch?v=-W9F__D3oY4
        - [ ] Short series: 
            - http://www.lecloud.net/post/7295452622/scalability-for-dummies-part-1-clones
            - http://www.lecloud.net/post/7994751381/scalability-for-dummies-part-2-database
            - http://www.lecloud.net/post/9246290032/scalability-for-dummies-part-3-cache
            - http://www.lecloud.net/post/9699762917/scalability-for-dummies-part-4-asynchronism
        - [ ] Scalable Web Architecture and Distributed Systems: http://www.aosabook.org/en/distsys.html
        - [ ] Fallacies of Distributed Computing Explained: https://pages.cs.wisc.edu/~zuyu/files/fallacies.pdf
        - [ ] Pragmatic Programming Techniques: http://horicky.blogspot.com/2010/10/scalable-system-design-patterns.html
            - extra: Google Pregel Graph Processing: http://horicky.blogspot.com/2010/07/google-pregel-graph-processing.html
        - [ ] Jeff Dean - Building Software Systems At Google and Lessons Learned: https://www.youtube.com/watch?v=modXC5IWTJI
        - [ ] Introduction to Architecting Systems for Scale: http://lethain.com/introduction-to-architecting-systems-for-scale/
        - [ ] Scaling mobile games to a global audience using App Engine and Cloud Datastore: https://www.youtube.com/watch?v=9nWyWwY2Onc
        - [ ] How Google Does Planet-Scale Engineering for Planet-Scale Infra: https://www.youtube.com/watch?v=H4vMcD7zKM0
        - [ ] The Importance of Algorithms: https://www.topcoder.com/community/data-science/data-science-tutorials/the-importance-of-algorithms/
        - [ ] Sharding: http://highscalability.com/blog/2009/8/6/an-unorthodox-approach-to-database-design-the-coming-of-the.html
        - [ ] Scale at Facebook (2009): https://www.infoq.com/presentations/Scale-at-Facebook
        - [ ] Scale at Facebook (2012), "Building for a Billion Users": https://www.youtube.com/watch?v=oodS71YtkGU
        - [ ] Engineering for the Long Game - Astrid Atkinson Keynote: https://www.youtube.com/watch?v=p0jGmgIrf_M&list=PLRXxvay_m8gqVlExPC5DG3TGWJTaBgqSA&index=4
        - [ ] 7 Years Of YouTube Scalability Lessons In 30 Minutes: http://highscalability.com/blog/2012/3/26/7-years-of-youtube-scalability-lessons-in-30-minutes.html
            - video: https://www.youtube.com/watch?v=G-lGCC4KKok
        - [ ] How PayPal Scaled To Billions Of Transactions Daily Using Just 8VMs: http://highscalability.com/blog/2016/8/15/how-paypal-scaled-to-billions-of-transactions-daily-using-ju.html
        - [ ] How to Remove Duplicates in Large Datasets: https://blog.clevertap.com/how-to-remove-duplicates-in-large-datasets/
        - [ ] A look inside Etsy's scale and engineering culture with Jon Cowie: https://www.youtube.com/watch?v=3vV4YiqKm1o
        - [ ] What Led Amazon to its Own Microservices Architecture: http://thenewstack.io/led-amazon-microservices-architecture/
        - [ ] To Compress Or Not To Compress, That Was Uber's Question: https://eng.uber.com/trip-data-squeeze/
        - [ ] Asyncio Tarantool Queue, Get In The Queue: http://highscalability.com/blog/2016/3/3/asyncio-tarantool-queue-get-in-the-queue.html
        - [ ] When Should Approximate Query Processing Be Used?: http://highscalability.com/blog/2016/2/25/when-should-approximate-query-processing-be-used.html
        - [ ] Google's Transition From Single Datacenter, To Failover, To A Native Multihomed Architecture: http://highscalability.com/blog/2016/2/23/googles-transition-from-single-datacenter-to-failover-to-a-n.html
        - [ ] Spanner: http://highscalability.com/blog/2012/9/24/google-spanners-most-surprising-revelation-nosql-is-out-and.html
        - [ ] Egnyte Architecture: Lessons Learned In Building And Scaling A Multi Petabyte Distributed System: http://highscalability.com/blog/2016/2/15/egnyte-architecture-lessons-learned-in-building-and-scaling.html
        - [ ] Machine Learning Driven Programming: A New Programming For A New World: http://highscalability.com/blog/2016/7/6/machine-learning-driven-programming-a-new-programming-for-a.html
        - [ ] The Image Optimization Technology That Serves Millions Of Requests Per Day: http://highscalability.com/blog/2016/6/15/the-image-optimization-technology-that-serves-millions-of-re.html
        - [ ] A Patreon Architecture Short: http://highscalability.com/blog/2016/2/1/a-patreon-architecture-short.html
        - [ ] Tinder: How Does One Of The Largest Recommendation Engines Decide Who You'll See Next?: http://highscalability.com/blog/2016/1/27/tinder-how-does-one-of-the-largest-recommendation-engines-de.html
        - [ ] Design Of A Modern Cache: http://highscalability.com/blog/2016/1/25/design-of-a-modern-cache.html
        - [ ] Live Video Streaming At Facebook Scale: http://highscalability.com/blog/2016/1/13/live-video-streaming-at-facebook-scale.html
        - [ ] A Beginner's Guide To Scaling To 11 Million+ Users On Amazon's AWS: http://highscalability.com/blog/2016/1/11/a-beginners-guide-to-scaling-to-11-million-users-on-amazons.html
        - [ ] How Does The Use Of Docker Effect Latency?: http://highscalability.com/blog/2015/12/16/how-does-the-use-of-docker-effect-latency.html
        - [ ] Does AMP Counter An Existential Threat To Google?: http://highscalability.com/blog/2015/12/14/does-amp-counter-an-existential-threat-to-google.html
        - [ ] A 360 Degree View Of The Entire Netflix Stack: http://highscalability.com/blog/2015/11/9/a-360-degree-view-of-the-entire-netflix-stack.html
        - [ ] Latency Is Everywhere And It Costs You Sales - How To Crush It: http://highscalability.com/latency-everywhere-and-it-costs-you-sales-how-crush-it
        - [ ] Serverless (very long, just need the gist): http://martinfowler.com/articles/serverless.html
        - [ ] What Powers Instagram: Hundreds of Instances, Dozens of Technologies: http://instagram-engineering.tumblr.com/post/13649370142/what-powers-instagram-hundreds-of-instances
        - [ ] Cinchcast Architecture - Producing 1,500 Hours Of Audio Every Day: http://highscalability.com/blog/2012/7/16/cinchcast-architecture-producing-1500-hours-of-audio-every-d.html
        - [ ] Justin.Tv's Live Video Broadcasting Architecture: http://highscalability.com/blog/2010/3/16/justintvs-live-video-broadcasting-architecture.html
        - [ ] Playfish's Social Gaming Architecture - 50 Million Monthly Users And Growing: http://highscalability.com/blog/2010/9/21/playfishs-social-gaming-architecture-50-million-monthly-user.html
        - [ ] TripAdvisor Architecture - 40M Visitors, 200M Dynamic Page Views, 30TB Data: http://highscalability.com/blog/2011/6/27/tripadvisor-architecture-40m-visitors-200m-dynamic-page-view.html
        - [ ] PlentyOfFish Architecture: http://highscalability.com/plentyoffish-architecture
        - [ ] Salesforce Architecture - How They Handle 1.3 Billion Transactions A Day: http://highscalability.com/blog/2013/9/23/salesforce-architecture-how-they-handle-13-billion-transacti.html
        - [ ] ESPN's Architecture At Scale - Operating At 100,000 Duh Nuh Nuhs Per Second: http://highscalability.com/blog/2013/11/4/espns-architecture-at-scale-operating-at-100000-duh-nuh-nuhs.html
        - [ ] See "Messaging, Serialization, and Queueing Systems" way below for info on some of the technologies that can glue services together
        - [ ] Twitter:
            - O'Reilly MySQL CE 2011: Jeremy Cole, "Big and Small Data at @Twitter": https://www.youtube.com/watch?v=5cKTP36HVgI
            - Timelines at Scale: https://www.infoq.com/presentations/Twitter-Timeline-Scalability
        - For even more, see "Mining Massive Datasets" video series in the Video Series section.
    - [ ] Practicing the system design process: Here are some ideas to try working through on paper, each with some documentation on how it was handled in the real world:
        - review: System Design from HiredInTech: http://www.hiredintech.com/system-design/
        - cheat sheet: https://github.com/jwasham/google-interview-university/blob/master/extras/cheat%20sheets/system-design.pdf
        - flow:
            1. Understand the problem and scope:
                - define the use cases, with interviewer's help
                - suggest additional features
                - remove items that interviewer deems out of scope
                - assume high availability is required, add as a use case
            2. Think about constraints:
                - ask how many requests per month
                - ask how many requests per second (they may volunteer it or make you do the math)
                - estimate reads vs. writes percentage
                - keep 80/20 rule in mind when estimating
                - how much data written per second
                - total storage required over 5 years
                - how much data read per second
            3. Abstract design:
                - layers (service, data, caching)
                - infrastructure: load balancing, messaging
                - rough overview of any key algorithm that drives the service
                - consider bottlenecks and determine solutions
        - Exercises:
            - Design a CDN network: old article: http://repository.cmu.edu/cgi/viewcontent.cgi?article=2112&context=compsci
            - Design a random unique ID generation system: https://blog.twitter.com/2010/announcing-snowflake
            - Design an online multiplayer card game: http://www.indieflashblog.com/how-to-create-an-asynchronous-multiplayer-game.html
            - Design a key-value database: http://www.slideshare.net/dvirsky/introduction-to-redis
            - Design a function to return the top k requests during past time interval: https://icmi.cs.ucsb.edu/research/tech_reports/reports/2005-23.pdf
            - Design a picture sharing system: http://highscalability.com/blog/2011/12/6/instagram-architecture-14-million-users-terabytes-of-photos.html
            - Design a recommendation system: http://ijcai13.org/files/tutorial_slides/td3.pdf
            - Design a URL-shortener system: copied from above: http://www.hiredintech.com/system-design/the-system-design-process/
            - Design a cache system: https://www.adayinthelifeof.nl/2011/02/06/memcache-internals/

- ### Unicode
    - [ ] The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets: http://www.joelonsoftware.com/articles/Unicode.html
    - [ ] What Every Programmer Absolutely, Positively Needs To Know About Encodings And Character Sets To Work With Text: http://kunststube.net/encoding

- ### Testing
    - To cover:
        - how unit testing works
        - what are mock objects
        - what is integration testing
        - what is dependency injection
    - [ ] Agile Software Testing with James Bach: https://www.youtube.com/watch?v=SAhJf36_u5U
    - [ ] Open Lecture by James Bach on Software Testing: https://www.youtube.com/watch?v=ILkT_HV9DVU
    - [ ] Steve Freeman - Test-Driven Development (that’s not what we meant): https://vimeo.com/83960706
        - slides: http://gotocon.com/dl/goto-berlin-2013/slides/SteveFreeman_TestDrivenDevelopmentThatsNotWhatWeMeant.pdf
    - [ ] TDD is dead. Long live testing.: http://david.heinemeierhansson.com/2014/tdd-is-dead-long-live-testing.html
    - [ ] Is TDD dead? https://www.youtube.com/watch?v=z9quxZsLcfo
    - [ ] Video series (152 videos) - not all are needed: https://www.youtube.com/watch?v=nzJapzxH_rE&list=PLAwxTw4SYaPkWVHeC_8aSIbSxE_NXI76g
    - [ ] Test-Driven Web Development with Python: http://www.obeythetestinggoat.com/pages/book.html#toc
    - [ ] Dependency injection:
        - [ ] https://www.youtube.com/watch?v=IKD2-MAkXyQ
        - [ ] http://jasonpolites.github.io/tao-of-testing/ch3-1.1.html
    - [ ] How to write tests: http://jasonpolites.github.io/tao-of-testing/ch4-1.1.html

- ### Design patterns
    - [ ] Quick UML review: https://www.youtube.com/watch?v=3cmzqZzwNDM&list=PLGLfVvz_LVvQ5G-LdJ8RLqe-ndo7QITYc&index=3
    - [ ] Learn these patterns:
        - [ ] strategy
        - [ ] singleton
        - [ ] adapter
        - [ ] prototype
        - [ ] decorator
        - [ ] visitor
        - [ ] factory, abstract factory
        - [ ] facade
        - [ ] observer
        - [ ] proxy
        - [ ] delegate
        - [ ] command
        - [ ] state
        - [ ] memento
        - [ ] iterator
        - [ ] composite
        - [ ] flyweight

### Books, when the interviews are close

**Read first:**
- [ ] Programming Interviews Exposed: Secrets to Landing Your Next Job, 2nd Edition:
    http://www.wiley.com/WileyCDA/WileyTitle/productCd-047012167X.html

**Read second (recommended by many, but not in Google coaching docs):**
- [ ] Cracking the Coding Interview, 6th Edition:
    - http://www.amazon.com/Cracking-Coding-Interview-6th-Programming/dp/0984782850/
    - If you see people reference "The Google Resume", it was a book replaced by "Cracking the Coding Interview".

## Coding exercises/challenges

Once you've learned your brains out, put those brains to work.
Take coding challenges every day, as many as you can.

- [ ] Great intro (copied from System Design section): Algorithm design: http://www.hiredintech.com/algorithm-design/
- [ ] How to Find a Solution: https://www.topcoder.com/community/data-science/data-science-tutorials/how-to-find-a-solution/
- [ ] How to Dissect a Topcoder Problem Statement: https://www.topcoder.com/community/data-science/data-science-tutorials/how-to-dissect-a-topcoder-problem-statement/ 
- [ ] Mathematics for Topcoders: https://www.topcoder.com/community/data-science/data-science-tutorials/mathematics-for-topcoders/
- [ ] Dynamic Programming – From Novice to Advanced: https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/

- https://courses.csail.mit.edu/iap/interview/materials.php
-http://www.javaprobs.com/problems-by-data-structure/linkedlist/
    - LeetCode: https://leetcode.com/
        - Solved: 1
    - Project Euler (math-focused): https://projecteuler.net/index.php?section=problems
    - Codility: https://codility.com/programmers/
    - InterviewCake: https://www.interviewcake.com/
    - InterviewBit: https://www.interviewbit.com/invite/icjf
    - Codewars: https://www.codewars.com/

    - Exercises for getting better at a given language: http://exercism.io/languages

## Once you're closer to the interview

- [ ] Cracking The Coding Interview Set 2:
    - https://www.youtube.com/watch?v=4NIb9l3imAo
    - https://www.youtube.com/watch?v=Eg5-tdAwclo
    - https://www.youtube.com/watch?v=1fqxMuPmGak

