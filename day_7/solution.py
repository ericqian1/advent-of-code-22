# Global to catch so we only have to traverse one time
global sum_vals
sum_vals = []

global min_candidates
min_candidates = []

class Directory:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = {}
        self.files = {}
        self.file_size = 0
        self.dir_size = 0
        self.total_size = 0

    def compute_file_size(self):
        self.file_size = 0
        for file, size in self.files.items():
            self.file_size += size
    
    def compute_dir_size(self):
        self.dir_size = 0
        for child, node in self.children.items():
            self.dir_size += node.compute_total_size()

    def compute_total_size(self):
        
        global min_cutoff 
        min_cutoff = 43629016

        self.compute_file_size()
        self.compute_dir_size()
        self.total_size = self.dir_size + self.file_size
        # Catch the values here
        if self.total_size <= 100000:
            sum_vals.append(self.total_size)
        if self.total_size >= 3629016:
            min_candidates.append(self.total_size)

        return self.total_size


# Part 1: Build tree
with open("data.txt") as f:
    root = Directory()
    curr_node = root 
    for line in f.readlines():
        line = line.strip("\n").strip("\t")
        splits = line.split(" ")
        if splits[0]=="$":
            if splits[1]=="cd":
                if splits[2]=="/":
                    curr_node = root
                elif splits[2]=="..":
                    curr_node = curr_node.parent 
                else:
                    curr_node.children[splits[2]] = Directory(curr_node)
                    curr_node = curr_node.children[splits[2]]

        else:
            try:
                curr_node.files[splits[1]] = int(splits[0])
            except:
                pass

# Breadth
root.compute_total_size()

# We caught it in the recursion with a global variable
sum(sum_vals)

# Part 2: This part is easier
total_space = 70000000
root_space = 43629016
required_space = 30000000
unused_space = total_space - root_space
free_space = required_space - unused_space

# Use the same framework with a global variable
min(min_candidates)