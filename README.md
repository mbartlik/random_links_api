# Random Link API

## General Purpose
Depending on which endpoint you send a request to, you get a link to some site related to the category of that endpoint. For example, if you send a request to the game-links endpoint, in response you will get a link to play a game. All links are retrieved from a Google Cloud SQL database. 

## Request Examples and List of Endpoints
- GET https://random-links-api.uk.r.appspot.com/fun-link
- GET https://random-links-api.uk.r.appspot.com/game-link
- GET https://random-links-api.uk.r.appspot.com/news-link

## Response Type
```javascript
{
  "description" : string,
  "link" : string
}
```