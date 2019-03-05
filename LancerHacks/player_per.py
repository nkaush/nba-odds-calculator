from teams import team_names

all_per_dic = {'Marc Gasol': 18.6, 'Kawhi Leonard': 22.5, 'Danny Green': 13.0, 
			   'Pascal Siakam': 15.5, 'OG Anunoby': 9.7, 'Kyle Lowry': 18.5, 
			   'Serge Ibaka': 17.1, 'Norman Powell': 12.3, 'Fred VanVleet': 14.4, 
			   'Chris Boucher': 28.4, 'Jordan Loyd': 11.8, 'Patrick McCaw': 7.6, 
			   'Jimmy Butler': 20.1, 'Tobias Harris': 16.8, 'Ben Simmons': 20.2, 
			   'Boban Marjanovic': 26.9, 'T.J. McConnell': 13.5, 'Furkan Korkmaz': 10.6, 
			   'Justin Patton': 19.8, 'Jonathon Simmons': 11.0, 'Joel Embiid': 24.1, 
			   'J.J. Redick': 15.0, 'Mike Scott': 13.7, 'James Ennis': 11.7, 
			   'Amir Johnson': 15.9, 'Jonah Bolden': 11.0, 'Shake Milton': 14.9, 
			   'Haywood Highsmith': 17.4, 'Kyrie Irving': 22.1, 'Marcus Morris': 13.4, 
			   'Terry Rozier': 13.0, 'Al Horford': 18.9, 'Jaylen Brown': 12.6, 
			   'Jayson Tatum': 15.7, 'Gordon Hayward': 17.5, 'Semi Ojeleye': 5.6, 
			   'Guerschon Yabusele': 12.2, 'Daniel Theis': 17.2, 'Brad Wanamaker': 14.3, 
			   'Robert Williams': 20.5, 'Aron Baynes': 14.1, 'Marcus Smart': 11.7, 
			   'PJ Dozier': 18.0, 'R.J. Hunter': 7.5, "D'Angelo Russell": 15.5, 
			   'Rondae Hollis-Jefferson': 14.6, 'DeMarre Carroll': 13.4, 'Allen Crabbe': 11.3, 
			   'Caris LeVert': 14.1, 'Jared Dudley': 12.7, 'Spencer Dinwiddie': 14.9, 
			   'Jarrett Allen': 18.3, 'Dzanan Musa': 3.0, 'Rodions Kurucs': 11.1, 
			   'Shabazz Napier': 12.6, 'Ed Davis': 16.7, 'Joe Harris': 11.6, 
			   'Treveon Graham': 8.2, 'Theo Pinson': 8.2, 'Alan Williams': 19.0, 
			   'Emmanuel Mudiay': 11.6, 'Lance Thomas': 8.4, 'Frank Ntilikina': 6.8, 
			   'Dennis Smith Jr.': 12.6, 'Damyean Dotson': 11.4, 'Isaiah Hicks': 6.9, 
			   'Kevin Knox': 8.4, 'Mario Hezonja': 10.6, 'DeAndre Jordan': 18.5, 
			   'Luke Kornet': 16.0, 'Mitchell Robinson': 19.7, 'Allonzo Trier': 12.1, 
			   'Noah Vonleh': 11.7, 'Kadeem Allen': 7.5, 'Trey Lyles': 13.4,
			   'Malik Beasley': 13.3, 'Jamal Murray': 14.7, 'Juan Hernangomez': 12.4, 
			   'Tyler Lydon': 8.1, 'Paul Millsap': 19.0, 'Mason Plumlee': 17.9, 
			   'Gary Harris': 14.1, 'Torrey Craig': 9.7, 'Nikola Jokic': 24.9, 
			   'Will Barton': 14.9, 'Jarred Vanderbilt': 17.0, 'Isaiah Thomas': 20.5, 
			   'Thomas Welsh': 13.8, 'Monte Morris': 16.9, 'Brandon Goodwin': 8.5, 
			   'Dennis Schroder': 15.2, 'Russell Westbrook': 23.7, 'Steven Adams': 16.8, 
			   'Alex Abrines': 8.8, 'Patrick Patterson': 12.7, 'Abdel Nader': 7.3, 
			   'Andre Roberson': 9.8, 'Terrance Ferguson': 7.0, 'Nerlens Noel': 16.8, 
			   'Paul George': 19.1, 'Deonte Burton': 7.3, 'Jerami Grant': 12.6, 
			   'Raymond Felton': 13.8, 'Hamidou Diallo': 10.6, 'Donte Grantham': -18.9, 
			   'Damian Lillard': 21.3, 'CJ McCollum': 17.2, 'Al-Farouq Aminu': 12.4, 
			   'Evan Turner': 12.0, 'Jake Layman': 11.6, 'Meyers Leonard': 12.3, 
			   'Skal Labissiere': 14.7, 'Maurice Harkless': 12.2, 'Zach Collins': 10.3, 
			   'Anfernee Simons': -5.5, 'Jusuf Nurkic': 18.7, 'Gary Trent Jr.': 1.9, 
			   'Seth Curry': 13.7, 'Rodney Hood': 13.5, 'Rudy Gobert': 21.2, 
			   'Ricky Rubio': 15.8, 'Jae Crowder': 13.0, 'Donovan Mitchell': 16.4, 
			   'Tony Bradley': 4.8, 'Kyle Korver': 12.8, 'Thabo Sefolosha': 11.5, 
			   "Royce O'Neale": 10.2, 'Ekpe Udoh': 11.7, 'Joe Ingles': 12.2, 
			   'Grayson Allen': 4.1, 'Derrick Favors': 18.7, 'Dante Exum': 8.4, 
			   'Raul Neto': 10.9, 'Georges Niang': 8.9, 'Naz Mitrou-Long': 0.5, 
			   'Tyler Cavanaugh': 12.7, 'Gorgui Dieng': 16.0, 'Andrew Wiggins': 14.6, 
			   'Robert Covington': 13.5, 'Karl-Anthony Towns': 24.7, 'Tyus Jones': 13.2, 
			   'Dario Saric': 13.8, 'Jerryd Bayless': 12.3, 'Jeff Teague': 17.1, 
			   'Taj Gibson': 15.3, 'Josh Okogie': 7.7, 'Derrick Rose': 18.0, 
			   'Jared Terrell': 1.9, 'Keita Bates-Diop': -2.7, 'Anthony Tolliver': 11.3, 
			   'C.J. Williams': 8.9, 'Luol Deng': 15.4, 'Isaiah Canaan': 10.7, 
			   'Eric Bledsoe': 18.0, 'Giannis Antetokounmpo': 21.4, 'Khris Middleton': 15.5, 
			   'Malcolm Brogdon': 15.6, 'D.J. Wilson': 11.6, 'George Hill': 15.0, 
			   'Sterling Brown': 10.1, 'Tony Snell': 9.0, 'Nikola Mirotic': 16.8, 
			   'Donte DiVincenzo': 8.5, 'Ersan Ilyasova': 15.5, 'Brook Lopez': 20.1, 
			   'Trevon Duval': 106.2, 'Pat Connaughton': 10.4, 'Christian Wood': 16.4, 
			   'Victor Oladipo': 16.8, 'Myles Turner': 17.5, 'Thaddeus Young': 16.4, 
			   'Cory Joseph': 12.7, 'Domantas Sabonis': 15.3, 'T.J. Leaf': 12.1, 
			   'Bojan Bogdanovic': 13.0, 'Darren Collison': 16.2, 'Edmond Sumner': 5.4, 
			   'Wade Baldwin': 7.1, 'Aaron Holiday': 12.5, 'Nik Stauskas': 9.0, 
			   'Tyreke Evans': 17.3, 'Doug McDermott': 10.4, "Kyle O'Quinn": 17.8, 
			   'Alize Johnson': -0.4, 'Davon Reed': 5.1, 'Reggie Jackson': 16.0, 
			   'Jon Leuer': 14.5, 'Ish Smith': 13.4, 'Andre Drummond': 21.8, 
			   'Henry Ellenson': 9.9, 'Thon Maker': 11.6, 'Luke Kennard': 11.5, 
			   'Langston Galloway': 11.3, 'Blake Griffin': 22.3, 'Bruce Brown': 6.4, 
			   'Glenn Robinson III': 10.4, 'Jose Calderon': 15.8, 'Sviatoslav Mykhailiuk': 5.9, 
			   'Zaza Pachulia': 14.6, 'Khyri Thomas': 8.8, 'Kalin Lucas': 8.0, 
			   'Isaiah Whitehead': 7.9, 'Robin Lopez': 16.1, 'Timothe Luwawu-Cabarrot': 7.6, 
			   'Denzel Valentine': 10.6, 'Kris Dunn': 11.9, 'Lauri Markkanen': 16.0, 'Cristiano Felicio': 14.2, 'Otto Porter': 15.5, 'Wayne Selden': 9.7, 'Chandler Hutchison': 8.9, 'Wendell Carter Jr.': 15.3, 'Zach LaVine': 14.4, 'Antonio Blakeney': 11.1, 'Ryan Arcidiacono': 9.9, 'Rawle Alkins': 60.9, 'Shaquille Harrison': 12.8, 'Brandon Sampson': 5.8, 'John Henson': 17.1, 'Larry Nance Jr.': 17.0, 'Brandon Knight': 14.1, 'Kevin Love': 21.9, 'Tristan Thompson': 15.4, 'Jordan Clarkson': 15.2, 'Matthew Dellavedova': 10.0, 'Marquese Chriss': 11.5, 'J.R. Smith': 14.0, 'Ante Zizic': 18.5, 'Cedi Osman': 10.8, 'Collin Sexton': 10.3, 'Channing Frye': 13.3, 'David Nwaba': 12.5, 'Jaron Blossomgame': 10.9, 'Deng Adel': 4.1, 'Klay Thompson': 16.4, 'Draymond Green': 15.5, 'Damian Jones': 12.6, 'Jordan Bell': 16.3, 'Stephen Curry': 23.9, 'Andre Iguodala': 15.7, 'Shaun Livingston': 12.5, 'Quinn Cook': 13.0, 'Jacob Evans': -1.3, 'DeMarcus Cousins': 22.4, 'Kevin Durant': 25.3, 'Kevon Looney': 15.8, 'Jonas Jerebko': 13.2, 'Damion Lee': 11.9, 'Marcus Derrickson': 10.4, 'Alfonzo McKinnie': 11.1, 'Wilson Chandler': 13.1, 'Patrick Beverley': 12.5, 'Lou Williams': 18.4, 'Ivica Zubac': 17.5, 'Garrett Temple': 9.6, 'Danilo Gallinari': 16.6, 'Sindarius Thornwell': 7.6, 'JaMychal Green': 14.2, 'Johnathan Motley': 16.4, 'Shai Gilgeous-Alexander': 12.3, 'Landry Shamet': 10.8, 'Jerome Robinson': 8.5, 'Angel Delgado': 7.6, 'Luc Mbah a Moute': 10.7, 'Michael Beasley': 15.7, 'Montrezl Harrell': 21.9, 'Tyrone Wallace': 9.5, 'Alec Burks': 13.7, 'Willie Cauley-Stein': 16.8, 'Kosta Koufos': 15.5, 'Harrison Barnes': 13.3, 'Buddy Hield': 15.1, 'Caleb Swanigan': 5.6, 'Harry Giles': 13.8, "De'Aaron Fox": 14.3, 'Bogdan Bogdanovic': 13.9, 'Frank Mason III': 12.9, 'Marvin Bagley III': 17.2, 'Nemanja Bjelica': 12.6, 'Yogi Ferrell': 12.3, 'Troy Williams': 11.2, 'Corey Brewer': 11.8, 'Brandon Ingram': 11.4, 'Lonzo Ball': 12.2, 'Kyle Kuzma': 14.4, 'Josh Hart': 11.1, 'Reggie Bullock': 11.4, 'Mike Muscala': 13.6, 'Moritz Wagner': 12.9, 'Isaac Bonga': 9.5, 'Kentavious Caldwell-Pope': 12.0, 'Rajon Rondo': 16.3, 'LeBron James': 27.6, 'Lance Stephenson': 12.2, 'JaVale McGee': 19.3, 'Alex Caruso': 8.8, 'Johnathan Williams': 10.3, 'Tyson Chandler': 16.2, 'T.J. Warren': 16.2, 'Devin Booker': 15.5, 'Kelly Oubre Jr.': 11.4, 'Richaun Holmes': 18.6, 'Tyler Johnson': 13.8, 'Troy Daniels': 10.6, 'Dragan Bender': 6.9, 'Josh Jackson': 11.4, 'Deandre Ayton': 21.0, 'Mikal Bridges': 11.2, 'George King': 1.9, 'Elie Okobo': 7.3, "De'Anthony Melton": 9.6, 'Jamal Crawford': 15.1, 'Jawun Evans': 6.8, 'Michael Kidd-Gilchrist': 13.8, 'Kemba Walker': 19.2, 'Cody Zeller': 15.4, 'Jeremy Lamb': 15.7, 'Frank Kaminsky': 13.4, 'Nicolas Batum': 15.0, 'Bismack Biyombo': 12.8, 'Marvin Williams': 13.7, 'Willy Hernangomez': 19.8, 'Malik Monk': 11.8, 'Dwayne Bacon': 7.6, 'Miles Bridges': 12.0, 'J.P. Macura': 0.6, "Devonte' Graham": 11.2, 'Tony Parker': 18.3, 'Joe Chealey': 2.1, 'Justise Winslow': 10.1, 'Goran Dragic': 17.2, 'Ryan Anderson': 16.5, 'Hassan Whiteside': 24.0, 'Rodney McGruder': 9.3, 'Bam Adebayo': 16.1, 'James Johnson': 14.7, 'Dion Waiters': 12.0, 'Kelly Olynyk': 16.0, 'Josh Richardson': 12.8, 'Derrick Jones Jr.': 13.8, 'Duncan Robinson': 7.9, 'Udonis Haslem': 13.0, 'Dwyane Wade': 23.6, 'Nikola Vucevic': 20.0, 'Terrence Ross': 12.4, 'Jerian Grant': 12.5, 'Jarell Martin': 10.5, 'Timofey Mozgov': 14.7, 'D.J. Augustin': 14.1, 'Evan Fournier': 13.3, 'Jonathan Isaac': 11.2, 'Markelle Fultz': 11.2, 'Wesley Iwundu': 7.8, 'Khem Birch': 16.6, 'Mohamed Bamba': 15.0, 'Isaiah Briscoe': 5.4, 'Melvin Frazier': -9.6, 'Aaron Gordon': 15.4, 'Troy Caupain': 33.1, 'Amile Jefferson': 17.8, 'John Wall': 19.4, 'Sam Dekker': 13.0, 'Bobby Portis': 16.9, 'Ian Mahinmi': 13.0, 'Tomas Satoransky': 13.6, 'Bradley Beal': 16.7, 'Devin Robinson': 21.6, 'Troy Brown Jr.': 11.2, 'Trevor Ariza': 13.3, 'Jeff Green': 13.3, 'Dwight Howard': 21.6, 'Jabari Parker': 16.2, 'Thomas Bryant': 20.5, 'Jordan McRae': 12.3, 'Chasson Randle': 11.5, 'John Jenkins': 12.0, 'Justin Anderson': 12.9, 'Kent Bazemore': 12.5, 'Jeremy Lin': 15.5, 'Taurean Prince': 12.0, "DeAndre' Bembry": 9.2, 'Miles Plumlee': 13.7, 'John Collins': 19.8, 'Dewayne Dedmon': 15.1, 'Trae Young': 14.2, 'Kevin Huerter': 9.8, 'Omari Spellman': 12.3, 'Jaylen Adams': 11.0, 'Alex Len': 14.6, 'Alex Poythress': 11.9, 'Vince Carter': 18.9, 'James Harden': 24.2, 'Iman Shumpert': 10.0, 'Eric Gordon': 14.5, 'Nene': 17.1, 'P.J. Tucker': 11.0, 'Chris Paul': 25.4, 'Gerald Green': 13.1, 'Isaiah Hartenstein': 9.6, 'Clint Capela': 22.2, 'Gary Clark': 8.4, 'Vince Edwards': 3.9, 'Danuel House': 12.5, 'Austin Rivers': 10.3, 'Kenneth Faried': 19.7, 'LaMarcus Aldridge': 20.8, 'Dejounte Murray': 14.2, 'DeMar DeRozan': 17.8, 'Jakob Poeltl': 16.8, 'Derrick White': 14.7, 'Pau Gasol': 21.4, 'Patty Mills': 14.5, 'Rudy Gay': 16.8, 'Davis Bertans': 13.9, 'Lonnie Walker': 0.6, 'Dante Cunningham': 11.2, 'Marco Belinelli': 12.4, 'Bryn Forbes': 10.0, 'Quincy Pondexter': 9.8, 'Chimezie Metu': 8.2, 'Drew Eubanks': 19.9, 'Ben Moore': -2.3, 'Kristaps Porzingis': 18.3, 'J.J. Barea': 14.5, 'Dwight Powell': 18.1, 'Dorian Finney-Smith': 9.3, 'Courtney Lee': 12.2, 'Justin Jackson': 9.6, 'Tim Hardaway Jr.': 13.6, 'Zach Randolph': 19.3, 'Maxi Kleber': 13.5, 'Trey Burke': 13.8, 'Luka Doncic': 19.4, 'Ryan Broekhoff': 11.1, 'Jalen Brunson': 10.6, 'Dirk Nowitzki': 22.6, 'Daryl Macon': 19.6, 'Devin Harris': 16.1, 'Anthony Davis': 27.5, 'Stanley Johnson': 8.6, "E'Twaun Moore": 11.4, 'Cheick Diallo': 17.1, 'Solomon Hill': 9.1, 'Jrue Holiday': 16.8, 'Frank Jackson': 9.2, 'Darius Miller': 8.4, 'Jason Smith': 12.9, 'Elfrid Payton': 15.2, 'Julius Randle': 17.5, 'Ian Clark': 10.3, 'Kenrich Williams': 11.1, 'Jahlil Okafor': 16.6, 'Tim Frazier': 12.1, 'Jonas Valanciunas': 19.7, 'Delon Wright': 15.8, 'Chandler Parsons': 14.9, 'Mike Conley': 17.6, 'Justin Holiday': 10.8, 'Tyler Dorsey': 9.6, 'C.J. Miles': 13.1, 'Dillon Brooks': 9.6, 'Ivan Rabb': 17.6, 'Jaren Jackson Jr.': 17.1, 'Avery Bradley': 11.2, 'Kyle Anderson': 13.6, 'Jevon Carter': 3.5, 'Yuta Watanabe': 7.1, 'Joakim Noah': 17.5, 'Julian Washburn': 1.6, 'Bruno Caboclo': 7.0}

