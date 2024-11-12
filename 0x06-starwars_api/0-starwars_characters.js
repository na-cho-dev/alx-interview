#!/usr/bin/node
const request = require('request');

const requestPromise = (url) => {
  const promise = new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else if (res && res.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(
          new Error(
            `Failed to fetch data. Status Code: ${res && res.statusCode}`
          )
        );
      }
    });
  });

  return promise;
};

const requestsAPI = async (url) => {
  try {
    const data = await requestPromise(url);
    const body = data.characters ? data.characters : data.name;
    // console.log(body);

    if (body instanceof Array) {
      for (const people of body) {
        await requestsAPI(people);
      }
    } else {
      console.log(body);
    }
  } catch (err) {
    console.error('Error fetching data:', err);
  }
};

(function printStarWarsCharacter () {
  const args = process.argv;

  if (args.length !== 3) {
    console.log('Script requires one argument');
    return;
  }

  const movieID = args[2];

  requestsAPI(`https://swapi-api.alx-tools.com/api/films/${movieID}`);
})();
