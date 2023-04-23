#!/usr/bin/env zsh

cd api

uvicorn main:app --reload &

cd ../frontend

npm run dev -- --open
