# Creating Community Small Groups
A work by: Cypress Payne and Zachary Himes

## Description

Our task and project were to develop and create an algorithm that was able to when given a group of people, able to sort that group into equal groups of a size given by the user. The restrictions for the groups were as follows: Must be as evenly distributed as possible, there should be a host for each group, Married couples must always remain in the same group, and everyone should visit everyone else's house (Everyone needs to host everyone else at least once). We utilized Python to implement this algorithm, as it had a nice array of graph libraries we would be able to use to assist, us in both the implementation and display of the algorithm.

## Requirements

Our Program is running through the Python interpreter: _Python 3.9_. We used a couple of libraries to assist us in creating a graphical representation of the relationship/visualization of the problem. First, we used a library in Python called iGraph. iGraph is a library collection for creating and manipulating graphs and analyzing the network. We also utilize a library known as cairocffin which is a 2D vector graphics library with support for multiple backends including image buffers, PNG, PostScript, PDF, and SVG file output. Finally, we imported the os library which simply assists with the inputting, outputting, and manipulating text files.

## User Manual
Once the repository has been cloned to your computer, you should have a folder containing main.py, requirements.txt, group1.txt, group2.txt, and group3.txt, as well as output example files that are not necessary to run the program. This program requires a python 3 interpreter. Once your interpreter is open, you can load the necessary libraries noted in the requirements.txt file.

If you are running the program in a command shell, then once you have opened the file in your shell you can run the command pip3 install -r requirements.txt to ensure you have all required libraries.
Then the program can be run with the command python3 main.py. The program will then provide instructions and prompt you to enter a text file (group1.txt, group2.txt, or group3.txt can be used), and a number for the groups before running the algorithm and outputting your results. These results can then be found in a text file in the program folder.
For an example of the program running, see https://youtu.be/G1xuVAUDwLE

## Reflection
There were many ways to go about this problem. First, we began on paper thinking of ways we could effectively iterate and "remember" certain things after each iteration. When investigating libraries that could be used to implement a graph in Python we came across the iGraph library. This library not only allows us to easily create nodes and edges but it allows us to assign attributes to each node. The attributes of the library act much like that of an object in C++ or any other object-oriented language.

After figuring out how we might be able to label these nodes, we next needed to determine what pieces of information would be useful to store to effectively iterate through the graph and make proper group assignments based on the requirements. The requirements included: "going to a small group with every other member", "everyone to have a chance to visit everyone else’s home" and finally "They would like married couples to always go together to the same group".  After discussing the requirements we then came up with the user attributes to assign to each node.

The attributes we decided on were: "Name" and "Weight". Name is simply a string label for the node to represent the name of the individual represented by that node. Weight is the number of people, it accounts for couples weighing 2 or singles with a weight of 1.

Finally, we started working on our algorithm. We went with a greedy approach, in that it iterates through the queue of all the names then pops and chooses the first eligible (weight < group size) person or persons(couple) to assign to the group. Then assigns the directed edge to that node, which represents that they went to the house. This loops until everyone has hosted as well as everyone having visited one another's house.

I believe we were able to avoid a lot of extended difficulties. Cypress and I had great communication, and most of our time was spent in the outlining and planning phase, which created an organized and straightforward implementation of the algorithm we had planned and fine-tuned on paper. As for some struggles we had as the implementation began, the restrictions state everyone must visit all houses, and couples needing to attend together. So in the case that there are two couples in a group, they must both visit and host each other. If the group size is 3 that will make it impossible for the couples to visit each other, so we made the design decision to make it mandatory for the group size to be greater than 3 and then less than group size/2 (which would make some group sizes == 1).

Our solution is not the optimum solution to this problem. We narrowed it down to a couple of bottlenecks that would need to be improved in order to gain better time complexity. Overall our Algorithm ran at O(n^2). This was due to the way we decided to store our information, which was a list of lists. To iterate and print the list of lists this involves a nest for loop which results in the O(n^2) time complexity. With some research, a better way to store our information for better access would be to merge the lists into one list of strings, which with some analysis prints 2-4x faster. In Python, the time complexity to concatenate two lists is O(n + m) with n and m being the length of the two lists.

## Results
