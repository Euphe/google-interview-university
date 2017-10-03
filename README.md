# Google Interview University

This is a fork of a study plan for going from web developer (self-taught, no CS degree) to Google (Google-level) software engineer.

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
    - [ ] http://alexbowe.com/failing-at-google-interviews/

## Algorithmic complexity / Big-O / Asymptotic analysis
- [x] A Gentle Introduction to Algorithm Complexity Analysis: http://discrete.gr/complexity/
- [x] TopCoder (includes recurrence relations and master theorem):
    - Computational Complexity: Section 2: https://www.topcoder.com/community/data-science/data-science-tutorials/computational-complexity-section-2/
- [x] Cheat sheet: http://bigocheatsheet.com/

## Additional knowledge
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

## Algorithms
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
- ### Trie
    - [x] Tries https://medium.com/algorithms/trie-prefix-tree-algorithm-ee7ab3fe3413
    - [x] Implement

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

- ### Sorting
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


- ### Graphs
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

- Read on:
    - [x] http://interactivepython.org/runestone/static/pythonds/Graphs/TopologicalSorting.html
    - [x] http://interactivepython.org/runestone/static/pythonds/Graphs/StronglyConnectedComponents.html
    - [x] http://interactivepython.org/runestone/static/pythonds/Graphs/ShortestPathProblems.html - Important
    - [x] http://interactivepython.org/runestone/static/pythonds/Graphs/PrimsSpanningTreeAlgorithm.html

- Implement:
    - [x] DFS with adjacency list (recursive)
    - [x] http://interactivepython.org/runestone/static/pythonds/Graphs/ImplementingKnightsTour.html - I am pretty sure code from here is wrong
    - [x] http://interactivepython.org/runestone/static/pythonds/Graphs/GeneralDepthFirstSearch.html

    - [x] BFS with adjacency list
        - [x] http://interactivepython.org/runestone/static/pythonds/Graphs/ImplementingBreadthFirstSearch.html
    - [x] http://interactivepython.org/runestone/static/pythonds/Graphs/DijkstrasAlgorithm.html
        - [x] http://techieme.in/shortest-path-using-dijkstras-algorithm/
        - [x] https://www-m9.ma.tum.de/graph-algorithms/spp-dijkstra/index_en.html
- Problems:
    - x] http://interactivepython.org/runestone/static/pythonds/Graphs/ProgrammingExercises.html

- ### Recursion
    - how is tail recursion better than not?
        - [x] https://www.quora.com/What-is-tail-recursion-Why-is-it-so-bad
 
- ### Dynamic Programming
    - [x] Intro https://www.codechef.com/wiki/tutorial-dynamic-programming
    - [x] http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
    - [x] https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/tutorial/
    - [x] Knapsack http://www.thelearningpoint.net/computer-science/algorithms-dynamic-programming---the-integer-knapsack-problem
    - [x] Longest common subsequence http://algorithms.tutorialhorizon.com/dynamic-programming-longest-common-subsequence/
    - [ ] REDO once more competent http://www.geeksforgeeks.org/dynamic-programming-set-12-longest-palindromic-subsequence/
    - [ ] REDO once more competent http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
    - [x] Coin change problem http://www.algorithmist.com/index.php/Coin_Change
    - [x] https://www.hackerrank.com/challenges/fibonacci-modified
    - [ ] Not really DP - https://www.hackerrank.com/challenges/stockmax
    - [ ] https://www.hackerrank.com/challenges/play-game
    - [ ] https://www.hackerrank.com/challenges/red-john-is-back
    - [ ] https://www.hackerrank.com/challenges/strplay
    - [ ] Began solving, got stuck. Inspect stolen solution in python file! https://www.hackerrank.com/challenges/equal
    - [ ] https://www.hackerearth.com/practice/notes/dynamic-programming-i-1/
    - [ ] Final read https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/
    - [ ] Loads of problems: http://www.geeksforgeeks.org/fundamentals-of-algorithms/#DynamicProgramming


