import sys
sys.path.insert(0, '../')

import node.node as nd
def percentage(list_a,list_b):
	den = len(list_b)
	set_a = set(list_a)
	set_b = set(list_b)
	set_c = set_a.intersection(set_b)
	f_list = list(set_c)
	num = len(f_list)
	return(num/den,f_list)


def common_users_follow(node_a,node_b):
	set_a = set(node_a.get_follow_list())
	set_b = set(node_b.get_follow_list())
	inter = set_a.intersection(set_b)
	return list(inter)

def common_users_following(node_a,node_b):
	set_a = set(node_a.get_following_list())
	set_b = set(node_b.get_following_list())
	inter = set_a.intersection(set_b)
	return list(inter)
def trend_analysis(node):
	perc_list = []
	followList = node.get_follow_list()
	soccer = ['cristiano','leomessi','davidBeckham','fifaworldcup','433','neymarjr','realmadrid','fcbarcelona','paulpogba','championsleague','sporf','goalglobal','premierleague','laliga','seriea','bundesliga_en','futbolalreves','falcao','jamesrodriguez10']
	basquet = ['nba','kingjames','stephencurry30','jharden13','russwest44','easymoneysniper','kyrieirving','nbatv','lakers','warriors','nbaontnt','jumpman23','giannis_an34','houseofhighlights']
	Reguetton = ['anuel_2blea','daddyyankee','mturizomusic','nickyjampr','ozuna','brytiago','sechmusic','lunay','nattinatasha','karolg','farrukoofficial','iambeckyg','maluma','zion','jbalvin','jquiles','badbunnypr']
	Pop = ['justinbieber','champagnepapi','teddysphotos','brunomars','taylorswift','selenagomez','dualipa','camila_cabello','iamcardib','lanadelrey','jlo','shakira','katyperry','ladygaga','arianagrande','badgalriri','postmalone','travisscott','tyga','wizkhalifa']
	electronic =['zedd','calvinharris','alesso','skrillex','alanwalkermusic','martingarrix','majorlazer','marshmellomusic','diplo','tiesto','davidguetta','thechainsmokers','djsnake','afrojack']
	Paction = ['schwarzenegger','robertdowneyjr','chrishemsworth','thehughjackman','markruffalo','tomholland2013','universalpictures','avengers','marvelstudios','dccomics','therock','marvel']
	Pcomedy = ['Kevinhart4real','adamsandler','jenniferaniston','jimmyfallon','theellenshow','davidspade','jackblack','willsmith','chrisrock']
	Pteens = ['zendaya', 'emmawatson', 'thecameronboyce', 'ddlovato', 'mileycyrus', 'zacefron',  'debbyryan', 'colesprouse', 'nickjonas', 'bellathorne',  'bridgitmendler']
	youTube = ['auronplay','soydrossrotzank','ksi','loganpaul','jakepaul','riceGum','lelepons','susanojose','curtislepore','pewdepie','elrubiuswtf','germangarmendia']
	models = ['caradelevingne','KimKardashian','Kyliejenner','Kendalljenner','gigihadid','bellahadid','KhloeKardashian','haileybieber','alexisren','alessandraambrosio','lilyjcollins']
	beauty_Health = ['fitgirlsguide','wakeupandmakeup','kyliecosmetics','Kendallandkylie','kylieskin','saschafitness','howto.makeup','fashionweek','fashionnova']
	netflix = [ 'ester_exposito', 'itzan.escamilla', 'milliebobbybrown', 'asabopp', 'noahschnapp', '13reasonswhy', 'dylanminnette', 'justin.prentice', 'lacasadepapel', 'jaimelorentelo', 'miguel.g.herran', 'ursulolita']
	series = ['darknetflix' , 'gameofthrones', 'suits_usa', 'houseofcards', 'cw_arrow', 'cwtheflash', 'friends', 'thewalkingdead', 'blackmirror.netflix', 'peakyblindersofficial']
	memes = ['9gag','jokezar','memezar','moriderisa','paradamaslaoficial','badabun','paracaballerosoficial','bestvines','funnyhoodvidz','el_coyote_cojo','worldstar','queboleta','juanpisgonzales']
	fortnite = ['fortnite', 'forrtnite',  'tfue', 'ninja', 'tsm_myth', 'tsm_daequan', 'couragejd', 'bugha', 'ighdistortion', 'hamlinz', 'mongraal']
	f_list = [soccer,basquet,Reguetton,Pop,electronic,Paction,Pcomedy,Pteens,youTube,models,beauty_Health,netflix,series,memes,fortnite]
	for i in f_list:
		perc = percentage(followList,i)
		perc_list.append(perc)
	str1 = "soccer tranding percentage:"
	str2 = "basquet tranding percentage:"
	str3 = "Reguetton tranding percentage:"
	str4 = "Pop tranding percentage:"
	str5 = "electronic tranding percentage:"
	str6 = "ActionMovies tranding percentage:"
	str7 = "comedyMovies tranding percentage:"
	str8 = "TeensMovies tranding percentage:"
	str9 = "youTube tranding percentage:"
	str10 = "models tranding percentage:"
	str11 = "beauty_Health tranding percentage:"
	str12 = "netflix tranding percentage:"
	str13 = "series tranding percentage:"
	str14 = "memes tranding percentage:"
	str15 = "fortnite tranding percentage:"
	print(str1)
	print(perc_list[0])
	print(str2)
	print(perc_list[1])
	print(str3)
	print(perc_list[2])
	print(str4)
	print(perc_list[3])
	print(str5)
	print(perc_list[4])
	print(str6)
	print(perc_list[5])
	print(str7)
	print(perc_list[6])
	print(str8)
	print(perc_list[7])
	print(str9)
	print(perc_list[8])
	print(str10)
	print(perc_list[9])
	print(str11)
	print(perc_list[10])
	print(str12)
	print(perc_list[11])
	print(str13)
	print(perc_list[12])
	print(str14)
	print(perc_list[13])
	print(str15)
	print(perc_list[14])
print("creating Node_a....")
Node_a = nd.Node("carlosladino6")
#print("creating Node_b....")
Node_b = nd.Node("alejandrouribe718")
"""print("This is the name to Node_a__________________________\n")
print(Node_a.get_name())
print("This is the follow list Node_a__________________________\n")
print(Node_a.get_follow_list())
print("This is the following list Node_a__________________________\n")
print(Node_a.get_following_list())
print("This is the biography Node_a__________________________\n")"""

print(Node_a.get_biography())
print("This is numLikes to Node_a__________________________\n")
print(Node_a.get_likes())
print("Now the realationship algorithm between Node_a and Node_b__________________________\n")
print("This is the common user follow between Node_a and Node_b__________________________\n")
print(common_users_follow(Node_a,Node_b))
print("This is the common user following between Node_a and Node_b__________________________\n")
print(common_users_following(Node_a,Node_b))
print("This the trend analisis by topic to Node_a__________________________\n")
print(trend_analysis(Node_b))
print(trend_analysis(Node_b))
