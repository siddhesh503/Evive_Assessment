### Evive Assessment

Table of Contents
=================

* [General Description](#general-description)
* [Instructions For Execution](#instructions-for-execution)



## General Description

The biggest hurdle of this assignment was to get around 40 Queries per 10 seconds limit of TMDB API. I handled this by keeping a tab on `X-RateLimit-Reset` and `X-RateLimit-Remaining` headers of the response. Following is the example of how Response headers look:

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
Rather than keeping a fixed timeout after the request limit gets exhuasted for a current time winodw, I am keeping a dynamic timeout based on the values of the headers. For example, if we exhaust all the 40 requests in 7 seconds, then my script will wait for only `(10-7=3)` `3` seconds until I make a next request, rather than waiting for a fixed amount of time. This model improves the running time of the script by more than 50%. 

## Instructions For Execution

1. Download the repository as a zip in your home directory
2. Extract the zip file in your home directory
3. cd Evive_Assessment
4. Run this command: `python evive.py`