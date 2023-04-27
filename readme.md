# Gamer's Delight

Gamer's Delight (by Gamers Unite) is our COP3530 final project written with FastAPI and SvelteKit. Using a database of video game details and ratings, you can input a game (or qualities of a game) and get back a list of similar games sorted with various algorithms.

# Installing and Running

Clone this project (`git clone https://github.com/Herschenglime/gamers-delight`).

This guide assumes you have NodeJS, Python 3, and pip installed. If you don't have those things, look up "install X on Y OS" and you should be ready.

## FastAPI
Type `pip install "fastapi[all]"` in your terminal to pull in what is needed for the backend. 

To run just the backend, go into the api folder (`cd api`) and type `uvicorn main:app --reload`. This will start the FastAPI process which will take up the terminal screen. Open a new terminal tab or window for the next step. 

## SvelteKit
Navigate to the `frontend` folder (`cd ../frontend` if you're still in `api`). Run `npm install` to pull in the dependencies for the project. Once that's done, you can do `npm run dev -- --open` to start the server and open the webpage, or just `npm run dev` to start the server but not open the site in a browser.

## dev.sh
Included for convenience is a shell script to run both of these at once to start the server, accessed by running `./dev.sh` (if on Mac/Linux/WSL). If the SvelteKit server starts too quickly, it's possible that it loads in before the API starts, which could lead to a 500 error. Just refresh the page and it should work.
