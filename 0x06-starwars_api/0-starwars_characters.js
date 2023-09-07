#!/usr/bin/node

const request = require('request-promise')

async function getCharacterName(characterUrl) {
  try {
    const character = await request(characterUrl);
    return JSON.parse(character).name;
  } catch (error) {
    throw new Error(`Error retrieving character: ${error}`)
  }
  
}

async function getCharacters(movieId) {
  try {
    const film = await request(`https://swapi.dev/api/films/${movieId}/`);
    const characters = JSON.parse(film).characters;

    for (const characterUrl of characters) {
      const characterName = await getCharacterName(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    throw new Error(`Error retrieving film: ${error}`)
  }
}

const movieId = process.argv[2];
getCharacters(movieId)
