def split_string(source,splitlist):
  
    split = True
    output = []
    for item in source:
        if item in splitlist:
            split = True
        else:
            if split:
                output.append(item)
                split = False
            else:
                output[-1] = output[-1] + item
    return output

def create_data_structure(string_input):
    x = 1
    y = 1
    i = 0
    j = 0
    k = 0
    initial_structure = []
    network = {}
    con = []
    game = []
    while y!=0 :
        if y == 1:
            data = string_input[y-1:string_input.find('.',y)]
            initial_structure.append(data)
            y = string_input.find('.', y)+1
            
        else:
            data = string_input[y:string_input.find('.',y)]
            initial_structure.append(data)
            y = string_input.find('.', y)+1

    while i < len(initial_structure)-1:
        info = split_string(initial_structure[i], [',' , ' '])
        info1 = info[0].split()
        network[info1[0]] = []
        i = i+1
        
    while j < len(initial_structure)-1:
        if j %2 == 0:
            info = split_string(initial_structure[j], [',' , ' '])
            name = info[0]
            network[name].append(info[4:])
            j = j+1
        elif j % 2 != 0:
            play = initial_structure[j].find("play")
            space = initial_structure[j].find(" ", play)
            lst =[x.strip() for x in initial_structure[j][space+ 1:].split(',')]
            network[name].append(lst)
            j = j+1                        
    return network

def get_connections(network, user):
    if not user in network:
        return None
    else:
	    return network[user][0]
	
def get_games_liked(network,user):
    if user not in network:
        return None
    return network[user][1]

def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    elif user_B not in network[user_A][0]:
        network[user_A][0].append(user_B)
        return network
    else:
        return network

def add_new_user(network, user, games):
    if user not in network:
        network[user] = [[],[]]
        for item in games:
            network[user][1].append(item)
    return network

def get_secondary_connections(network, user):
    h = 0
    if user in network:
        if network[user][0]!= []:
            primary_connections = network[user][0]
            result = []
            results= []
            for item in primary_connections:
                i = 0
                j = 0
                while i < len(network[item][0]):
                    if network[item][0] != []:
                        result.append(network[item][0][i])
                        i = i+1
                    else:
                        i = i+1
                print result
            while h < len(result):
                k = 0
                while k < len(result):
                    if result[h] == result[k] and h==k:
                        k +=1
                    elif result[h] == result[k] and h!=k:
                        del result[k]
                        
                    else:
                        k+=1
                h+= 1
                    
            return result
        else:
            return []
    else:
        return None

def count_common_connections(network, user_A, user_b):
    count = 0
    j = 0
    if user_A not in network:
        return False
    if user_b not in network:
        return False
    if len(user_A) > len(user_b):
        shorter = network[user_b][0]
        longer = network[user_A][0]
        length1 = len(network[user_b][0])
        length2 =len(network[user_A][0])
    else:
        shorter = network[user_A][0]
        longer = network[user_b][0]
        length1 = len(network[user_A][0])
        length2 = len(network[user_b][0])
    while j < length1:
        k = 0
        while k < length2:
            if shorter[j] == longer[k]:
                count = count + 1
                k = k+1
            else:
                k = k+1
        j = j+1
    return count

def recur_path(network, user_A, user_B, path=None):
    if path == None:
        path = []
    path = path + [user_A]
    if user_A == user_B:
        return path
    for node in network[user_A][0]:
        if node not in path:
            newpath = recur_path(network, node, user_B, path)
            if newpath:
                return newpath
    return None

def find_path_to_friend(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return None
    return recur_path(network, user_A, user_B, path=None)
  

def count_common_games(network,user_A, user_b):
    if user_A not in network:
        return False
    elif user_b not in network:
        return False
    else:
        common_games = []
        j = 0
        if len(user_A) > len(user_b):
            shorter = network[user_b][1]
            longer = network[user_A][1]
            length1 = len(network[user_b][1])
            length2 =len(network[user_A][1])
        else:
            shorter = network[user_A][1]
            longer = network[user_b][1]
            length1 = len(network[user_A][1])
            length2 = len(network[user_b][1])
        while j < length1:
            k = 0
            while k < length2:
                if shorter[j] == longer[k]:
                    common_games.append(shorter[j])
                    k = k+1
                else:
                    k = k+1
            j = j+1
        return common_games 
