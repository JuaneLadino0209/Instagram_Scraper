import sys
sys.path.insert(0, '../')

import node.node as nd 

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
"""def tend_analysis(node):
	followlisr
	soccer = ['cristiano','leomessi','davidBeckham','fifaworldcup','433','neymarjr','realmadrid','fcbarcelona','paulpogba','championsleague','sporf','goalglobal','premierleague','laliga','seriea','bundesliga_en','futbolalreves','falcao','jamesrodriguez10']
    basquet = ['nba','kingjames','stephencurry30','jharden13','russwest44','easymoneysniper','kyrieirving','nbatv','lakers','warriors','nbaontnt','jumpman23','giannis_an34','houseofhighlights']
    Reguetton = ['anuel_2blea','daddyyankee','mturizomusic','nickyjampr','ozuna','brytiago','sechmusic','lunay','nattinatasha','karolg','farrukoofficial','iambeckyg','maluma','zion','jbalvin','jquiles','badbunnypr']
    Pop = ['justinbieber','champagnepapi','teddysphotos','brunomars','taylorswift','selenagomez','dualipa','camila_cabello','iamcardib','lanadelrey','jlo','shakira','katyperry','ladygaga','arianagrande','badgalriri','postmalone','travisscott','tyga','wizkhalifa']
    electronic = ['zedd','calvinharris','alesso','skrillex','alanwalkermusic','martingarrix','majorlazer','marshmellomusic','diplo','tiesto','davidguetta','thechainsmokers','djsnake','afrojack']
    Paction = ['schwarzenegger','robertdowneyjr','chrishemsworth','thehughjackman','markruffalo','tomholland2013','universalpictures','avengers','marvelstudios','dccomics','therock','marvel']
    Pcomedy = ['Kevinhart4real','adamsandler','jenniferaniston','jimmyfallon','theellenshow','davidspade','jackblack','willsmith','chrisrock','','','','','','']
    Pteens = ['zendaya', 'emmawatson', 'thecameronboyce', 'ddlovato', 'mileycyrus', 'zacefron',  'debbyryan', 'colesprouse', 'nickjonas', 'bellathorne',  'bridgitmendler']
    youTube = ['auronplay','soydrossrotzank','ksi','loganpaul','jakepaul','riceGum','lelepons','susanojose','curtislepore','pewdepie','elrubiuswtf','germangarmendia']
    models = ['caradelevingne','KimKardashian','Kyliejenner','Kendalljenner','gigihadid','bellahadid','KhloeKardashian','haileybieber','alexisren','alessandraambrosio','lilyjcollins']
    beauty_Health = ['fitgirlsguide','wakeupandmakeup','kyliecosmetics','Kendallandkylie','kylieskin','saschafitness','howto.makeup','fashionweek','fashionnova']
    netflix = [ 'ester_exposito', 'itzan.escamilla', 'milliebobbybrown', 'asabopp', 'noahschnapp', '13reasonswhy', 'dylanminnette', 'justin.prentice', 'lacasadepapel', 'jaimelorentelo', 'miguel.g.herran', 'ursulolita']
    series = ['darknetflix' , 'gameofthrones', 'suits_usa', 'houseofcards', 'cw_arrow', 'cwtheflash', 'friends', 'thewalkingdead', 'blackmirror.netflix', 'peakyblindersofficial']
    memes = ['9gag','jokezar','memezar','moriderisa','paradamaslaoficial','badabun','paracaballerosoficial','bestvines','funnyhoodvidz','el_coyote_cojo','worldstar','queboleta','juanpisgonzales']
    fortnite = ['fortnite', 'forrtnite',  'tfue', 'ninja', 'tsm_myth', 'tsm_daequan', 'couragejd', 'bugha', 'ighdistortion', 'hamlinz', 'mongraal']
"""
Node_a = nd.Node("carlosladino6")
Node_b = nd.Node("alejandra.sefair")
list = common_users_follow(Node_b,Node_a)
print(list)
