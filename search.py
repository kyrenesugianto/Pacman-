# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    visited = set()  # Set to keep track of visited states
    stack = [(problem.getStartState(), [])]  # Stack for DFS with path

    while stack:
        state, actions = stack.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)
            successors = problem.getSuccessors(state)
            for next_state, action, _ in successors:
                if next_state not in visited:
                    stack.append((next_state, actions + [action]))

    return []  # Return an empty list if no path is found

    "util.raiseNotDefined()"

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # Initialize a queue to store nodes
    queue = util.Queue()
    # Initialize a set to track visited states
    visited = set()
    # Push initial state to queue
    queue.push((problem.getStartState(), [], 1))
    
    while not queue.isEmpty():
        state, actions, _ = queue.pop()

        # Goal check
        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)
            successors = problem.getSuccessors(state)
            for successor_state, action, _ in successors:
                if successor_state not in visited:
                    new_actions = actions + [action]
                    queue.push((successor_state, new_actions, 1))

    return []  # Return an empty list if no path is found

    "util.raiseNotDefined()"

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # create fringe to store nodes
    fringe = util.PriorityQueue()
    # track visited nodes
    visited = set()
    # push initial state to fringe
    fringe.push((problem.getStartState(), [], 0), 0)

    while not fringe.isEmpty():
        node = fringe.pop()
        state, actions, cost = node

        # goal check
        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)
            # visit child nodes
            successors = problem.getSuccessors(state)
            for child in successors:
                # store state, action and cost
                child_state, child_action, step_cost = child
                if child_state not in visited:
                    # add child nodes
                    child_actions = actions + [child_action]
                    total_cost = cost + step_cost
                    fringe.push((child_state, child_actions, total_cost), total_cost)

    return []  # Return an empty list if no path is found
    
    "util.raiseNotDefined()"

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    fringe = util.PriorityQueue()  # PriorityQueue to store nodes
    visited = set()  # Set to track visited nodes

    # Push initial state to fringe with priority based on cost and heuristic
    initial_state = problem.getStartState()
    initial_actions = []
    initial_priority = 0 + heuristic(initial_state, problem)
    fringe.push((initial_state, initial_actions, 0), initial_priority)

    while not fringe.isEmpty():
        state, actions, cost = fringe.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            successors = problem.getSuccessors(state)
            for next_state, action, step_cost in successors:
                if next_state not in visited:
                    new_actions = actions + [action]
                    new_cost = cost + step_cost
                    priority = new_cost + heuristic(next_state, problem)
                    fringe.push((next_state, new_actions, new_cost), priority)

    return []  # Return an empty list if no path is found

   
    "util.raiseNotDefined()"


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
