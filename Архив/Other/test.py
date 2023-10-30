links_soccerway = []
with open('links_soccerway.txt', 'r') as file:
    for line in file:
        links_soccerway.append(line.strip())
result = []
for link in links_soccerway:
    date = link.split('/')
    date = f'{date[4]}-{date[5]}-{date[6]}'
    match_id = link.split('/')[-2]
    print(f'http://192.168.31.95:12320/soccerway_parser_match/date={date}&id={match_id}')
