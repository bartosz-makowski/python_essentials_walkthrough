from scraper import JobScrape

monster = JobScrape("monster")

print('working bitch')

monster_results = monster.get_jobs('hatfield','uk', 'web-developer')

for result in monster_results:
    print(f"Job title: {result['title']}")
    print('..................')
    print(f"Company: {result['company']}")
    print('..................')
    print(f"Job URL: {result['url']}")
    print('..................')
    

    if 'description' in result:
        print(f"Description: {result['description']}")
        print('.......END...........')

print(f'{len(monster_results)} jobs found')
