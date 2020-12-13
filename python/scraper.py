class JobScrape():
    def __init__(self, site_name,):
        """Having the job sites in a list means we can check on initialisation and throw an error if the site is not available"""
        
        sites =[{"monster": {
                    "url":"https://www.monster.co.uk/jobs/search/",
                    "query_format" : "?q={keywords}}&where={city}}&cy={country}",
                    'results' : '#ResultsContainer'
        }}]
        try:
            self.site_name = site_name
            self.site_data = [site[site_name] for site in sites if site_name in site][0]
        except IndexError:
            raise ValueError(f'{site_name} is not found or not supported yet!')
    #def get_jobs():
        pass

    #def _scrape_site():
        pass

    #def _get_description():
        pass

    #def _format_monster():
        pass
