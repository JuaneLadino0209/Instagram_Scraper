import sys
sys.path.insert(0, '../')

import node.node as nd 

def common_users_follow(node_a,node_b):
	set_a = set(Node_a.get_follow_list())
	set_b = set(Node_b.get_follow_list())
	inter = set_a.intersection(set_b)
	return list(inter)

def common_users_following(node_a,node_b):
	set_a = set(Node_a.get_following_list())
	set_b = set(Node_b.get_following_list())
	inter = set_a.intersection(set_b)
	return list(inter)
Node_a = nd.Node("camilarocet")
Node_b = nd.Node("valentina_9707")
list = common_users_follow(Node_b,Node_a)
print(list)