- ### NP, NP-Complete and Approximation Algorithms
    - Know about the most famous classes of NP-complete problems, such as traveling salesman and the knapsack problem,
        and be able to recognize them when an interviewer asks you them in disguise.
    - Know what NP-complete means.
    - [x] http://stackoverflow.com/questions/1857244/what-are-the-differences-between-np-np-complete-and-np-hard/1857342#1857342
    - [x] http://stackoverflow.com/questions/1857244/what-are-the-differences-between-np-np-complete-and-np-hard/19510170#19510170
    - [x] https://www.quora.com/How-do-you-explain-NP-Complete-and-NP-hard-to-a-child

- ### Garbage collection
    - [x] GC in Python: https://www.quora.com/How-does-garbage-collection-in-Python-work

- ### Processes and Threads
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
        - [ ] Python GIL 
            - [x] https://softwareengineering.stackexchange.com/questions/186889/why-was-python-written-with-the-gil/186909#186909
            - [ ] https://wiki.python.org/moin/GlobalInterpreterLock
        - [ ] http://www.python-course.eu/threads.php


    Scalability and System Design are very large topics with many topics and resources, since there is a lot to consider 
    when designing a software/hardware system that can scale. Expect to spend quite a bit of time on this.

## System Design, Scalability, Data Handling
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
        
+ [ ] **START HERE**: System Design from HiredInTech: http://www.hiredintech.com/system-design/
+ [ ] https://www.quora.com/How-do-I-prepare-to-answer-design-questions-in-a-technical-interview?redirected_qid=1500023
+ [ ] 8 Things You Need to Know Before a System Design Interview: http://blog.gainlo.co/index.php/2015/10/22/8-things-you-need-to-know-before-system-design-interviews/
+ [ ] Algorithm design: http://www.hiredintech.com/algorithm-design/
+ [ ] Database Normalization - 1NF, 2NF, 3NF and 4NF
+ [ ] https://github.com/checkcheckzz/system-design-interview - There are a lot of resources in this one. Look through the articles and examples. I put some of them below.
+ [ ] How to ace a systems design interview: http://www.palantir.com/2011/10/how-to-rock-a-systems-design-interview/
+ [ ] Numbers Everyone Should Know: http://everythingisdata.wordpress.com/2009/10/17/numbers-everyone-should-know/
+ [ ] How long does it take to make a context switch?: http://blog.tsunanet.net/2010/11/how-long-does-it-take-to-make-context.html
+ [ ] Transactions Across Datacenters
+ [ ] A plain english introduction to CAP Theorem: http://ksat.me/a-plain-english-introduction-to-cap-theorem/
+ [ ] Paxos Consensus algorithm: 
    * short video: https://www.youtube.com/watch?v=s8JqcZtvnsM
    * paper: http://research.microsoft.com/en-us/um/people/lamport/pubs/paxos-simple.pdf
* [x] https://en.wikipedia.org/wiki/Object-oriented_programming
* [x] https://tproger.ru/translations/oop-principles-cheatsheet/
* [x] SOLID OOP Principles:
    * [x] https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design
    * [x] https://habrahabr.ru/post/83269/
    * [x] http://makedev.org/principles/solid/isp.html
    * [x] http://makedev.org/principles/solid/dip.html
* [ ] Additional on solid:
    * [ ] http://www.oodesign.com/single-responsibility-principle.html
    * [ ] http://www.oodesign.com/open-close-principle.html
    * [ ] http://www.oodesign.com/liskov-s-substitution-principle.html
    * [ ] http://www.oodesign.com/interface-segregation-principle.html
    * [ ] http://www.oodesign.com/dependency-inversion-principle.html
