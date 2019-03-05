from pprint import pprint as pp
import sys
import random
import math
from collections import defaultdict
#import numpy

class Tree:
    Tree_Num = 0
    def __init__(self,x,y,monkeys,thres):
        self.xaxis = x
        self.yaxis = y
        self.num_monkeys = monkeys
        self.threshold = thres
        Tree.Tree_Num += 1

    def print_tree_info(self):
        print("X: %d Y: %d Num_of_Monkeys: %d Threshold: %d Tree_Num: %d " % (self.xaxis, self.yaxis, self.num_monkeys, self.threshold, self.Tree_Num))


    def total_trees(self):
        return Tree.Tree_Num

    def monkey_jump(self, tree):
        # when monkey jump from self, reduce threshold and reduce number of monkeys remaining in the tree, increse number of monkeys on target
        self.threshold -= 1
        if self.threshold <= 0:
            self.__del__()
        self.num_monkeys -= 1
        tree.num_monkeys += 1

    def __del__(self):
        return True



def euclidean_distance(x1, y1, x2, y2,):
    distance = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    return distance

def can_jump(x1, y1, x2, y2, C):
    distance = euclidean_distance(x1, y1, x2, y2)
    if distance < C:
        #print("Distance :%d Jumping Capacity: %d" % (distance, C))
        return True
    else:
        return False



if __name__ == '__main__':
    input1 = input()
    N = int(input1.split()[0])
    C = float(input1.split()[1])

    trees = [[0]*1 for i in range(N)]
    total_monkeys = 0
    for i in range(N):
        input1 = input()
        x, y, m, t = input1.split()
        total_monkeys += int(m)
        trees[i] = Tree(int(x), int(y), int(m), int(t))
        #trees[i].print_tree_info() ## This will print information about Entered Trees

    #print("Total Monkeys: %d" % total_monkeys)
    count_of_weak_tree = [[0]*2 for i in range(N)]

    for i in range(N):
        if trees[i].num_monkeys > trees[i].threshold:
            count_of_weak_tree[i][0] += 1
            count_of_weak_tree[i][1] = i

    #pp(count_of_weak_tree)
    sum = [sum(x) for x in zip(*count_of_weak_tree)]
    #pp(sum)
    if sum[0] >= 2:
        print(-1)
        sys.exit()
    elif sum[0] == 1:
        #print(random.choice([-1, sum[1]]))
        print(sum[1])
    else:
        if all(trees[i].threshold >= total_monkeys for i in range(N)):
            # print numbers in order
            print(*range(N))
        else:
            #Actual Logic here
            #print(min(trees[i].threshold for i in range(N)))
            final_result = []
            for fl in range(N):
                # This is the loop of Trees to identify the tree can get all the monkeys
                if trees[fl].num_monkeys > trees[fl].threshold:
                    #print("Tree %d has less threshold than monkeys" % fl)
                    break
                edge = [[0]*4 for i in range(1)] # First elements will be 0
                reference_table = [] # Consumed Trees, don't need to refer again
                reference_table.append(fl)
                possible_to_jump = True
                for adj in range(N):
                    # This is to find the adjescent trees where the monkeys can jump from
                    if fl == adj or adj in reference_table:
                        continue
                    jump = can_jump(trees[adj].xaxis, trees[adj].yaxis, trees[fl].xaxis, trees[fl].yaxis, C)
                    if jump:
                        if trees[adj].num_monkeys > trees[adj].threshold:
                            #print("Tree %d has less threshold than monkeys" % adj)
                            possible_to_jump = False
                            break
                        edge.append([fl, adj, trees[adj].threshold, trees[adj].num_monkeys]) # Destination, source, source threshold
                        reference_table.append(adj)
                    #print("Reference table")
                    #pp(reference_table)
                    #print("Edge")
                    #pp(edge)
                #pp(edge)
                sum_of_thresholds = 0
                jumped_monkeys = 0
                for i in range(len(edge)):
                    sum_of_thresholds += (edge[i][2]-edge[i][3])
                    jumped_monkeys += edge[i][3]
                remaining_monkeys = (total_monkeys - jumped_monkeys - trees[fl].num_monkeys)
                if sum_of_thresholds < remaining_monkeys: # this should be remainig monkeys
                    possible_to_jump = False
                    continue
                else:
                    final_result.append(fl)
                    #print("Final result table")
                    #pp(final_result)
            # Finally print the results
            final_result = sorted(set(final_result))
            if len(final_result) == 0:
                print(-1)
            print(*final_result)