def all_per():
	global all_per_dic
	return all_per_dic

player_per_list = [{'Marc Gasol': 18.6, 'Kawhi Leonard': 22.5, 'Danny Green': 13.0, 'Pascal Siakam': 15.5, 'OG Anunoby': 9.7, 'Kyle Lowry': 18.5, 'Serge Ibaka': 17.1, 'Norman Powell': 12.3, 'Fred VanVleet': 14.4, 'Chris Boucher': 28.4, 'Jordan Loyd': 11.8, 'Patrick McCaw': 7.6}, {'Jimmy Butler': 20.1, 'Tobias Harris': 16.8, 'Ben Simmons': 20.2, 'Boban Marjanovic': 26.9, 'T.J. McConnell': 13.5, 'Furkan Korkmaz': 10.6, 'Justin Patton': 19.8, 'Jonathon Simmons': 11.0, 'Joel Embiid': 24.1, 'J.J. Redick': 15.0, 'Mike Scott': 13.7, 'James Ennis': 11.7, 'Amir Johnson': 15.9, 'Jonah Bolden': 11.0, 'Shake Milton': 14.9, 'Haywood Highsmith': 17.4}, {'Kyrie Irving': 22.1, 'Marcus Morris': 13.4, 'Terry Rozier': 13.0, 'Al Horford': 18.9, 'Jaylen Brown': 12.6, 'Jayson Tatum': 15.7, 'Gordon Hayward': 17.5, 'Semi Ojeleye': 5.6, 'Guerschon Yabusele': 12.2, 'Daniel Theis': 17.2, 'Brad Wanamaker': 14.3, 'Robert Williams': 20.5, 'Aron Baynes': 14.1, 'Marcus Smart': 11.7, 'PJ Dozier': 18.0, 'R.J. Hunter': 7.5}, {"D'Angelo Russell": 15.5, 'Rondae Hollis-Jefferson': 14.6, 'DeMarre Carroll': 13.4, 'Allen Crabbe': 11.3, 'Caris LeVert': 14.1, 'Jared Dudley': 12.7, 'Spencer Dinwiddie': 14.9, 'Jarrett Allen': 18.3, 'Dzanan Musa': 3.0, 'Rodions Kurucs': 11.1, 'Shabazz Napier': 12.6, 'Ed Davis': 16.7, 'Joe Harris': 11.6, 'Treveon Graham': 8.2, 'Theo Pinson': 8.2, 'Alan Williams': 19.0}, {'Emmanuel Mudiay': 11.6, 'Lance Thomas': 8.4, 'Frank Ntilikina': 6.8, 'Dennis Smith Jr.': 12.6, 'Damyean Dotson': 11.4, 'Isaiah Hicks': 6.9, 'Kevin Knox': 8.4, 'Mario Hezonja': 10.6, 'DeAndre Jordan': 18.5, 'Luke Kornet': 16.0, 'Mitchell Robinson': 19.7, 'Allonzo Trier': 12.1, 'Noah Vonleh': 11.7, 'Kadeem Allen': 7.5}, {'Trey Lyles': 13.4, 'Malik Beasley': 13.3, 'Jamal Murray': 14.7, 'Juan Hernangomez': 12.4, 'Tyler Lydon': 8.1, 'Paul Millsap': 19.0, 'Mason Plumlee': 17.9, 'Gary Harris': 14.1, 'Torrey Craig': 9.7, 'Nikola Jokic': 24.9, 'Will Barton': 14.9, 'Jarred Vanderbilt': 17.0, 'Isaiah Thomas': 20.5, 'Thomas Welsh': 13.8, 'Monte Morris': 16.9, 'Brandon Goodwin': 8.5}, {'Dennis Schroder': 15.2, 'Russell Westbrook': 23.7, 'Steven Adams': 16.8, 'Alex Abrines': 8.8, 'Patrick Patterson': 12.7, 'Abdel Nader': 7.3, 'Andre Roberson': 9.8, 'Terrance Ferguson': 7.0, 'Nerlens Noel': 16.8, 'Paul George': 19.1, 'Deonte Burton': 7.3, 'Jerami Grant': 12.6, 'Raymond Felton': 13.8, 'Hamidou Diallo': 10.6, 'Donte Grantham': -18.9}, {'Damian Lillard': 21.3, 'CJ McCollum': 17.2, 'Al-Farouq Aminu': 12.4, 'Evan Turner': 12.0, 'Jake Layman': 11.6, 'Meyers Leonard': 12.3, 'Skal Labissiere': 14.7, 'Maurice Harkless': 12.2, 'Zach Collins': 10.3, 'Anfernee Simons': -5.5, 'Jusuf Nurkic': 18.7, 'Gary Trent Jr.': 1.9, 'Seth Curry': 13.7, 'Rodney Hood': 13.5}, {'Rudy Gobert': 21.2, 'Ricky Rubio': 15.8, 'Jae Crowder': 13.0, 'Donovan Mitchell': 16.4, 'Tony Bradley': 4.8, 'Kyle Korver': 12.8, 'Thabo Sefolosha': 11.5, "Royce O'Neale": 10.2, 'Ekpe Udoh': 11.7, 'Joe Ingles': 12.2, 'Grayson Allen': 4.1, 'Derrick Favors': 18.7, 'Dante Exum': 8.4, 'Raul Neto': 10.9, 'Georges Niang': 8.9, 'Naz Mitrou-Long': 0.5, 'Tyler Cavanaugh': 12.7}, {'Gorgui Dieng': 16.0, 'Andrew Wiggins': 14.6, 'Robert Covington': 13.5, 'Karl-Anthony Towns': 24.7, 'Tyus Jones': 13.2, 'Dario Saric': 13.8, 'Jerryd Bayless': 12.3, 'Jeff Teague': 17.1, 'Taj Gibson': 15.3, 'Josh Okogie': 7.7, 'Derrick Rose': 18.0, 'Jared Terrell': 1.9, 'Keita Bates-Diop': -2.7, 'Anthony Tolliver': 11.3, 'C.J. Williams': 8.9, 'Luol Deng': 15.4, 'Isaiah Canaan': 10.7}, {'Eric Bledsoe': 18.0, 'Giannis Antetokounmpo': 21.4, 'Khris Middleton': 15.5, 'Malcolm Brogdon': 15.6, 'D.J. Wilson': 11.6, 'George Hill': 15.0, 'Sterling Brown': 10.1, 'Tony Snell': 9.0, 'Nikola Mirotic': 16.8, 'Donte DiVincenzo': 8.5, 'Ersan Ilyasova': 15.5, 'Brook Lopez': 20.1, 'Trevon Duval': 106.2, 'Pat Connaughton': 10.4, 'Christian Wood': 16.4}, {'Victor Oladipo': 16.8, 'Myles Turner': 17.5, 'Thaddeus Young': 16.4, 'Cory Joseph': 12.7, 'Domantas Sabonis': 15.3, 'T.J. Leaf': 12.1, 'Bojan Bogdanovic': 13.0, 'Darren Collison': 16.2, 'Edmond Sumner': 5.4, 'Wade Baldwin': 7.1, 'Aaron Holiday': 12.5, 'Nik Stauskas': 9.0, 'Tyreke Evans': 17.3, 'Doug McDermott': 10.4, "Kyle O'Quinn": 17.8, 'Alize Johnson': -0.4, 'Davon Reed': 5.1}, {'Reggie Jackson': 16.0, 'Jon Leuer': 14.5, 'Ish Smith': 13.4, 'Andre Drummond': 21.8, 'Henry Ellenson': 9.9, 'Thon Maker': 11.6, 'Luke Kennard': 11.5, 'Langston Galloway': 11.3, 'Blake Griffin': 22.3, 'Bruce Brown': 6.4, 'Glenn Robinson III': 10.4, 'Jose Calderon': 15.8, 'Sviatoslav Mykhailiuk': 5.9, 'Zaza Pachulia': 14.6, 'Khyri Thomas': 8.8, 'Kalin Lucas': 8.0, 'Isaiah Whitehead': 7.9}, {'Robin Lopez': 16.1, 'Timothe Luwawu-Cabarrot': 7.6, 'Denzel Valentine': 10.6, 'Kris Dunn': 11.9, 'Lauri Markkanen': 16.0, 'Cristiano Felicio': 14.2, 'Otto Porter': 15.5, 'Wayne Selden': 9.7, 'Chandler Hutchison': 8.9, 'Wendell Carter Jr.': 15.3, 'Zach LaVine': 14.4, 'Antonio Blakeney': 11.1, 'Ryan Arcidiacono': 9.9, 'Rawle Alkins': 60.9, 'Shaquille Harrison': 12.8, 'Brandon Sampson': 5.8}, {'John Henson': 17.1, 'Larry Nance Jr.': 17.0, 'Brandon Knight': 14.1, 'Kevin Love': 21.9, 'Tristan Thompson': 15.4, 'Jordan Clarkson': 15.2, 'Matthew Dellavedova': 10.0, 'Marquese Chriss': 11.5, 'J.R. Smith': 14.0, 'Ante Zizic': 18.5, 'Cedi Osman': 10.8, 'Collin Sexton': 10.3, 'Channing Frye': 13.3, 'David Nwaba': 12.5, 'Jaron Blossomgame': 10.9, 'Deng Adel': 4.1}, {'Klay Thompson': 16.4, 'Draymond Green': 15.5, 'Damian Jones': 12.6, 'Jordan Bell': 16.3, 'Stephen Curry': 23.9, 'Andre Iguodala': 15.7, 'Shaun Livingston': 12.5, 'Quinn Cook': 13.0, 'Jacob Evans': -1.3, 'DeMarcus Cousins': 22.4, 'Kevin Durant': 25.3, 'Kevon Looney': 15.8, 'Jonas Jerebko': 13.2, 'Damion Lee': 11.9, 'Marcus Derrickson': 10.4, 'Alfonzo McKinnie': 11.1}, {'Wilson Chandler': 13.1, 'Patrick Beverley': 12.5, 'Lou Williams': 18.4, 'Ivica Zubac': 17.5, 'Garrett Temple': 9.6, 'Danilo Gallinari': 16.6, 'Sindarius Thornwell': 7.6, 'JaMychal Green': 14.2, 'Johnathan Motley': 16.4, 'Shai Gilgeous-Alexander': 12.3, 'Landry Shamet': 10.8, 'Jerome Robinson': 8.5, 'Angel Delgado': 7.6, 'Luc Mbah a Moute': 10.7, 'Michael Beasley': 15.7, 'Montrezl Harrell': 21.9, 'Tyrone Wallace': 9.5}, {'Alec Burks': 13.7, 'Willie Cauley-Stein': 16.8, 'Kosta Koufos': 15.5, 'Harrison Barnes': 13.3, 'Buddy Hield': 15.1, 'Caleb Swanigan': 5.6, 'Harry Giles': 13.8, "De'Aaron Fox": 14.3, 'Bogdan Bogdanovic': 13.9, 'Frank Mason III': 12.9, 'Marvin Bagley III': 17.2, 'Nemanja Bjelica': 12.6, 'Yogi Ferrell': 12.3, 'Troy Williams': 11.2, 'Corey Brewer': 11.8}, {'Brandon Ingram': 11.4, 'Lonzo Ball': 12.2, 'Kyle Kuzma': 14.4, 'Josh Hart': 11.1, 'Reggie Bullock': 11.4, 'Mike Muscala': 13.6, 'Moritz Wagner': 12.9, 'Isaac Bonga': 9.5, 'Kentavious Caldwell-Pope': 12.0, 'Rajon Rondo': 16.3, 'LeBron James': 27.6, 'Lance Stephenson': 12.2, 'JaVale McGee': 19.3, 'Alex Caruso': 8.8, 'Johnathan Williams': 10.3, 'Tyson Chandler': 16.2}, {'T.J. Warren': 16.2, 'Devin Booker': 15.5, 'Kelly Oubre Jr.': 11.4, 'Richaun Holmes': 18.6, 'Tyler Johnson': 13.8, 'Troy Daniels': 10.6, 'Dragan Bender': 6.9, 'Josh Jackson': 11.4, 'Deandre Ayton': 21.0, 'Mikal Bridges': 11.2, 'George King': 1.9, 'Elie Okobo': 7.3, "De'Anthony Melton": 9.6, 'Jamal Crawford': 15.1, 'Jawun Evans': 6.8}, {'Michael Kidd-Gilchrist': 13.8, 'Kemba Walker': 19.2, 'Cody Zeller': 15.4, 'Jeremy Lamb': 15.7, 'Frank Kaminsky': 13.4, 'Nicolas Batum': 15.0, 'Bismack Biyombo': 12.8, 'Marvin Williams': 13.7, 'Willy Hernangomez': 19.8, 'Malik Monk': 11.8, 'Dwayne Bacon': 7.6, 'Miles Bridges': 12.0, 'J.P. Macura': 0.6, "Devonte' Graham": 11.2, 'Tony Parker': 18.3, 'Joe Chealey': 2.1}, {'Justise Winslow': 10.1, 'Goran Dragic': 17.2, 'Ryan Anderson': 16.5, 'Hassan Whiteside': 24.0, 'Rodney McGruder': 9.3, 'Bam Adebayo': 16.1, 'James Johnson': 14.7, 'Dion Waiters': 12.0, 'Kelly Olynyk': 16.0, 'Josh Richardson': 12.8, 'Derrick Jones Jr.': 13.8, 'Duncan Robinson': 7.9, 'Udonis Haslem': 13.0, 'Dwyane Wade': 23.6}, {'Nikola Vucevic': 20.0, 'Terrence Ross': 12.4, 'Jerian Grant': 12.5, 'Jarell Martin': 10.5, 'Timofey Mozgov': 14.7, 'D.J. Augustin': 14.1, 'Evan Fournier': 13.3, 'Jonathan Isaac': 11.2, 'Markelle Fultz': 11.2, 'Wesley Iwundu': 7.8, 'Khem Birch': 16.6, 'Mohamed Bamba': 15.0, 'Isaiah Briscoe': 5.4, 'Melvin Frazier': -9.6, 'Aaron Gordon': 15.4, 'Troy Caupain': 33.1, 'Amile Jefferson': 17.8}, {'John Wall': 19.4, 'Sam Dekker': 13.0, 'Bobby Portis': 16.9, 'Ian Mahinmi': 13.0, 'Tomas Satoransky': 13.6, 'Bradley Beal': 16.7, 'Devin Robinson': 21.6, 'Troy Brown Jr.': 11.2, 'Trevor Ariza': 13.3, 'Jeff Green': 13.3, 'Dwight Howard': 21.6, 'Jabari Parker': 16.2, 'Thomas Bryant': 20.5, 'Jordan McRae': 12.3, 'Chasson Randle': 11.5, 'John Jenkins': 12.0}, {'Justin Anderson': 12.9, 'Kent Bazemore': 12.5, 'Jeremy Lin': 15.5, 'Taurean Prince': 12.0, "DeAndre' Bembry": 9.2, 'Miles Plumlee': 13.7, 'John Collins': 19.8, 'Dewayne Dedmon': 15.1, 'Trae Young': 14.2, 'Kevin Huerter': 9.8, 'Omari Spellman': 12.3, 'Jaylen Adams': 11.0, 'Alex Len': 14.6, 'Alex Poythress': 11.9, 'Vince Carter': 18.9}, {'James Harden': 24.2, 'Iman Shumpert': 10.0, 'Eric Gordon': 14.5, 'Nene': 17.1, 'P.J. Tucker': 11.0, 'Chris Paul': 25.4, 'Gerald Green': 13.1, 'Isaiah Hartenstein': 9.6, 'Clint Capela': 22.2, 'Gary Clark': 8.4, 'Vince Edwards': 3.9, 'Danuel House': 12.5, 'Austin Rivers': 10.3, 'Kenneth Faried': 19.7}, {'LaMarcus Aldridge': 20.8, 'Dejounte Murray': 14.2, 'DeMar DeRozan': 17.8, 'Jakob Poeltl': 16.8, 'Derrick White': 14.7, 'Pau Gasol': 21.4, 'Patty Mills': 14.5, 'Rudy Gay': 16.8, 'Davis Bertans': 13.9, 'Lonnie Walker': 0.6, 'Dante Cunningham': 11.2, 'Marco Belinelli': 12.4, 'Bryn Forbes': 10.0, 'Quincy Pondexter': 9.8, 'Chimezie Metu': 8.2, 'Drew Eubanks': 19.9, 'Ben Moore': -2.3}, {'Kristaps Porzingis': 18.3, 'J.J. Barea': 14.5, 'Dwight Powell': 18.1, 'Dorian Finney-Smith': 9.3, 'Courtney Lee': 12.2, 'Justin Jackson': 9.6, 'Tim Hardaway Jr.': 13.6, 'Zach Randolph': 19.3, 'Maxi Kleber': 13.5, 'Trey Burke': 13.8, 'Luka Doncic': 19.4, 'Ryan Broekhoff': 11.1, 'Jalen Brunson': 10.6, 'Dirk Nowitzki': 22.6, 'Daryl Macon': 19.6, 'Devin Harris': 16.1}, {'Anthony Davis': 27.5, 'Stanley Johnson': 8.6, "E'Twaun Moore": 11.4, 'Cheick Diallo': 17.1, 'Solomon Hill': 9.1, 'Jrue Holiday': 16.8, 'Frank Jackson': 9.2, 'Darius Miller': 8.4, 'Jason Smith': 12.9, 'Elfrid Payton': 15.2, 'Julius Randle': 17.5, 'Ian Clark': 10.3, 'Kenrich Williams': 11.1, 'Jahlil Okafor': 16.6, 'Tim Frazier': 12.1}, {'Jonas Valanciunas': 19.7, 'Delon Wright': 15.8, 'Chandler Parsons': 14.9, 'Mike Conley': 17.6, 'Justin Holiday': 10.8, 'Tyler Dorsey': 9.6, 'C.J. Miles': 13.1, 'Dillon Brooks': 9.6, 'Ivan Rabb': 17.6, 'Jaren Jackson Jr.': 17.1, 'Avery Bradley': 11.2, 'Kyle Anderson': 13.6, 'Jevon Carter': 3.5, 'Yuta Watanabe': 7.1, 'Joakim Noah': 17.5, 'Julian Washburn': 1.6, 'Bruno Caboclo': 7.0}]

def sort_all():
	global player_per_list
	new_list = []
	for dic in player_per_list:
		keys = dic.keys()
		keys = sorted(keys, key=lambda x: dic[x], reverse=True)
		new_dic = {}
		i = 0
		while len(new_dic.keys()) < 7:
			if dic[keys[i]] < 32.5 and dic[keys[i]] > 5:
				new_dic[keys[i]] = dic[keys[i]]
			i+=1
		new_list.append(new_dic)
	return new_list

def all_per_by_team_list():
	global player_per_list
	return player_per_list

def all_per_by_team_dict():
	global player_per_list
	teams = team_names()
	dic = {}
	for i in range(len(teams)):
		dic[teams[i]] = player_per_list[i]
	return dic

def all_per_by_team_dict_top_7():
	l = sort_all()
	teams = team_names()
	dic = {}
	for i in range(len(teams)):
		dic[teams[i]] = l[i]
	return dic