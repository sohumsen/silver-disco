# THE NETWORK --Completed
import networkx as nx
import matplotlib.pyplot as plt
#ALL COMMENTS
  #Packages
    #Networkx
    #Matplotlib
    #Plotly

  #PSUEDOCODE
    #GET name of user and 3 adjacent nodes
    #IF name or nodes doesnt exist, create new node


def get_input():
  list_of_person_friends=[]

  stop = False
  while stop==False:

    person = input("Enter your name: ") 
    if person =="":
      stop=True
      break
    else:

      list_of_person_friends.append(person)
    
    for i in range(0,3):

      friend_of_person = input("Enter the other names: ")
      list_of_person_friends.append(friend_of_person)

  return list_of_person_friends


def make_graph(list_of_person_friends):
  
  G = nx.DiGraph()
  G.add_nodes_from(set(list_of_person_friends))
  
  for i in range(0,len(list_of_person_friends),4):
     G.add_edges_from([(list_of_person_friends[i],list_of_person_friends[i+1]), (list_of_person_friends[i],list_of_person_friends[i+2]), (list_of_person_friends[i],list_of_person_friends[i+3])])

  x=[]
  for element in set(list_of_person_friends):
    x.append(G.degree[element]) #return num of nodes incident to element
  print("Max node adjacencies: ", max(x))

  #print(nx.shortest_path(G, "a", "d"))

  sp = dict(nx.all_pairs_shortest_path(G))
  print(sp[list_of_person_friends[0]])

  nx.draw(G,with_labels=True, font_weight='bold')
  plt.savefig("graph.png")
  plt.show()


def main():
  list_of_person_friends=get_input()

  make_graph(list_of_person_friends)

main()