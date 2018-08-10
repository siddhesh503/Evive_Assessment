### Evive Assessment

Table of Contents
=================

* [Requirements](#requirements)
* [General Description](#general-description)
* [Instructions For Execution](#instructions-for-execution)
* [Miscellaneous Notes](#miscellaneous-notes)


## Requirements

* Python 2.7.0 or higher


## General Description

The biggest hurdle of this assignment was to get around 40 Queries per 10 seconds limit of TMDB API. I handled this by keeping a tab on `X-RateLimit-Reset` and `X-RateLimit-Remaining` headers of the response.

Rather than keeping a fixed timeout after the request limit gets exhuasted for a current time winodw, I am keeping a dynamic timeout based on the values of the headers. For example, if we exhaust all the 40 requests in 7 seconds, then my script will wait for only `(10-7=3)` `3` seconds until I make a next request, rather than waiting for a fixed amount of time. This model improves the running time of the script by more than 50%.

Following is the example of how Response headers look:

**Headers Notes**

* `X-RateLimit-Reset` : denotes the time at which current window will expire.
* `X-RateLimit-Reset` : denotes the number of requests remaining in the current time window.

**Example**

```
HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: ETag, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, Retry-After
Cache-Control: public, max-age=28800
Content-Length: 1339
Content-Type: application/json;charset=utf-8
Date: Wed, 03 May 2017 15:57:05 GMT
ETag: "a2f04167b75be463e8c30b93b473aed1"
Server: openresty
Vary: Accept-Encoding
X-Memc: HIT
X-Memc-Age: 25954
X-Memc-Expires: 2846
X-Memc-Key: a7a8be33582080c3e162cfcb93607b73
X-RateLimit-Limit: 40
X-RateLimit-Remaining: 32
X-RateLimit-Reset: 1493827035
Connection: keep-alive
```
 

## Instructions For Execution

1. Download the repository as a zip in your home directory
2. Extract the zip file in your home directory
3. cd Evive_Assessment
4. Run this command: `python evive.py`


## Miscellaneous Notes

* My current count is 247 but it might be different when you execute it, as, TMDB keeps updating and adding to their data constantly.
* I have tried to make my code as modularized as possible and to avoid as much code duplication as possible and hence all of my utility functions are in the `utils` package in `utils.py` file.
* API results are duplicated across different pages. This affects the resultant count. I am attaching the example of this phenomenon in this documentation. Following are the API results for pages 51 and 52. Ids that are duplicated Are: `{513352, 489297, 500770}`

#### Page: 51
```
{
	'page': 51,
	'total_results': 1030,
	'total_pages': 52,
	'results': [{
		'vote_count': 0,
		'id': 491130,
		'video': False,
		'vote_average': 0,
		'title': 'A.M.A.',
		'popularity': 0.083,
		'poster_path': '/6xPFqihckMfgf25LXwwKB3y3rpY.jpg',
		'original_language': 'en',
		'original_title': 'A.M.A.',
		'genre_ids': [18, 35],
		'backdrop_path': None,
		'adult': False,
		'overview': 'A v-logger takes questions from strangers in a film-related community.',
		'release_date': '2017-12-05'
	}, {
		'vote_count': 0,
		'id': 491198,
		'video': False,
		'vote_average': 0,
		'title': 'Jesper Juhl: Sikke En Joke',
		'popularity': 0.083,
		'poster_path': '/uBesdiQxN2Fu5M1hjqxajji1Xkl.jpg',
		'original_language': 'da',
		'original_title': 'Jesper Juhl: Sikke En Joke',
		'genre_ids': [35],
		'backdrop_path': '/iIo0nOZftj0vu37jmMsrAti2yiL.jpg',
		'adult': False,
		'overview': '',
		'release_date': '2017-12-05'
	}, {
		'vote_count': 0,
		'id': 491500,
		'video': False,
		'vote_average': 0,
		'title': 'Styrofoam',
		'popularity': 0.083,
		'poster_path': '/xOnWkn7kjS89U4scyAZ2Mu5BZJW.jpg',
		'original_language': 'zh',
		'original_title': 'Styrofoam',
		'genre_ids': [99],
		'backdrop_path': None,
		'adult': False,
		'overview': 'Guo Jie is one of the estimated 277 million rural migrant workers in China. In Shanghai, Guo Jie buys and collects styrofoam boxes from markets selling fresh produce. She takes them to a seafood wholesale market where she resells them to wholesalers who will store fish in the boxes.',
		'release_date': '2017-12-03'
	}, {
		'vote_count': 0,
		'id': 496522,
		'video': False,
		'vote_average': 0,
		'title': 'A Thin Place',
		'popularity': 0.083,
		'poster_path': '/2tZfUD0pwpYU3US8fRyxCCTcail.jpg',
		'original_language': 'en',
		'original_title': 'A Thin Place',
		'genre_ids': [],
		'backdrop_path': '/zMJCbUdid9xGmQKg5dZuwU5sSK.jpg',
		'adult': False,
		'overview': 'Grace, a young heroin addict and Jamie, her alcoholic doctor, imprisoned by the horror of addiction and sexual co-dependency take a powerful natural hallucinogenic in order to travel the spiritual road to recovery. Whilst seeking the truth to their present and past behaviour but driven by self-obsession and malevolent denial, far from leading to salvation, the road they actually travel leads them to a place from which they may never return. A place where the truth is more horrific than the lies they tell themselves. One person from a past that connects them both holds the key to their new place of captivity and that person is in no hurry to leave.',
		'release_date': '2017-12-04'
	}, {
		'vote_count': 0,
		'id': 493848,
		'video': False,
		'vote_average': 0,
		'title': 'Slay Bells Ring: The Story of Silent Night, Deadly Night',
		'popularity': 0.083,
		'poster_path': '/20HI7oqjcPrgE8MTMFdGKef9DgM.jpg',
		'original_language': 'en',
		'original_title': 'Slay Bells Ring: The Story of Silent Night, Deadly Night',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': 'Documentary on the cult Christmas horror classic Silent Night, Deadly Night.',
		'release_date': '2017-12-05'
	}, {
		'vote_count': 0,
		'id': 421363,
		'video': False,
		'vote_average': 0,
		'title': 'Istanbul Story',
		'popularity': 0.082,
		'poster_path': '/9gHsiaKZanq3XnSIAyAN5Dd7gc1.jpg',
		'original_language': 'en',
		'original_title': 'Istanbul Story (Μια ιστορία της Πόλης)',
		'genre_ids': [12, 18, 10751],
		'backdrop_path': None,
		'adult': False,
		'overview': 'Katia’s unexpected journey to Istanbul traps her in a chain of adventures enacted on the front of her disrupted childhood. She discovers her mother’s secrets and faces her own inner desires and dilemmas.',
		'release_date': '2017-12-01'
	}, {
		'vote_count': 0,
		'id': 490592,
		'video': False,
		'vote_average': 0,
		'title': 'All Is Forgiven, for We Have Been Happy',
		'popularity': 0.082,
		'poster_path': '/prINYk9f92Y1RnBY9KiYSvOBHgh.jpg',
		'original_language': 'id',
		'original_title': 'Semua Sudah Dimaafkan sebab Kita Pernah Bahagia',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': 'The film tells the story of Leon Agusta (1938-2015), a poet, cultural activist, and playwright who was born in Sigiran, Lake ManinJau, West Sumatra. Leon’s craft was fueled by pain of the past from the tragedies, betrayals, and the many instances love has touched his life. His activism was driven by his love of his birthplace and the betterment of others. Semua Sudah Dimaafkan sebab Kita Pernah Bahagia sees Paul Agusta; Leon’s youngest son recounts what he remembers of his father as well as following him to trace back Leon’s early years to find the roots of his passion and pain to further know the complex individual that was his father, Leon Agusta.',
		'release_date': '2017-12-02'
	}, {
		'vote_count': 0,
		'id': 490907,
		'video': False,
		'vote_average': 0,
		'title': 'Where is Tomorrow, Shuji Terayama',
		'popularity': 0.082,
		'poster_path': '/d6VIz5ZxQFjgQPJXal4QwCHEWca.jpg',
		'original_language': 'ja',
		'original_title': 'Ashita wa docchi da, Terayama Shûji',
		'genre_ids': [99],
		'backdrop_path': None,
		'adult': False,
		'overview': 'The documentary to find the "true Shuji Terayama".',
		'release_date': '2017-12-02'
	}, {
		'vote_count': 0,
		'id': 496894,
		'video': False,
		'vote_average': 0,
		'title': 'Alien Contact: NASA Exposed 2',
		'popularity': 0.082,
		'poster_path': '/u8cnyEpQmAadtNoWQ5bte8AGmog.jpg',
		'original_language': 'en',
		'original_title': 'Alien Contact: NASA Exposed 2',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': 'A former astronaut recently went on record to allege that there is abundant evidence that we are being contacted by Alien races and that these civilizations have been visiting us for a very long time. These claims also state that the Alien creatures appearance "is bizarre compared to any type of traditional western point of view and that these visitors use the technologies of consciousness and that they use "toroids," co-rotating magnetic disks for their propulsion systems. In addition, the recent discovery of 1,300 exoplanets that could sustain life has rocked the scientific world. Now more and more people, from world leaders to former astronauts, are testifying that UFOs not only exist, but that Aliens are here and have been monitoring the human race for centuries.',
		'release_date': '2017-12-01'
	}, {
		'vote_count': 0,
		'id': 511971,
		'video': False,
		'vote_average': 0,
		'title': 'Insoumise',
		'popularity': 0.082,
		'poster_path': None,
		'original_language': 'fr',
		'original_title': 'Insoumise',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': '',
		'release_date': '2017-12-01'
	}, {
		'vote_count': 0,
		'id': 516106,
		'video': False,
		'vote_average': 0,
		'title': 'An Ornament of Faith',
		'popularity': 0.082,
		'poster_path': '/feTYlQlkF3xRWOlEIE5UOHcGNtg.jpg',
		'original_language': 'en',
		'original_title': 'An Ornament of Faith',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': "Set in the stark, harsh industrial fringes of the City, a parolee's fraternal love for his sociopath sister is put to the test by a paternal Parole Officer, with emotionally shattering results.",
		'release_date': '2017-12-02'
	}, {
		'vote_count': 0,
		'id': 534665,
		'video': False,
		'vote_average': 0,
		'title': 'Ferida',
		'popularity': 0.082,
		'poster_path': '/7uVex9WAYT2Swb0AhqaX2RURTH7.jpg',
		'original_language': 'pt',
		'original_title': 'Ferida',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': 'Kira, Sioux, Mo and Hemera live in an abandoned shed. They need each other to escape from nature itself. However, there are rules in the everyday that must be followed so that they remain in peace. Kira breaks down the most important of them: not to talk to their victims - and so discovers that there are wounds that surpass the surfaces.',
		'release_date': '2017-12-01'
	}, {
		'vote_count': 0,
		'id': 492474,
		'video': False,
		'vote_average': 0,
		'title': 'Just in Time',
		'popularity': 0.082,
		'poster_path': None,
		'original_language': 'en',
		'original_title': 'Just in Time',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': "A man at the cinema finds out that the movie he's watching is a little more interactive than he expected...",
		'release_date': '2017-12-01'
	}, {
		'vote_count': 0,
		'id': 491490,
		'video': False,
		'vote_average': 0,
		'title': 'The Coolest Village in Britain',
		'popularity': 0.082,
		'poster_path': '/61MbzsmK2pDT45wD3VZhfSUa0qO.jpg',
		'original_language': 'en',
		'original_title': 'The Coolest Village in Britain',
		'genre_ids': [99],
		'backdrop_path': None,
		'adult': False,
		'overview': 'A short documentary about the village of Moniave.',
		'release_date': '2017-12-03'
	}, {
		'vote_count': 0,
		'id': 501867,
		'video': False,
		'vote_average': 0,
		'title': 'Mugabo',
		'popularity': 0.082,
		'poster_path': None,
		'original_language': 'en',
		'original_title': 'Mugabo',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': "Mugabo is an experimental short film about a young girl's return to the idealised homeland, a journey to a place full of borrowed memories. Director Amelia Umuhire, a Rwandese filmmaker living in Germany, also directed and produced the fictional web series Polyglot about the lives of young black artists in Europe.",
		'release_date': '2017-12-01'
	}, {
		'vote_count': 0,
		'id': 489297,
		'video': False,
		'vote_average': 0,
		'title': 'Night of Hunt',
		'popularity': 0.081,
		'poster_path': None,
		'original_language': 'en',
		'original_title': '사냥의 밤',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': 'The Night come, All Light disappear. Everyone lost their way, so it is great for hunting.',
		'release_date': '2017-12-01'
	}, {
		'vote_count': 0,
		'id': 500770,
		'video': False,
		'vote_average': 0,
		'title': 'Pagine nascoste',
		'popularity': 0.081,
		'poster_path': '/hm0ze3ZuPu4gf1zneYdtTAKChnE.jpg',
		'original_language': 'it',
		'original_title': 'Pagine nascoste',
		'genre_ids': [],
		'backdrop_path': '/6zgFSyDK7rxFqkcd4Tlch8zmkk0.jpg',
		'adult': False,
		'overview': '',
		'release_date': '2017-12-01'
	}, {
		'vote_count': 0,
		'id': 519575,
		'video': False,
		'vote_average': 0,
		'title': 'H',
		'popularity': 0.081,
		'poster_path': '/p9wTBQecCBNyvkYSWpVaYcmQiT4.jpg',
		'original_language': 'en',
		'original_title': 'H',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': 'An animated short about the chaos of war.',
		'release_date': '2017-12-01'
	}, {
		'vote_count': 0,
		'id': 512716,
		'video': False,
		'vote_average': 0,
		'title': 'The Making of Tex Murphy',
		'popularity': 0.081,
		'poster_path': '/7iSmvRCXkJxj6WYeIl46fJwVa9M.jpg',
		'original_language': 'en',
		'original_title': 'The Making of Tex Murphy',
		'genre_ids': [99],
		'backdrop_path': None,
		'adult': False,
		'overview': "From humble beginnings in amateur film, to a multi award-winning video game franchise, this documentary explores the history of one of the world's longest-running and influential Adventure Game icons: Tex Murphy.",
		'release_date': '2017-12-02'
	}, {
		'vote_count': 0,
		'id': 513352,
		'video': False,
		'vote_average': 0,
		'title': 'The Surrogate',
		'popularity': 0.081,
		'poster_path': '/FOww0v8QRSNDsx6rKQsc7FwTZ3.jpg',
		'original_language': 'en',
		'original_title': 'The Surrogate',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': 'Juliana Bach suffers from an anxiety disorder caused by a proliferation of augmented and virtual realities in her daily life. After struggling with the disorder and experimenting with various treatments, she decides to hire a “Surrogate” to assume her physical presence. You choose how to follow the narrative, navigate the passageways, and see into the various rooms through the live action portals that offer an immersive vantage point. The story builds to a dramatic conclusion in which both Juliana and the Surrogate face the potential sublimation of their identities – two halves of a nearly merged new whole.',
		'release_date': '2017-12-02'
	}]
}
```

#### Page: 52
```
{
	'page': 52,
	'total_results': 1030,
	'total_pages': 52,
	'results': [{
		'vote_count': 0,
		'id': 513352,
		'video': False,
		'vote_average': 0,
		'title': 'The Surrogate',
		'popularity': 0.081,
		'poster_path': '/FOww0v8QRSNDsx6rKQsc7FwTZ3.jpg',
		'original_language': 'en',
		'original_title': 'The Surrogate',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': 'Juliana Bach suffers from an anxiety disorder caused by a proliferation of augmented and virtual realities in her daily life. After struggling with the disorder and experimenting with various treatments, she decides to hire a “Surrogate” to assume her physical presence. You choose how to follow the narrative, navigate the passageways, and see into the various rooms through the live action portals that offer an immersive vantage point. The story builds to a dramatic conclusion in which both Juliana and the Surrogate face the potential sublimation of their identities – two halves of a nearly merged new whole.',
		'release_date': '2017-12-02'
	}, {
		'vote_count': 0,
		'id': 522881,
		'video': False,
		'vote_average': 0,
		'title': 'The Distant Echo',
		'popularity': 0.081,
		'poster_path': '/3Vfg331z8CGb3qTyDpDMorrArMR.jpg',
		'original_language': 'en',
		'original_title': 'The Distant Echo',
		'genre_ids': [878],
		'backdrop_path': None,
		'adult': False,
		'overview': 'A Star Wars Fan Film',
		'release_date': '2017-12-02'
	}, {
		'vote_count': 0,
		'id': 489297,
		'video': False,
		'vote_average': 0,
		'title': 'Night of Hunt',
		'popularity': 0.081,
		'poster_path': None,
		'original_language': 'en',
		'original_title': '사냥의 밤',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': 'The Night come, All Light disappear. Everyone lost their way, so it is great for hunting.',
		'release_date': '2017-12-01'
	}, {
		'vote_count': 0,
		'id': 501870,
		'video': False,
		'vote_average': 0,
		'title': 'Unearthing. In Conversation.',
		'popularity': 0.081,
		'poster_path': None,
		'original_language': 'en',
		'original_title': 'Unearthing. In Conversation.',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': 'The seats in the theatre are still empty when the performer – the artist – enters the frame. She speaks about a colonial flashback. She is haunted by a series of historic photographs of or taken by the Austrian ethnographer Paul Schebesta in the 1930s, in the Belgian colony of the Congo.',
		'release_date': '2017-12-01'
	}, {
		'vote_count': 0,
		'id': 500770,
		'video': False,
		'vote_average': 0,
		'title': 'Pagine nascoste',
		'popularity': 0.081,
		'poster_path': '/hm0ze3ZuPu4gf1zneYdtTAKChnE.jpg',
		'original_language': 'it',
		'original_title': 'Pagine nascoste',
		'genre_ids': [],
		'backdrop_path': '/6zgFSyDK7rxFqkcd4Tlch8zmkk0.jpg',
		'adult': False,
		'overview': '',
		'release_date': '2017-12-01'
	}, {
		'vote_count': 0,
		'id': 514706,
		'video': False,
		'vote_average': 0,
		'title': 'Other News',
		'popularity': 0.081,
		'poster_path': '/gmnN82g4LJBy5HC8hUkjkwC2ubQ.jpg',
		'original_language': 'en',
		'original_title': 'Other News',
		'genre_ids': [878],
		'backdrop_path': None,
		'adult': False,
		'overview': 'Newspaper Man delivers the truth from alternative dimensions and timelines.',
		'release_date': '2017-12-02'
	}, {
		'vote_count': 0,
		'id': 531246,
		'video': False,
		'vote_average': 0,
		'title': 'Les 7 Doigts De La Main - Reversible - (Cirque)',
		'popularity': 0.081,
		'poster_path': '/p5C6QYNeyGU0MLACN4qMAPOXz55.jpg',
		'original_language': 'fr',
		'original_title': 'Les 7 Doigts De La Main - Reversible - (Cirque)',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': '',
		'release_date': '2017-12-01'
	}, {
		'vote_count': 0,
		'id': 539272,
		'video': False,
		'vote_average': 0,
		'title': 'Sin Cielo',
		'popularity': 0.015,
		'poster_path': '/67ZPLceQAVSDvLtHzFDV4U09gPB.jpg',
		'original_language': 'es',
		'original_title': 'Sin Cielo',
		'genre_ids': [],
		'backdrop_path': None,
		'adult': False,
		'overview': '',
		'release_date': '2017-12-02'
	}, {
		'vote_count': 0,
		'id': 541373,
		'video': False,
		'vote_average': 0,
		'title': 'Stains and Scratches',
		'popularity': 0,
		'poster_path': None,
		'original_language': 'lt',
		'original_title': 'Dėmės ir įbrėžimai',
		'genre_ids': [99],
		'backdrop_path': None,
		'adult': False,
		'overview': 'Experimental film',
		'release_date': '2017-12-28'
	}, {
		'vote_count': 1,
		'id': 541442,
		'video': False,
		'vote_average': 10,
		'title': 'Mare mosso',
		'popularity': 0,
		'poster_path': '/uxPkrVqvq5hTkItgLqVwuoSjk9i.jpg',
		'original_language': 'it',
		'original_title': 'Mare mosso',
		'genre_ids': [18, 53],
		'backdrop_path': '/r3asxBXudhlaBvwg0DxNxQ369mw.jpg',
		'adult': False,
		'overview': '',
		'release_date': '2017-12-31'
	}]
}
```