* [x] http://codebetter.com/raymondlewallen/2005/07/19/4-major-principles-of-object-oriented-programming/
* [x] https://habrahabr.ru/post/87205/
* [x] OOP in Python:
    * [x] http://interactivepython.org/runestone/static/thinkcspy/ClassesBasics/toctree.html
    * [x] http://interactivepython.org/runestone/static/thinkcspy/ClassesDiggingDeeper/toctree.html
    * [x] On abstract classes https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
* [x] DRY 
* [x] KISS
* [x] YAGNI
* [x] Общие советы http://makedev.org/principles/general.html
* [ ] Scalability:
    * [ ] Short series: 
        * http://www.lecloud.net/post/7295452622/scalability-for-dummies-part-1-clones
        * http://www.lecloud.net/post/7994751381/scalability-for-dummies-part-2-database
        * http://www.lecloud.net/post/9246290032/scalability-for-dummies-part-3-cache
        * http://www.lecloud.net/post/9699762917/scalability-for-dummies-part-4-asynchronism
    * [ ] Scalable Web Architecture and Distributed Systems: http://www.aosabook.org/en/distsys.html
    * [ ] Fallacies of Distributed Computing Explained: https://pages.cs.wisc.edu/~zuyu/files/fallacies.pdf
    * [ ] Pragmatic Programming Techniques: http://horicky.blogspot.com/2010/10/scalable-system-design-patterns.html
        * extra: Google Pregel Graph Processing: http://horicky.blogspot.com/2010/07/google-pregel-graph-processing.html
    * [ ] Introduction to Architecting Systems for Scale: http://lethain.com/introduction-to-architecting-systems-for-scale/
    * [ ] Twitter:
        * Timelines at Scale: https://www.infoq.com/presentations/Twitter-Timeline-Scalability
    * For even more, see "Mining Massive Datasets" video series in the Video Series section.
* [ ] Practicing the system design process: Here are some ideas to try working through on paper, each with some documentation on how it was handled in the real world:
    * review: System Design from HiredInTech: http://www.hiredintech.com/system-design/
    * cheat sheet: https://github.com/jwasham/google-interview-university/blob/master/extras/cheat%20sheets/system-design.pdf
    * flow:
        1. Understand the problem and scope:
            * define the use cases, with interviewer's help
            * suggest additional features
            * remove items that interviewer deems out of scope
            * assume high availability is required, add as a use case
        2. Think about constraints:
            * ask how many requests per month
            * ask how many requests per second (they may volunteer it or make you do the math)
            * estimate reads vs. writes percentage
            * keep 80/20 rule in mind when estimating
            * how much data written per second
            * total storage required over 5 years
            * how much data read per second
        3. Abstract design:
            * layers (service, data, caching)
            * infrastructure: load balancing, messaging
            * rough overview of any key algorithm that drives the service
            * consider bottlenecks and determine solutions
    * Exercises:
        * Design a CDN network: old article: http://repository.cmu.edu/cgi/viewcontent.cgi?article=2112&context=compsci
        * Design a random unique ID generation system: https://blog.twitter.com/2010/announcing-snowflake
        * Design an online multiplayer card game: http://www.indieflashblog.com/how-to-create-an-asynchronous-multiplayer-game.html
        * Design a key-value database: http://www.slideshare.net/dvirsky/introduction-to-redis
        * Design a function to return the top k requests during past time interval: https://icmi.cs.ucsb.edu/research/tech_reports/reports/2005-23.pdf
        * Design a picture sharing system: http://highscalability.com/blog/2011/12/6/instagram-architecture-14-million-users-terabytes-of-photos.html
        * Design a recommendation system: http://ijcai13.org/files/tutorial_slides/td3.pdf
        * Design a URL-shortener system: copied from above: http://www.hiredintech.com/system-design/the-system-design-process/
        * Design a cache system: https://www.adayinthelifeof.nl/2011/02/06/memcache-internals/

## Unicode
- [x] The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets: http://www.joelonsoftware.com/articles/Unicode.html
- [x] What Every Programmer Absolutely, Positively Needs To Know About Encodings And Character Sets To Work With Text http://kunststube.net/encoding/

