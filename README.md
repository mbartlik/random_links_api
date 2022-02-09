# Random Link API

## General Purpose
Depending on which endpoint you send a request to, you get a link to some site related to the category of that endpoint. For example, if you send a request to the game-links endpoint, in response you will get a link to play a game. All links are retrieved from a Google Cloud SQL database. 

## Documentation
- Get a random link
  - GET https://random-links-api.uk.r.appspot.com/fun-link
- Add a link to the database
  - POST https://random-links-api.uk.r.appspot.com/fun-link
    - link
    - description
- Update a link AND it's description in the database
  - PATCH https://random-links-api.uk.r.appspot.com/fun-link
    - link
    - description
    - new_link
- Update a link's description in the database
  - PATCH https://random-links-api.uk.r.appspot.com/fun-link
    - link
    - description
- DELETE a link from the database
  - DELETE https://random-links-api.uk.r.appspot.com/fun-link

- Note: the above examples were all shown using the /fun-link endpoint. To use /game-link or /news-link you can just substitute /fun-link with one of those
  - Equivalent forms of GET https://random-links-api.uk.r.appspot.com/fun-link for /game-link and /news-link
  - GET https://random-links-api.uk.r.appspot.com/news-link
  - GET https://random-links-api.uk.r.appspot.com/game-link

## Response Type
```javascript
{
  "description" : string,
  "link" : string
}
```