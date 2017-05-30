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
- [ ] Statistics basics
- [ ] Linear algebra basics
- [ ] Trigonometry basics
- [ ] Calculus basics

## Data Structures
- Good info source: https://courses.cs.washington.edu/courses/cse326/00wi/handouts.html
- 
- ### Arrays
    - [x] Description:
        - Arrays: https://en.wikipedia.org/wiki/Array_data_structure
        - 
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
- Tad bit more advanced (but the best of three) http://interactivepython.org/runestone/static/pythonds/index.html

- ### Endianness
    - [x] https://www.cs.umd.edu/class/sum2003/cmsc311/Notes/Data/endian.html

- ### Binary search
    - [x] https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search
    - [x] Implement:
        - binary search using recursion
## Trees
- ### Trees - Notes & Background
    - [x] http://interactivepython.org/runestone/static/pythonds/Trees/toctree.html
    - [x] basic tree construction
    - [x] traversal
    - DFS (depth-first search)
        - notes:
            time complexity: O(n)
            space complexity:
                best: O(log n) - avg. height of tree
                worst: O(n)
        - [x] inorder (DFS: left, self, right)
        - [x] postorder (DFS: left, right, self)
        - [x] preorder (DFS: self, left, right)

_*Currently here*_
- ### Prefix tree
    - [ ] Prefix trees
    - [ ] Implement

- ### Trie
    - [ ] Tries
    - [ ] Implement

- ### Binary search trees: BSTs
	- [x] http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html
    - [x] Implement:
        - [x] insert    // insert value into tree
        - [x] get_node_count // get count of values stored
        - [x] print_values // prints the values in the tree, from min to max
        - [x] delete_tree
        - [x] is_in_tree // returns true if given value exists in the tree
        - [x] delete_value
        - [x] get_successor // returns next-highest value in tree after given value


- ### Heap / Priority Queue / Binary Heap
    - visualized as a tree, but is usually linear in storage (array, linked list)
    - [x] http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html
    - [x] Implement a min-heap:
        - [x] MinHeap() creates a new, empty, binary heap.
		- [x] put(k) adds a new item to the heap.
		- [x] find_min() returns the item with the minimum key value, leaving item in the heap.
		- [x] del_min() returns the item with the minimum key value, removing the item from the heap.
		- [x] is_empty() returns true if the heap is empty, false otherwise.
		- [x] __len__() returns the number of items in the heap.
		- [x] _from_list(list) builds a new heap from a list of keys.
        - [x] heap_sort() - take an unsorted array and turn it into a sorted array in-place using a min heap - not implement, just read

- ### Balanced search trees
    - Know least one type of balanced binary tree (and know how it's implemented):
    - [x] Red/black trees - just read on them

## Sorting
- [x] stability in sorting algorithms ("Is Quicksort stable?")
    - https://en.wikipedia.org/wiki/Sorting_algorithm#Stability
    - http://stackoverflow.com/questions/1517793/stability-in-sorting-algorithms
    
- For heapsort, see Heap data structure above. Heap sort is great, but not stable.
- [x] http://interactivepython.org/runestone/static/pythonds/SortSearch/toctree.html
	- [x] Bubble sort - no need to implement
	- [x] Selection sort - no need to implement
	- [x] Insertion sort - no need to implement
	- [x] Merge sort - implement
	- [x] Quick sort - implement


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


- [x] Graphs (review and more):
    - [x] http://interactivepython.org/runestone/static/pythonds/Graphs/toctree.html
    - [x] https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs

Read on:
    - [x] http://interactivepython.org/runestone/static/pythonds/Graphs/TopologicalSorting.html
    - [x] http://interactivepython.org/runestone/static/pythonds/Graphs/StronglyConnectedComponents.html
    - [X] http://interactivepython.org/runestone/static/pythonds/Graphs/ShortestPathProblems.html - Important
    - [X] http://interactivepython.org/runestone/static/pythonds/Graphs/PrimsSpanningTreeAlgorithm.html

- I'll implement:
    - [x] DFS with adjacency list (recursive)
    - [x] http://interactivepython.org/runestone/static/pythonds/Graphs/ImplementingKnightsTour.html - I am pretty sure code from here is wrong
    - [x] http://interactivepython.org/runestone/static/pythonds/Graphs/GeneralDepthFirstSearch.html

    - [x] BFS with adjacency list
        - [x] http://interactivepython.org/runestone/static/pythonds/Graphs/ImplementingBreadthFirstSearch.html
    - [x http://interactivepython.org/runestone/static/pythonds/Graphs/DijkstrasAlgorithm.html
        - [x] http://techieme.in/shortest-path-using-dijkstras-algorithm/
        - [x] https://www-m9.ma.tum.de/graph-algorithms/spp-dijkstra/index_en.html
- Problems:
    - [ ] http://interactivepython.org/runestone/static/pythonds/Graphs/ProgrammingExercises.html

## Even More Knowledge
- ### Recursion
    - how is tail recursion better than not?
        - [x] https://www.quora.com/What-is-tail-recursion-Why-is-it-so-bad
 
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

- ### System Design
    - [ ] https://www.hiredintech.com/classrooms/system-design/lesson/52
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

- ### SQL
    - [ ] https://community.modeanalytics.com/sql/tutorial/introduction-to-sql/

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
- [x] Great intro (copied from System Design section): Algorithm design: http://www.hiredintech.com/algorithm-design/
- [ ] Mathematics for Topcoders: https://www.topcoder.com/community/data-science/data-science-tutorials/mathematics-for-topcoders/
- [ ] Dynamic Programming – From Novice to Advanced: https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/

    - http://www.javaprobs.com/
    - http://algorithms.tutorialhorizon.com/
    - LeetCode: https://leetcode.com/
        - Solved: 1
    - Project Euler (math-focused): https://projecteuler.net/index.php?section=problems
    - Codility: https://codility.com/programmers/
    - InterviewCake: https://www.interviewcake.com/
    - InterviewBit: https://www.interviewbit.com/invite/icjf
    - Codewars: https://www.codewars.com/

    - Exercises for getting better at a given language: http://exercism.io/languages
## Other:
    - [ ] http://www.codefool.org/wiki_165/index.php?title=Google_Interview_Questions - primarily use as a source of topics to study

## Once you're closer to the interview
- [ ] http://haseebq.com/my-ten-rules-for-negotiating-a-job-offer/
- [ ] http://haseebq.com/how-not-to-bomb-your-offer-negotiation/
- [ ] Cracking The Coding Interview Set 2:
    - https://www.youtube.com/watch?v=4NIb9l3imAo
    - https://www.youtube.com/watch?v=Eg5-tdAwclo
    - https://www.youtube.com/watch?v=1fqxMuPmGak