## Testing
- To cover:
    - how unit testing works
    - what are mock objects
    - what is integration testing
    - what is dependency injection
- [ ] Steve Freeman - Test-Driven Development (that’s not what we meant): https://vimeo.com/83960706
    - slides: http://gotocon.com/dl/goto-berlin-2013/slides/SteveFreeman_TestDrivenDevelopmentThatsNotWhatWeMeant.pdf
- [ ] TDD is dead. Long live testing.: http://david.heinemeierhansson.com/2014/tdd-is-dead-long-live-testing.htmlg
- [ ] Test-Driven Web Development with Python: http://www.obeythetestinggoat.com/pages/book.html#toc
- [ ] Dependency injection:
    - [ ] http://jasonpolites.github.io/tao-of-testing/ch3-1.1.html
- [ ] How to write tests: http://jasonpolites.github.io/tao-of-testing/ch4-1.1.html
+ [x] Debug
    + [x] http://interactivepython.org/runestone/static/thinkcspy/Debugging/toctree.html


## Design patterns
- [x] https://sourcemaking.com/design_patterns
- [x] Learn these patterns:
    - [x] builder 
        - [x] https://github.com/faif/python-patterns/blob/master/creational/builder.py 
        - [x] https://sourcemaking.com/design_patterns/builder
        - [x] https://stackoverflow.com/questions/5788240/when-should-i-use-builder-design-pattern
    - [x] strategy https://sourcemaking.com/design_patterns/strategy
    - [x] singleton https://sourcemaking.com/design_patterns/singleton/python/1
    - [x] adapter https://sourcemaking.com/design_patterns/adapter
    - [x] decorator 
    - [x] visitor
    - [x] factory, abstract factory https://sourcemaking.com/design_patterns/abstract_factory
    - [x] bridge - need to rehearse
        - [x] http://www.tutorialspoint.com/design_pattern/bridge_pattern.htm
        - [x] https://gist.github.com/pazdera/1173009
        - [x] https://sourcemaking.com/design_patterns/bridge
    - [x] facade
    - [x] observer https://sourcemaking.com/design_patterns/observer
    - [x] command https://sourcemaking.com/design_patterns/command
    - [x] state https://sourcemaking.com/design_patterns/state
    - [x] memento https://sourcemaking.com/design_patterns/memento
    - [x] iterator https://sourcemaking.com/design_patterns/iterator
    - [x] composite
- [x] Good overview of different python features and some design patterns https://www.toptal.com/python/python-design-patterns
- [ ] https://github.com/faif/python-patterns
- [x] http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PatternConcept.html
- MVC
    - [x] http://reinout.vanrees.org/weblog/2011/12/13/django-mvc-explanation.html
    - [x] http://djangobook.com/model-view-controller-design-pattern/
    - [x] https://docs.djangoproject.com/en/1.11/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names

## SQL
- [ ] https://community.modeanalytics.com/sql/tutorial/introduction-to-sql/
- https://sqlbolt.com/
    - [x] SELECT
    - [ ] Update
    - [ ] Insert
    - [ ] Create, Alter, Drop table
    - [ ] Subquery
    - [ ] Union, intersection

## MSSQL
- [ ] https://docs.microsoft.com/en-us/sql/relational-databases/databases/contained-databases
- [ ] https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-database-user
- [x] https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-login
- [x] https://docs.microsoft.com/en-us/sql/relational-databases/databases/databases
- [x] User-Schema separation https://msdn.microsoft.com/en-us/library/ms190387(v=sql.105).aspx
- [x] https://msdn.microsoft.com/en-us/library/aa337545(v=sql.105).aspx
- [ ] https://msdn.microsoft.com/en-us/library/dd207005(v=sql.105).aspx
- [ ] https://msdn.microsoft.com/en-us/library/aa337562(v=sql.105).aspx


