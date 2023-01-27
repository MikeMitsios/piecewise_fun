# piecewise_fun


Design Choices

This project was constructed in 2 classes. First of all, we have our main class the PiecewiseFunction class. But in order to construct such a function we need the pieces of this function. The class PieceFunction was developed for those purposes. A PieceFunction is a function with its domain. For the range of the domain, it is available to leave out the edges. This can be done by defining the appropriate boolean inside the equal tuple. Many PieceFunctions construct a PIecewiseFunction. 

The PieceFunction is capable to handle both types of functions made of constant and linear functions at the same time. 

In order to achieve this I used a string to represent the general formula of the function. In this way, the project can be extended to create piecewise functions from more complex ones. Also, I personally believe that is the best way for a user to handle functions. I thought of having only the first and the last points of the PieceFunction but this wouldn't be practical. It's more expressive and clear to give as input the type/formula of the function rather than finding the edges of the function and giving those points one by one.

I used a custom regex in order to allow specific characters (and x as the only parameter). This part can be developed more but the eval function itself is capable of recognizing wrong syntax or unbalanced brackets.
The PiecewiseFunction is actually a list of many PieceFunctions. The function_list is private but it is fully accessible through the methods. Someone can view/plot the function, modify it (remove/add a PieceFunction) and find the min/max of it. Because the function can be modified someone can initialize an empty PiecewiseFunction object. Because the function is dynamic I preferred to find every time which is the min/max value. This part could also be improved by having the min/max modified only in cases where the function is created or modified (add/remove an element)

There are custom exceptions that handle wrong type arguments, limit values, check indexes to have the correct form, and keep the domains of each PieceFunction clear, with no overlappings. 

Each time a PiecewiseFunction has been created the items inside are sorted based on the start and end of each PieceFunction. Also when an item is added the function searches for its position if it is available.

Because the functions are presorted the evaluation uses a binary search in order to find the correct domain that x belongs to.

Finally, I created a random function in order to produce many PiecewiseFunctions for the timing tests. Where the more the PieceFunction inside a PiecewiseFunction are, the more time it takes to create the function itself and find the min/max of it. The evaluation instead of some spikes is done very fast overall (0 nanosec).

