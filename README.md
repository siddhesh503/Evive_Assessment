### Evive Assessment

Table of Contents
=================

* [General Description](#general-description)
* [Instructions For Execution](#instructions-for-execution)



## General Description
The biggest hurdle of this assignment was to get around 40 Queries/second limit of TMDB API. I handled this by keeping a tab on `X-RateLimit-Reset` and `X-RateLimit-Remaining` headers of the response. Following is the example of how Response headers look:

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
##X-RateLimit-Remaining: 32
##X-RateLimit-Reset: 1493827035
Connection: keep-alive
```