## Python 
- [ ] Metaclasses, with django ORM example https://habrahabr.ru/post/145835/
- [ ] How web works introduction, continues on web sockets and async http://mrjoes.github.io/2013/06/21/python-realtime.html
- [x] solve all : http://pyobject.ru/blog/2010/02/04/python-quiz/
    - Solutions 1 https://habrahabr.ru/post/145369/
    - Solutions 2 https://habrahabr.ru/post/147783/
    - [x] data types, etc
    - [x] functions
    - [x] iterators
    - [x] modules
    - [x] classes
    - [x] metaclasses and descriptors
- [x] https://habrahabr.ru/post/50026/
- [ ] https://habrahabr.ru/post/132554/
- [ ] I dont understand at all, I need some pipe prequesites http://www.python-course.eu/pipes.php
- [x] http://www.python-course.eu/sys_module.php
- [x] http://www.python-course.eu/exception_handling.php
- [x] https://habrahabr.ru/post/193890/


_*Currently here*_
## Golang
- Tour of Go
    - [x] Basics
    - [ ] Methods and interfaces - currently covered up to readers
    - [ ] Concurrency
- https://gobyexample.com/
- Exercism tasks http://exercism.io/languages/go/about

## Javascript
- Core JS - Estimated completition time: 3 days.
    - [ ] rehearse lang basics https://javascript.info/
    - [x] https://javascript.info/async
    - [ ] Great stuff on promises! https://pouchdb.com/2015/05/18/we-have-a-problem-with-promises.html
    
- VueJS 
    - https://vuejs.org/v2/guide/
        - [x] Essentials
        - [ ] Transitions
        - [ ] Reusability and composition
        - [ ] Tooling

- NodeJS
    - [x] https://docs.nodejitsu.com/articles/file-system/how-to-read-files-in-nodejs/

    - npm
        - [x] https://docs.npmjs.com/files/package.json
        - [x] https://docs.npmjs.com/misc/scripts
        - [x] https://docs.npmjs.com/misc/config
        
- Testing
    - Mocha
        - [ ] https://mochajs.org/#asynchronous-code
        
## Typescript
- http://www.typescriptlang.org/docs/handbook/interfaces.html#toc-handbook
    - [x] http://www.typescriptlang.org/docs/handbook/basic-types.html
    - [x] http://www.typescriptlang.org/docs/handbook/variable-declarations.html
    - [x] http://www.typescriptlang.org/docs/handbook/interfaces.html
    - [ ] Read up to Advanced techniques - http://www.typescriptlang.org/docs/handbook/classes.html
    - [x] https://www.typescriptlang.org/docs/handbook/generics.html
        - [x] https://templecoding.com/blog/2016/03/17/leveraging-the-power-of-generics-with-typescript/
    - [ ] Read about half of it https://www.typescriptlang.org/docs/handbook/advanced-types.html
    - [x] https://www.typescriptlang.org/docs/handbook/iterators-and-generators.html
    - [ ] https://www.typescriptlang.org/docs/handbook/modules.html


## Devops

### RabbitMQ
- [x] http://www.rabbitmq.com/tutorials/tutorial-three-javascript.html
- [x] http://www.rabbitmq.com/tutorials/tutorial-four-javascript.html
- [x] http://www.rabbitmq.com/tutorials/tutorial-five-javascript.html
- [x] https://facundoolano.wordpress.com/2016/06/26/real-world-rpc-with-rabbitmq-and-node-js/

### Docker
- [x] Overview http://elliot.land/post/docker-explained-simply

