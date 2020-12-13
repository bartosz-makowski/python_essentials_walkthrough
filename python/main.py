from scraper import JobScrape

monster = JobScrape("monster")

monster_results = monster.get_jobs('hatfield','uk', 'web-developer')