### Ansible 
- [x] Overview https://www.ansible.com/how-ansible-works
- [x] http://docs.ansible.com/ansible/latest/intro_getting_started.html
- [x] http://docs.ansible.com/ansible/latest/intro_inventory.html
- [x] http://docs.ansible.com/ansible/latest/intro_adhoc.html
- [x] http://docs.ansible.com/ansible/latest/playbooks_variables.html
- http://docs.ansible.com/ansible/latest/playbooks.html
    - [x] http://docs.ansible.com/ansible/latest/playbooks_intro.html
    - [ ] http://docs.ansible.com/ansible/latest/playbooks_reuse.html
        - [x] http://docs.ansible.com/ansible/latest/playbooks_reuse_includes.html
        - [x] http://docs.ansible.com/ansible/latest/playbooks_reuse_roles.html
    - [ ] http://docs.ansible.com/ansible/latest/playbooks_best_practices.html

- Extras:
    - [ ] http://docs.ansible.com/ansible/latest/playbooks_templating.html
    - [ ] http://docs.ansible.com/ansible/latest/playbooks_conditionals.html
    - [ ] http://docs.ansible.com/ansible/latest/playbooks_loops.html

### Linux
- Apt 
	- [x] https://wiki.debian.org/Apt
    - [x] Ubuntu https://help.ubuntu.com/community/AptGet/Howto#auto-apt
    - [x] https://wiki.debian.org/AptCLI
- dpkg
	- [ ] https://wiki.debian.org/DebianPackageManagement
- [ ] Tar https://www.computerhope.com/unix/utar.htm
- [ ] Cat http://www.linfo.org/cat.html

### Guides from the frontlines
- [x] Setup gitlab using ansible and docker image https://www.djouxtech.net/posts/gitlab-installation-with-ansible-and-docker/
    - A well-written guide, explains all steps and settings
    - Good ansible playbook organization
- [x] Understand your azure spending https://www.petri.com/understand-your-microsoft-azure-spending

## Meta 
- [ ] Improving my code quality
    - [ ] https://sourcemaking.com/antipatterns
    - [ ] https://sourcemaking.com/refactoring

- [ ] Improving system architecture quality
    - [ ] https://sourcemaking.com/antipatterns/software-architecture-antipatterns

- [ ] Improving my work ethic and approaches
    - [ ] https://sourcemaking.com/antipatterns/software-project-management-antipatterns


### Books, in-depth
- [ ] Python
    - [ ] http://python-3-patterns-idioms-test.readthedocs.io/en/latest/index.html

## When interviews are close 

### Books, when the interviews are close
**Read first:**
- [ ] Programming Interviews Exposed: Secrets to Landing Your Next Job, 2nd Edition:
    http://www.wiley.com/WileyCDA/WileyTitle/productCd-047012167X.html

**Read second (recommended by many, but not in Google coaching docs):**
- [ ] Cracking the Coding Interview, 6th Edition:
    - http://www.amazon.com/Cracking-Coding-Interview-6th-Programming/dp/0984782850/
    - If you see people reference "The Google Resume", it was a book replaced by "Cracking the Coding Interview".

## Misc interview questions prep
Where you will be in 5 years and other stuff
- [ ] Not a lot of detail, but a broad range of topics http://www.programmerinterview.com


## Coding exercises/challenges
Once you've learned your brains out, put those brains to work.
Take coding challenges every day, as many as you can.
- [x] Great intro (copied from System Design section): Algorithm design: http://www.hiredintech.com/algorithm-design/
- http://www.javaprobs.com/
- http://algorithms.tutorialhorizon.com/
- LeetCode: https://leetcode.com/
- Project Euler (math-focused): https://projecteuler.net/index.php?section=problems
- Codility: https://codility.com/programmers/
- InterviewCake: https://www.interviewcake.com/
- InterviewBit: https://www.interviewbit.com/invite/icjf
- Codewars: https://www.codewars.com/
- Exercises for getting better at a given language: http://exercism.io/languages
## Other:
- [ ] http://www.codefool.org/wiki_165/index.php?title=Google_Interview_Questions - primarily use as a source of topics to study
- [x] http://haseebq.com/my-ten-rules-for-negotiating-a-job-offer/
- [x] http://haseebq.com/how-not-to-bomb-your-offer-negotiation/
